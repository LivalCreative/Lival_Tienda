"""Genera ocupacion.json (público, sin nombres ni montos) a partir de los pedidos del tablero Pedidos 3D.

Uso: python3 tools/ocupacion.py pedidos.json > ocupacion.json
pedidos.json: lista de documentos [{"id": "p-0001", "data": {...}}, ...] o un JSON por línea.
"""
import json, sys, math, datetime, zoneinfo

CUPO_POR_DIA = 4        # entregas máximas por fecha
HORAS_POR_DIA = 16      # horas de impresión que salen en un día (2 impresoras)
HORAS_DEFAULT = 1.5     # horas por pieza cuando no la conocemos

def cargar(path):
    txt = open(path, encoding="utf-8").read().strip()
    try:
        docs = json.loads(txt)
    except json.JSONDecodeError:
        docs = [json.loads(l) for l in txt.splitlines() if l.strip().startswith("{")]
    return [d.get("data", d) for d in docs]

def main():
    hoy = datetime.datetime.now(zoneinfo.ZoneInfo("America/Mexico_City")).date()
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
                    horas += HORAS_DEFAULT * int(pr.get("cantidad", 1) or 1)
    out = {
        "actualizado": datetime.datetime.now(zoneinfo.ZoneInfo("America/Mexico_City")).isoformat(timespec="minutes"),
        "cupo_por_dia": CUPO_POR_DIA,
        "horas_por_dia": HORAS_POR_DIA,
        "horas_pendientes": round(horas, 1),
        "entregas_por_fecha": dict(sorted(por_fecha.items())),
    }
    print(json.dumps(out, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
