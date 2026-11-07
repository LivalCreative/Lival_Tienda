"""Genera pedido/index.html (checkout compartido) a partir de duende/index.html.
Uso: python3 tools/build_pedido.py   (córrelo cada vez que cambie duende/index.html)"""
import os, re
h = open("duende/index.html", encoding="utf-8").read()
def rep(a, b):
    global h
    assert a in h, a[:80]
    h = h.replace(a, b, 1)
rep("<title>Travesuras del Duende · Lival Creative Studio</title>", "<title>Tu pedido · Lival Creative Studio</title>")
# El Duende puede estar en pausa (redirige al inicio); el pedido no debe heredar esa redirección
h = re.sub(r"<!-- DUENDE-PAUSA.*?<!-- /DUENDE-PAUSA -->\n?", "", h, flags=re.S)
rep("<body>", '<body class="solo-pedido temporada-navidad">')
# Tema de temporada (nieve); quítalo en enero junto con el de las demás páginas
h = re.sub(r'(<link rel="stylesheet" href="\.\./assets/lival\.css\?v=([0-9a-z]+)">)', r'\1\n<link rel="stylesheet" href="../assets/temporada.css?v=\2">', h, count=1)
# En la barra, "Mi pedido" es la página actual
rep('<a class="bolsa" href="#pedido">', '<a class="bolsa" href="#pedido" aria-current="page">')
rep("</style>", """
.solo-pedido .hero, .solo-pedido nav.pills, .solo-pedido #paquete, .solo-pedido #cats, .solo-pedido #bar, .solo-pedido #como-duende, .solo-pedido .cred-duende { display: none !important; }
.solo-pedido { padding-bottom: 24px; }
.solo-pedido #pedido { margin-top: 8px; }
#pedido > h1 { font-size: var(--t2); color: var(--pine); }
.seguir { display: inline-flex; align-items: center; min-height: 44px; font-weight: 800; color: var(--pine); }
</style>""")
rep('<p class="sub">Escribe tu nombre y mándanos tu pedido por WhatsApp. Ahí acordamos la entrega.</p>',
    '<p class="sub">Escribe tu nombre y mándanos tu pedido por WhatsApp. Ahí acordamos la entrega. <a class="seguir" href="../">← Seguir comprando</a></p>')
rep("<h2>Tu pedido</h2>", "<h1>Tu pedido</h1>")
rep("Todavía no eliges nada. Usa los botones + de arriba.", 'Tu carrito está vacío. Elige tus regalos en <a href="../navidad/">Navidad</a>.')
# El pedido no muestra las fotos del duende: no las cargamos (la página pesaba 1.8 MB)
h, n = re.subn(r"FOTOS = \{.*?\};", "FOTOS = {};", h, count=1, flags=re.S)
assert n == 1, "no encontré FOTOS en duende/index.html"
os.makedirs("pedido", exist_ok=True)
open("pedido/index.html", "w", encoding="utf-8").write(h)
print("pedido/index.html listo")
