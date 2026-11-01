"""Genera pedido/index.html (checkout compartido) a partir de duende/index.html.
Uso: python3 tools/build_pedido.py   (córrelo cada vez que cambie duende/index.html)"""
import os
h = open("duende/index.html", encoding="utf-8").read()
def rep(a, b):
    global h
    assert a in h, a[:80]
    h = h.replace(a, b, 1)
rep("<title>Travesuras del Duende · Lival Creative Studio</title>", "<title>Tu pedido · Lival Creative Studio</title>")
rep("<body>", '<body class="solo-pedido">')
# En la barra, "Mi pedido" es la página actual
rep('<a class="link" href="../duende/" aria-current="page">Duende</a>', '<a class="link" href="../duende/">Duende</a>')
rep('<a class="bolsa" href="#pedido">', '<a class="bolsa" href="#pedido" aria-current="page">')
rep("</style>", """
.solo-pedido .hero, .solo-pedido nav.pills, .solo-pedido #paquete, .solo-pedido #cats, .solo-pedido #bar { display: none !important; }
.solo-pedido { padding-bottom: 24px; }
.solo-pedido #pedido { margin-top: 8px; }
#pedido > h1 { font-size: var(--t2); color: var(--pine); }
.seguir { display: inline-flex; align-items: center; min-height: 44px; font-weight: 800; color: var(--pine); }
</style>""")
rep('<p class="sub">Llena tus datos. Al final se arma un mensaje con todo para mandarlo por WhatsApp.</p>',
    '<p class="sub">Llena tus datos. Al final se arma un mensaje con todo para mandarlo por WhatsApp. <a class="seguir" href="../">← Seguir comprando</a></p>')
rep("<h2>Tu pedido</h2>", "<h1>Tu pedido</h1>")
rep("Todavía no eliges nada. Usa los botones + de arriba.", 'Tu carrito está vacío. Elige en <a href="../duende/">Travesuras del Duende</a> o en <a href="../navidad/">Navidad</a>.')
os.makedirs("pedido", exist_ok=True)
open("pedido/index.html", "w", encoding="utf-8").write(h)
print("pedido/index.html listo")
