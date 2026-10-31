"""Genera pedido/index.html (checkout compartido) a partir de duende/index.html.
Uso: python3 tools/build_pedido.py   (córrelo cada vez que cambie duende/index.html)"""
import os
h = open("duende/index.html", encoding="utf-8").read()
def rep(a, b):
    global h
    assert a in h, a[:80]
    h = h.replace(a, b, 1)
rep("<title>Travesuras del Duende · Lival Creative Studio</title>", "<title>Tu pedido · Lival Creative Studio</title>")
rep("<body>", """<body class="solo-pedido">
<div class="ped-top"><a href="../">← Seguir comprando</a><span><a href="../duende/">🎅 Duende</a> · <a href="../navidad/">🎄 Navidad</a></span></div>""")
rep("</style>", """
.solo-pedido header.hero, .solo-pedido nav.pills, .solo-pedido #paquete, .solo-pedido #cats, .solo-pedido #bar { display: none !important; }
.solo-pedido { padding-bottom: 24px; }
.ped-top { display: flex; justify-content: space-between; gap: 10px; flex-wrap: wrap; padding: 12px 16px; background: var(--pine); font-weight: 800; }
.ped-top a { color: #fff; text-decoration: none; }
</style>""")
rep("Todavía no eliges nada. Usa los botones + de arriba.", 'Tu carrito está vacío. Elige en <a href="../duende/">Travesuras del Duende</a> o en <a href="../navidad/">Navidad</a>.')
os.makedirs("pedido", exist_ok=True)
open("pedido/index.html", "w", encoding="utf-8").write(h)
print("pedido/index.html listo")
