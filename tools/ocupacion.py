"""Genera ocupacion.json (público, sin nombres ni montos) a partir de los pedidos del tablero Pedidos 3D.

Uso: python3 tools/ocupacion.py pedidos.json > ocupacion.json
pedidos.json: lista de documentos [{"id": "p-0001", "data": {...}}, ...] o un JSON por línea.

Además de las fechas ocupadas calcula el cupo de Navidad: cuántas horas de impresión quedan libres
antes del corte (23 de diciembre). La tienda deja de aceptar piezas grandes (8 h o más) cuando ya no
caben en esas horas libres, empezando por las más grandes. Se guarda una reserva para piezas chicas.
"""
import json, sys, os, re, unicodedata, datetime, zoneinfo

CUPO_POR_DIA = 4        # entregas máximas por fecha
HORAS_POR_DIA = 16      # horas de impresión que salen en un día (2 impresoras)
HORAS_DEFAULT = 1.5     # horas por pieza cuando no la reconocemos
CORTE_NAVIDAD = "12-23" # último día para imprimir lo que se entrega antes de Navidad
DIAS_SIN_IMPRESION = {5} # sábado (0 = lunes)
RESERVA_MIN = 32        # horas que siempre se guardan para piezas chicas (2 días)
RESERVA_PCT = 0.25      # o el 25 % de lo que queda, lo que sea mayor
PIEZA_GRANDE = 8        # horas a partir de las cuales una pieza cuenta como grande

AQUI = os.path.dirname(os.path.abspath(__file__))
TZ = zoneinfo.ZoneInfo("America/Mexico_City")


def norm(s):
    s = unicodedata.normalize("NFD", str(s).lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", s).split())


def catalogo():
    """Nombre del producto (como sale en el pedido de WhatsApp) -> horas de impresión."""
    h = {}
    try:
        for p in json.load(open(os.path.join(AQUI, "navidad_productos.json"), encoding="utf-8")):
            hs = [o["horas"] for o in p["opciones"]]
            h[norm(p["nombre"])] = max(hs)
            for o in p["opciones"]:
                h[norm(f'{p["nombre"]} {o["label"]}')] = o["horas"]
    except FileNotFoundError:
        pass
    h.update({norm("Foco navideño"): 1.42, norm("Set de 4 focos navideños"): 5.68,
              norm("Chimenea navideña"): 10.67, norm("Chimenea con botas"): 10.67,
              norm("Casita de jengibre para utensilios"): 11.41,
              norm("Casita de jengibre para utensilios interior abierto"): 9.67,
              norm("Casita de jengibre para utensilios interior con divisiones"): 11.41,
              norm("Paquete de 24 travesuras"): 93.9})
    return h


def horas_de(producto, cat):
    if isinstance(producto.get("horas"), (int, float)):
        return float(producto["horas"])
    n = norm(producto.get("nombre", ""))
    if n in cat:
        return cat[n]
    # el nombre más largo del catálogo que aparezca dentro del nombre del pedido
    m = [k for k in cat if len(k) >= 6 and (k in n)]
    return cat[max(m, key=len)] if m else HORAS_DEFAULT


def cargar(path):
    txt = open(path, encoding="utf-8").read().strip()
    try:
        docs = json.loads(txt)
    except json.JSONDecodeError:
        docs = [json.loads(l) for l in txt.splitlines() if l.strip().startswith("{")]
    return [d.get("data", d) for d in docs]


def main():
    ahora = datetime.datetime.now(TZ)
    hoy = ahora.date()
    cat = catalogo()
    pedidos = cargar(sys.argv[1])
    por_fecha, horas = {}, 0.0
    for p in pedidos:
        if p.get("estado") in ("entregado", "cancelado"):
            continue
        f = (p.get("entrega") or {}).get("fecha")
        if f and f >= hoy.isoformat():
            por_fecha[f] = por_fecha.get(f, 0) + 1
        if p.get("estado") != "listo":
            for pr in p.get("productos", []):
                if not pr.get("listo"):
                    horas += horas_de(pr, cat) * int(pr.get("cantidad", 1) or 1)

    corte = datetime.date.fromisoformat(f"{hoy.year}-{CORTE_NAVIDAD}")
    dias = sum(1 for k in range(1, (corte - hoy).days + 1)
               if (hoy + datetime.timedelta(days=k)).weekday() not in DIAS_SIN_IMPRESION) if corte > hoy else 0
    capacidad = dias * HORAS_POR_DIA
    reserva = max(RESERVA_MIN, RESERVA_PCT * capacidad) if capacidad else 0
    libres = max(0.0, capacidad - horas - reserva)

    out = {
        "actualizado": ahora.isoformat(timespec="minutes"),
        "cupo_por_dia": CUPO_POR_DIA,
        "horas_por_dia": HORAS_POR_DIA,
        "horas_pendientes": round(horas, 1),
        "entregas_por_fecha": dict(sorted(por_fecha.items())),
        "navidad": {
            "corte": corte.isoformat(),
            "capacidad_horas": capacidad,
            "reserva_horas": round(reserva, 1),
            "horas_libres": round(libres, 1),
            "pieza_grande_horas": PIEZA_GRANDE,
        },
    }
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
