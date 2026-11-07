"""Genera assets/navidad-productos.js con los productos de la colección Navidad 2026.

Precio = (costo × 2) + $15 por hora + $30, redondeado a terminación 9, mínimo $49.
Costo = gramos × $0.25 + horas × $0.75 (+ extras como foto impresa y listón).
Uso: python3 tools/navidad_productos.py
"""
import json

FIL, MAQ = 0.25, 0.75
FOTO = 7  # foto impresa + listón (estimado)
CDN = "https://makerworld.bblmw.com/makerworld/model/"


def costo(h, g, extra=0):
    return round(g * FIL + h * MAQ + extra, 2)


def precio(h, g, extra=0):
    x = costo(h, g, extra) * 2 + 15 * h + 30
    p = round((x - 9) / 10) * 10 + 9
    return max(49, int(p))


# id, nombre, badge, lead, bullets, fotos (rutas CDN), opciones [(clave, etiqueta, sub, h, g, extra)], personal
P = [
 ("14093", "Letrero ¡Jo, Jo, Jo!", "🎄 Decoración", "Las letras de ¡HO HO HO! convertidas en personajes navideños. Perfecto para la mesa de dulces, un librero o la entrada de tu casa.",
  ["Cada letra es un personaje: Santa, muñeco de nieve, reno y más.", "Base de una pieza que se para sola.", "Colores vivos y alegres."],
  ["US17955e7a9c0e2f/design/2023-09-02_79xbtwml7vhs.jpeg", "US17955e7a9c0e2f/design/2023-09-02_9431aur72zuy.jpeg"],
  [("a", "Santa, muñeco de nieve y reno", "", 5.02, 178, 0), ("b", "Duende, esfera y muñeco de nieve", "", 5.05, 179, 0)], None),
 ("797351", "Cámara de Santa (domo)", "🎅 Para la magia", "Una cámara de vigilancia de mentira que \"transmite al Polo Norte\". Ideal para que los niños se porten bien en diciembre.",
  ["Mide 8 cm de diámetro: discreta pero se nota.", "Ligera, se cuelga con un tornillo o cinta.", "En rojo y negro con la palabra SANTA."],
  ["US4a91d42924f20f/design/2024-11-17_97caa375d97958.jpg", "US4a91d42924f20f/design/2024-11-17_4c0c796c20338.jpg"],
  [("u", "Cámara de Santa", "", 3.39, 81, 0)], None),
 ("817845", "Árbol de la Familia con Nombres", "🎁 Personalizado", "Un arbolito con una esfera para cada integrante de la familia y su nombre. Para colgar en el árbol o regalar.",
  ["De 3 a 5 integrantes.", "Cada esfera lleva un nombre.", "Ligero, perfecto para el árbol."],
  ["US8dd726cfee8dad/design/2024-11-24_1f0761859207.jpg", "US8dd726cfee8dad/design/2024-11-24_dcf1e45992b03.jpg"],
  [("u", "Árbol familiar", "3 a 5 nombres", 0.81, 18, 0)],
  {"label": "Nombres (de 3 a 5, separados por coma)", "ph": "Ej. Ana, Luis, Sofía, Mateo", "max": 60}),
 ("1935739", "Hombre de Jengibre Flexible", "🍪 Para jugar", "Un hombrecito de jengibre articulado que se mueve y se dobla. Divertido para los niños y para decorar.",
  ["Articulado: brazos y piernas que se mueven.", "Con gorrito navideño.", "Ideal para detalles y bolsitas de regalo."],
  ["USc6cf2d8e796cb6/design/2025-10-28_5eeb9e2ed79818.jpeg", "USc6cf2d8e796cb6/design/2025-10-28_1368592091f4b.png"],
  [("u", "Hombre de jengibre flexible", "", 6.64, 90, 0)], None),
 ("1993434", "Cuenta Regresiva Estrellada", "⭐ Cuenta regresiva", "Una tira con los números del 1 al 24 y una estrellita que avanza cada día hasta Navidad.",
  ["Mueve la estrella un lugar cada día de diciembre.", "Con arbolito al final del camino.", "Diseño sencillo y elegante."],
  ["USd05b0f73f61365/design/2025-11-13_7fe437d7d8f91.jpeg", "USd05b0f73f61365/design/2025-11-13_74eb9e56280ad.jpeg"],
  [("u", "Cuenta regresiva", "", 1.9, 50, 0)], None),
 ("1996511", "Foquito Navideño con Nombre", "🎁 Personalizado", "Un foquito de colores con el nombre que tú quieras. Para el árbol, como etiqueta de regalo o llavero.",
  ["Nombre en relieve.", "Sirve como adorno, etiqueta o llavero.", "Varios colores para toda la familia."],
  ["US24c696b4e6dc33/design/2025-11-14_ce398ee5bddbe8.png", "US24c696b4e6dc33/design/2025-11-14_13657fb3a857a8.png"],
  [("a", "Nombre sencillo", "", 0.58, 16, 0), ("b", "Nombre con efecto de sombra", "", 0.75, 17, 0)],
  {"label": "Nombre", "ph": "Ej. Valentina", "max": 12}),
 ("2000058", "Cuenta Regresiva Casita de Jengibre", "⭐ Cuenta regresiva", "Una casita de jengibre con calendario: cambia los números cada día y cuenta los días para Navidad.",
  ["Números intercambiables.", "Techo nevado y detalles de dulce.", "Para repisa, mesa o recámara de los niños."],
  ["US840511436be8d9/design/2025-11-15_aef822da13a27.jpeg", "US840511436be8d9/design/2025-11-15_d9a8b906f25dc.jpeg"],
  [("a", "Clásica", "", 6.64, 212, 0), ("b", "Multicolor premium", "Más detalle de color", 21.08, 462, 0)], None),
 ("2027611", "Letreros de Calle Navideños", "🎄 Decoración", "Un set de letreros tipo calle con nombres navideños, como en los mercaditos de Navidad.",
  ["Set de varios letreros.", "Con orificios para colgarlos o clavarlos.", "Para casa o jardín."],
  ["US8398591f161690/design/2025-11-22_29651ff52d6b88.jpg", "US8398591f161690/design/2025-11-22_197c31e86b96b8.jpg"],
  [("u", "Set de letreros", "", 3.71, 125, 0)], None),
 ("2047031", "Adorno Cámara del Polo Norte", "🎅 Para la magia", "Una mini cámara de seguridad con gorro de Santa que \"vigila\" quién se porta bien. Para el árbol o una repisa.",
  ["Con gorrito de Santa.", "Para colgar en el árbol o poner en un estante.", "Perfecta para las escenas del duende navideño."],
  ["USb0158389fa401d/design/2025-11-26_c6bfc0933b7348.jpeg", "USb0158389fa401d/design/2025-11-26_48f86ac0fe1bd.jpeg"],
  [("u", "Cámara del Polo Norte", "", 4.14, 104, 0)], None),
 ("2052441", "Gato Navideño de Jengibre", "🎲 Juego", "El clásico juego de gato (tic-tac-toe) en versión navideña: tablero de casita de jengibre y fichas de bastones y galletas.",
  ["Fichas de bastón de caramelo y de galleta.", "Imanes que mantienen las fichas en su lugar.", "Para jugar en familia en las posadas."],
  ["US29a4c6f9b1a2d/design/2025-11-28_f1e1c3075d08c.jpg", "US29a4c6f9b1a2d/design/2025-11-28_8651009527b5b8.jpg"],
  [("u", "Juego completo", "", 4.09, 114, 0)], None),
 ("2057491", "Reno con Inicial y Nombre", "🎁 Personalizado", "Un renito con la inicial y el nombre que elijas. Un detalle perfecto para cada niño de la casa.",
  ["Inicial grande y nombre.", "Para colgar en el árbol.", "Ideal para regalo de intercambio."],
  ["US7e51b3ea62710a/design/2025-11-29_59f16cf901dda8.jpg", "US7e51b3ea62710a/design/2025-11-29_8b10e6c1271b8.jpg"],
  [("u", "Reno con nombre", "", 1.95, 43, 0)],
  {"label": "Nombre", "ph": "Ej. Mateo", "max": 10}),
 ("2070704", "Pueblito Navideño de Jengibre", "🏠 Decoración", "Cuatro casitas estilo jengibre con glaseado blanco. Ponle una lucecita atrás y se ilumina por las ventanas.",
  ["Set de 4 piezas.", "Detalles de nieve y glaseado.", "Se ve precioso con luz detrás."],
  ["UScdb32891953d6b/design/2025-12-02_482c8d43b7c94.jpg", "UScdb32891953d6b/design/2025-12-02_3ee904bf042fe8.jpg"],
  [("u", "Set de 4 casitas", "", 6.13, 122, 0)], None),
 ("2073409", "Bandeja de Botanas para Santa", "🥛 Para Santa", "La charolita para dejarle a Santa sus galletas y su leche en Nochebuena.",
  ["Espacios marcados para las galletas y la leche.", "Con letras de Santa.", "Una tradición para repetir cada año."],
  ["US3fe224c6f79bac/design/2025-12-03_450a1e89021698.jpg", "US3fe224c6f79bac/design/2025-12-03_5c8168508fc93.jpg"],
  [("u", "Bandeja", "", 2.75, 119, 0)], None),
 ("2078410", "Esfera Gigante Iluminada", "✨ Gran formato", "Una esfera navideña gigante que se ilumina por dentro. Luce de día y de noche, dentro o fuera de casa.",
  ["Tamaño gigante: es el centro de atención.", "Diseñada para iluminarse por dentro.", "No incluye el cable con foco; pregúntanos por WhatsApp."],
  ["US7a8606324ee066/design/2025-12-04_393f58689fa1c8.jpeg", "US7a8606324ee066/design/2025-12-04_36c1fa422d011.jpeg"],
  [("u", "Esfera gigante (sin luz)", "", 27.98, 661, 0)], None),
 ("2083881", "Globo de Nieve de Jengibre con Nombres", "🎁 Personalizado", "Una esfera tipo globo de nieve con galletitas de jengibre y los nombres de tu familia.",
  ["Lleva el apellido y los nombres de la familia.", "Para colgar en el árbol.", "Un recuerdo para cada Navidad."],
  ["USd0533a5916ad32/design/2025-12-07_e6ec323ac5a3c.jpg", "USd0533a5916ad32/design/2025-12-06_bc6bc41eb1ad2.jpg"],
  [("u", "Globo de nieve familiar", "", 3.14, 69, 0)],
  {"label": "Apellido y nombres", "ph": "Ej. Familia López: Ana, Luis, Sofía", "max": 70}),
 ("2087313", "Pueblito de Jengibre para Armar", "✉️ Tarjeta", "Una tarjeta con las piezas de un pueblito de jengibre listas para desprender y armar. Un detalle original para regalar.",
  ["Las piezas se desprenden y se arman.", "Con o sin marco.", "Perfecta como tarjeta de Navidad."],
  ["USf75902674a33b2/design/2025-12-07_1026252695f36.jpg", "USf75902674a33b2/design/2025-12-07_83216c0b0273f8.jpg"],
  [("a", "Con marco", "", 1.51, 30, 0), ("b", "Sin marco", "", 1.23, 25, 0)], None),
 ("2101416", "Porta Papel de Baño Ho-Ho-Ho", "🧻 Para el baño", "Un porta rollos navideño con las letras HO HO HO. Hasta el baño se pone en modo Navidad.",
  ["Guarda los rollos de papel de baño.", "Elige de 1 a 3 niveles.", "Firme y fácil de limpiar."],
  ["USbf9b5aa3d0fd0d/design/2025-12-10_a494d86d1dd2e8.png", "USbf9b5aa3d0fd0d/design/2025-12-10_6baf72a097c8e8.jpg"],
  [("a", "1 nivel", "HO", 7.28, 257, 0), ("b", "2 niveles", "HO HO", 13.48, 483, 0), ("c", "3 niveles", "HO HO HO", 19.61, 712, 0)], None),
 ("2109874", "Galleta de Jengibre con Nombre", "🎁 Personalizado", "Un adorno de galleta de jengibre con el nombre de quien tú quieras.",
  ["Nombre en relieve.", "Para el árbol o como etiqueta de regalo.", "Un detalle para cada invitado."],
  ["USf3320125cc8cf5/design/2025-12-13_5bd7669a3150e.jpg", "USf3320125cc8cf5/design/2025-12-13_4fde47af3b1aa.jpg"],
  [("u", "Galleta con nombre", "", 2.65, 53, 0)],
  {"label": "Nombre", "ph": "Ej. Camila", "max": 10}),
 ("2128543", "Adorno Estrella con tu Foto", "📸 Con tu foto", "Una estrella brillante que enmarca tu foto favorita para colgar en el árbol.",
  ["Va con tu foto: mándanosla por WhatsApp después de tu pedido.", "Acabado brillante tipo dorado.", "Incluye listón para colgar."],
  ["US5cf8191d8344f3/design/2025-12-17_a276a4543318c8.png", "US5cf8191d8344f3/design/2025-12-17_9200abdea6595.png"],
  [("u", "Estrella con foto", "Mándanos tu foto por WhatsApp", 0.32, 7, FOTO)], None),
 ("3175033", "Cascanueces Decorativo", "🎄 Decoración", "El clásico soldadito cascanueces en un estilo moderno de un solo color.",
  ["Elegante para repisa o mesa.", "Combina con decoración minimalista.", "Ligero y resistente."],
  ["US5a9c8ec5102a4a/design/a39f594ee5ccd690.png", "US5a9c8ec5102a4a/design/ccab4d303478ac29.jpg"],
  [("u", "Cascanueces", "", 1.52, 19, 0)], None),
 ("3176140", "Arbolitos Japandi (set de 2)", "🌲 Minimalista", "Dos arbolitos de diseño moderno con líneas suaves, en dos tamaños. Para una Navidad elegante y minimalista.",
  ["Set de 2 tamaños.", "Para repisa, mesa, chimenea o ventana.", "Estilo nórdico-japonés."],
  ["USe2c2ad920a85f/design/82598bd2d40761ba.png", "USe2c2ad920a85f/design/f8dec2b23123cfae.png"],
  [("u", "Set de 2 arbolitos", "", 4.35, 59, 0)], None),
 ("3337730", "Reno Estilo Tejido", "🦌 Decoración", "Un renito con textura de tejido a gancho. Se ve hecho a mano y le da un toque acogedor a tu casa.",
  ["Textura que parece tejida.", "Elige tamaño o la pareja.", "Para repisa, mesa o centro de mesa."],
  ["USb811a8f846c088/design/783c5450daf345dc.jpg", "USb811a8f846c088/design/5fea1ded5fb79145.jpg"],
  [("a", "Chico (11 cm)", "", 3.07, 39, 0), ("b", "Grande (12.5 cm)", "", 3.87, 53, 0), ("c", "Pareja (chico y grande)", "", 8.8, 96, 0)], None),
 ("3338545", "Árbol Espiral Minimalista", "🌲 Minimalista", "Un arbolito en espiral con textura que proyecta sombras preciosas. Moderno y elegante.",
  ["Forma de espiral con estrella.", "Uno solo o set de 3 tamaños.", "Para decoración nórdica o minimalista."],
  ["USe11a183eb1e66c/design/ecf8cf92cb6b63fa.png", "USe11a183eb1e66c/design/d2a419d12fba15e8.jpg"],
  [("a", "Un árbol", "", 2.04, 40, 0), ("b", "Set de 3 tamaños", "", 4.45, 72, 0)], None),
 ("3348753", "Bandeja de Galletas para Santa", "🥛 Para Santa", "\"Querido Santa\": la charola con lugar para la galleta, la leche y la zanahoria del reno.",
  ["Espacios para galleta, leche y zanahoria.", "Orilla ondulada y detalles en rojo.", "Para la noche del 24."],
  ["USc8d881c97f1b64/design/a866a6dab7b08bc6.png", "USc8d881c97f1b64/design/a3b4716c6dc30025.png"],
  [("u", "Bandeja", "", 3.85, 134, 0)], None),
 ("3355184", "Esfera Muñeco de Nieve con Nombre", "🎁 Personalizado", "Una esfera con muñeco de nieve, copos y arbolitos, y el nombre que elijas al centro.",
  ["Nombre grande al centro.", "Colores rojo, verde y blanco.", "Para colgar en el árbol."],
  ["US48fa87708a0023/design/90bd0438157c84df.jpg", "US48fa87708a0023/design/2e7d949031106474.jpg"],
  [("u", "Esfera con nombre", "", 1.14, 30, 0)],
  {"label": "Nombre", "ph": "Ej. Nicole", "max": 10}),
 ("3371427", "Árbol de Cuerda Trenzada", "🌲 Minimalista", "Un arbolito con una cuerda esculpida que lo envuelve y una estrella arriba. Se ve hecho a mano.",
  ["Detalle de cuerda trenzada.", "Estrella en la punta.", "Para repisa o mesa."],
  ["US5b4a0cf914e933/design/5118d05dd1556803.jpg", "US5b4a0cf914e933/design/a6fba2e468d2d141.jpg"],
  [("u", "Árbol de cuerda", "", 2.96, 56, 0)], None),
 ("3373774", "Marco de Foto Reno de Nariz Roja", "📸 Con tu foto", "Un renito de nariz roja que enmarca tu foto para colgar en el árbol.",
  ["Va con tu foto: mándanosla por WhatsApp después de tu pedido.", "Nariz roja en relieve.", "Incluye listón para colgar."],
  ["US57c20a2b0c71c/design/75969e0a59301fc7.jpg", "US57c20a2b0c71c/design/d5c567c5b268410e.png"],
  [("u", "Marco con foto", "Mándanos tu foto por WhatsApp", 0.62, 10, FOTO)], None),
 ("3394419", "Suéter Navideño con Nombre", "🎁 Personalizado", "Un adorno con forma de suéter navideño y el nombre que tú quieras.",
  ["Nombre al centro del suéter.", "Para el árbol o como etiqueta de regalo.", "Divertido para toda la familia."],
  ["USf1b71cb7199f2c/design/791deb16919bcfc0.jpeg", "USf1b71cb7199f2c/design/7592d319314e6c86.jpeg"],
  [("u", "Suéter con nombre", "", 0.94, 16, 0)],
  {"label": "Nombre", "ph": "Ej. Daniel", "max": 10}),
 ("3397234", "Bandejas Bastón de Caramelo", "🍬 Para la mesa", "Un bastón de caramelo gigante que se separa en charolitas para botanas, dulces o galletas.",
  ["Módulos que se juntan en forma de bastón.", "Para botanas, dulces o galletas.", "Para tus posadas y cenas."],
  ["US4dd15aa2752a26/design/e047c3c8c7aafa15.jpeg", "US4dd15aa2752a26/design/5d892dfb561a4d78.jpeg"],
  [("u", "Set de bandejas", "", 5.69, 265, 0)], None),
 ("3407142", "Porta Rollos de Cocina Gorro de Santa", "🍪 Para la cocina", "Un porta rollos de papel de cocina con forma de gorro de Santa. Lo de diario, en modo Navidad.",
  ["Gorro rojo con orilla blanca texturizada y pompón.", "Para rollos de papel de cocina.", "Firme y estable sobre la barra."],
  ["US38908b1488b29c/design/7b8f7032a54d8e5d.png", "US38908b1488b29c/design/d4cd2d3b42539374.png"],
  [("u", "Porta rollos", "", 8.19, 480, 0)], None),
 ("3412717", "Corona con Reno y Letrero", "🎁 Personalizado", "Una corona navideña con renito, moño, piñas, hojas y un letrero con el texto que tú quieras.",
  ["Letrero con tu texto (ej. Feliz Navidad o tu apellido).", "Detalles de moño, piñas y acebo.", "Para puerta o pared."],
  ["US95b1cf38e7a98/design/e3d2864b746f126d.png", "US95b1cf38e7a98/design/d9f97595d065d0dc.png"],
  [("u", "Corona con letrero", "", 9.86, 181, 0)],
  {"label": "Texto del letrero", "ph": "Ej. Familia Pérez", "max": 20}),
 ("3420091", "Caseta Cámara de Santa", "🎅 Para la magia", "Una casetita con cámara y gorro de Santa que vigila quién se porta bien. Para escenas del duende o repisa.",
  ["Con gorrito de Santa y letrero SANTA CAM.", "Se para sola.", "Colores rojo, verde y blanco."],
  ["USce19a6c44403ff/design/ff4c786ec057ba3e.png", "USce19a6c44403ff/design/e1ac848cf8d1ef82.jpeg"],
  [("u", "Caseta Santa Cam", "", 1.06, 33, 0)], None),
 ("3430824", "Corona de Acebo con tu Apellido", "🎁 Personalizado", "Una corona de acebo con moño, moritas y un listón con el apellido de tu familia. Para dar la bienvenida en tu puerta.",
  ["Lleva el apellido de tu familia.", "Hojas de acebo, moritas y moño.", "Un solo color o a 4 colores."],
  ["US35e54453a34f1b/design/b1bbae716ac2de91.png", "US35e54453a34f1b/design/bd95548cd849e2b7.png"],
  [("a", "Un solo color", "", 2.08, 40, 0), ("b", "4 colores", "", 3.67, 70, 0)],
  {"label": "Apellido", "ph": "Ej. Rossi", "max": 12}),
 ("3471108", "Broche de Acebo para Chongo", "🎀 Accesorio", "Una coronita de acebo con su palito con estrella para sujetar el chongo. El peinado más navideño.",
  ["Corona de acebo con moritas.", "Palito con estrella.", "Para posadas y fiestas."],
  ["USb7e20bd848011e/design/b92e7113617a4e4c.png", "USb7e20bd848011e/design/5bc5758394cdaa04.jpeg"],
  [("u", "Broche y palito", "", 2.32, 28, 0)], None),
 ("3485874", "Casita Navideña con tu Apellido", "🎁 Personalizado", "Una casita navideña con techo nevado, coronita, puerta roja, arbolitos y el apellido de tu familia.",
  ["Lleva el apellido de tu familia.", "Se para sola: para repisa o mesa.", "Detalles de nieve, ventanas y arbolitos."],
  ["USa6c3046be13b15/design/1281c9e18ecff55d.jfif", "USa6c3046be13b15/design/9ba98520e5713930.jfif"],
  [("u", "Casita familiar", "", 19.84, 536, 0)],
  {"label": "Apellido de la familia", "ph": "Ej. Familia Hernández", "max": 22}),
 ("3500990", "Porta Panetón Reno", "🎁 Para regalar", "Convierte un panetón en un regalo encantador con este porta panetón de reno.",
  ["Para panetón tradicional.", "Con cara de reno y astas.", "No incluye el panetón."],
  ["US5f744af03bb00b/design/20c1eb396c3cb2ce.jpeg", "US5f744af03bb00b/design/68727216d4397c49.jpeg"],
  [("u", "Porta panetón reno", "", 7.79, 230, 0)], None),
 ("3523645", "Porta Mini Panetón Santa", "🎁 Para regalar", "Un porta mini panetón con el traje de Santa: cinturón negro, hebilla dorada y orilla blanca.",
  ["Para mini panetón.", "Traje de Santa con hebilla dorada.", "No incluye el panetón."],
  ["US7fbdc0502b85a4/design/456ee765ed7e39aa.jpeg", "US7fbdc0502b85a4/design/ab75324c6cd78d42.jpeg"],
  [("u", "Porta mini panetón", "", 4.43, 110, 0)], None),
 ("3531613", "Porta Panetón Duende", "🎁 Para regalar", "Un porta panetón con el traje del duende navideño: verde, rojo y hebilla dorada.",
  ["Dos tamaños: panetón tradicional o mini.", "Traje de duende con hebilla dorada.", "No incluye el panetón."],
  ["US6653332aef5ed9/design/1e6c1a412779c5c9.png", "US6653332aef5ed9/design/c418530ee1728ff7.jpeg"],
  [("a", "Panetón tradicional (500 g)", "15.6 × 10 cm", 6.66, 206, 0), ("b", "Mini panetón", "9 × 6 cm", 2.89, 72, 0)], None),
 ("3533521", "Bota Navideña con Nombre", "🎁 Personalizado", "Un adorno de bota navideña con el nombre que elijas. Uno para cada integrante de la familia.",
  ["Nombre grande en la bota.", "Moño y copo de nieve.", "Para el árbol o como etiqueta de regalo."],
  ["USe32837fe204709/design/a8ba757367d594a7.png", "USe32837fe204709/design/b4db5a5c3000e4ed.png"],
  [("u", "Bota con nombre", "", 0.71, 20, 0)],
  {"label": "Nombre", "ph": "Ej. Emma", "max": 10}),
 ("3536610", "Cuenta Regresiva del Reno", "⭐ Cuenta regresiva", "Un renito asomado sobre un letrero con cubos de números para contar los días que faltan para Navidad.",
  ["Cubos de números intercambiables.", "Reno con nariz roja.", "Para repisa o mesa."],
  ["USac916bd566b7dc/design/f56fc8a56e67cdfe.jfif", "USac916bd566b7dc/design/893c17366dc08733.jfif"],
  [("u", "Cuenta regresiva", "", 12.36, 366, 0)], None),
]

PROPIOS = ["Santa", "Ho-Ho-Ho", "Japandi", "Polo Norte", "Jo, Jo, Jo"]


def oracion(t):
    """Primera letra en mayúscula y el resto en minúscula, respetando nombres propios (estilo de la tienda)."""
    s = t[0] + t[1:].lower()
    for n in PROPIOS:
        s = s.replace(n.lower(), n)
    return s


def sin_emoji(t):
    return "".join(ch for ch in t if ord(ch) < 0x2600).strip()


# ---------- Construcción: productos sueltos + grupos (cosas iguales = un producto con versiones) ----------
SRC = {}
for mid, nombre, badge, lead, bullets, fotos, ops, personal in P:
    opciones = [{"k": k, "label": label, "sub": sub, "precio": precio(h, g, extra), "costo": costo(h, g, extra),
                 "horas": h, "gramos": g, "mw": mid} for k, label, sub, h, g, extra in ops]
    SRC[mid] = {"id": "NV" + mid, "mw": mid, "nombre": oracion(nombre), "badge": sin_emoji(badge), "lead": lead,
                "bullets": bullets, "fotos": [CDN + f + "?x-oss-process=image/resize,w_900" for f in fotos],
                "opciones": opciones, "personal": personal}

# Adorno corona con foto (antes era un producto aparte en la página; foto propia de Lilian)
CORONA = [{"k": "corona", "label": "Corona", "sub": "Con 1 foto", "precio": 59, "costo": costo(0.34, 7, FOTO), "horas": 0.34, "gramos": 7, "mw": "2128558"},
          {"k": "corona3", "label": "Corona, paquete de 3", "sub": "Con 3 fotos distintas · ahorras $18", "precio": 159, "costo": costo(1.02, 21, 3 * FOTO), "horas": 1.02, "gramos": 21, "mw": "2128558"}]

GRUPOS = [
 ("bandeja-santa", "Bandeja para Santa", "Para Santa",
  "La charolita para dejarle a Santa sus galletas y su leche en Nochebuena. Elige tu modelo.",
  ["Dos modelos: botanas para Santa o \"Querido Santa\" con lugar para la zanahoria del reno.", "Espacios marcados para galletas y leche.", "Una tradición para repetir cada año."],
  [("2073409", "Botanas para Santa"), ("3348753", "Querido Santa, con zanahoria para el reno")], None),
 ("camara-santa", "Cámara de Santa", "Para la magia",
  "Una cámara de vigilancia de mentira que \"transmite al Polo Norte\" para que los niños se porten bien. Elige tu modelo.",
  ["Domo: 8 cm, se cuelga en la pared.", "Caseta: con gorro de Santa, se para sola.", "Adorno: con gorrito, para el árbol o una repisa."],
  [("797351", "Domo de pared"), ("3420091", "Caseta con gorro"), ("2047031", "Adorno para el árbol")], None),
 ("cuenta-regresiva", "Cuenta regresiva navideña", "Cuenta regresiva",
  "Cuenten juntos los días que faltan para Navidad. Elige el modelo que más te guste.",
  ["Estrellada: una estrellita avanza del 1 al 24.", "Casita de jengibre: números intercambiables.", "Reno: cubos de números con nariz roja."],
  [("1993434", "Estrellada"), ("2000058", "Casita de jengibre"), ("3536610", "Reno con cubos")], None),
 ("porta-paneton", "Porta panetón", "Para regalar",
  "Convierte un panetón en un regalo encantador. Elige personaje y tamaño.",
  ["Reno, duende o Santa.", "Para panetón tradicional (500 g) o mini.", "No incluye el panetón."],
  [("3500990", "Reno · tradicional"), ("3531613", "Duende"), ("3523645", "Santa · mini")], None),
 ("arbolitos", "Arbolitos de diseño", "Minimalista",
  "Arbolitos modernos para una Navidad elegante: en repisa, mesa, chimenea o ventana. Elige tu estilo.",
  ["Japandi: set de 2 tamaños con líneas suaves.", "Espiral: con estrella, uno o set de 3 tamaños.", "Cuerda trenzada: se ve hecho a mano."],
  [("3176140", "Japandi"), ("3338545", "Espiral"), ("3371427", "Cuerda trenzada")], None),
 ("adorno-foto", "Adorno con tu foto", "Con tu foto",
  "Un adorno para el árbol que enmarca tu foto favorita. El regalo perfecto para abuelos, padrinos y maestras.",
  ["Va con tu foto: mándanosla por WhatsApp después de tu pedido.", "Elige corona, estrella o reno de nariz roja.", "Paquete de 3: combina los modelos que quieras y ahorra $18.", "Incluye listón para colgar."],
  [("CORONA", "Corona"), ("2128543", "Estrella"), ("3373774", "Reno de nariz roja")], None),
 ("adorno-nombre", "Adorno con nombre", "Personalizado",
  "Un adorno con el nombre que tú quieras: uno para cada integrante de la familia o como etiqueta de regalo.",
  ["Elige el modelo: bota, esfera, galleta, suéter, foquito o reno.", "Nombre en relieve.", "Para el árbol, como etiqueta de regalo o llavero."],
  [("3533521", "Bota"), ("3355184", "Esfera muñeco de nieve"), ("2109874", "Galleta de jengibre"), ("3394419", "Suéter navideño"), ("1996511", "Foquito"), ("2057491", "Reno con inicial")],
  {"label": "Nombre", "ph": "Ej. Valentina", "max": 12}),
 ("corona-texto", "Corona personalizada", "Personalizado",
  "Una corona navideña para tu puerta o pared con el apellido de tu familia o el texto que quieras.",
  ["Acebo: con moño, moritas y listón con tu apellido.", "Reno: con moño, piñas y letrero con tu texto.", "Para dar la bienvenida en tu puerta."],
  [("3430824", "Acebo"), ("3412717", "Reno con letrero")],
  {"label": "Apellido o texto del letrero", "ph": "Ej. Familia Pérez", "max": 20}),
]

usados = set()
grupos = {}
for gid, nombre, badge, lead, bullets, partes, personal in GRUPOS:
    ops, fotos = [], []
    for mid, etiqueta in partes:
        if mid == "CORONA":
            fotos.append("../img/navidad/corona-foto.jpg")
            for o in CORONA[:1]:
                ops.append(dict(o, k="corona" + o["k"][6:] if False else o["k"], f=len(fotos) - 1))
            continue
        src = SRC[mid]; usados.add(mid)
        fotos.append(src["fotos"][0])
        for o in src["opciones"]:
            label = etiqueta if len(src["opciones"]) == 1 else f"{etiqueta} · {o['label'][0].lower() + o['label'][1:]}"
            ops.append(dict(o, k=f"{mid}{o['k']}", label=label, f=len(fotos) - 1))
    nota = "mándanos la foto por WhatsApp" if gid == "adorno-foto" else ""
    paquete = {"n": 3, "ahorro": 18} if gid == "adorno-foto" else None
    grupos[gid] = {"paquete": paquete, "nota": nota, "id": "NVG-" + gid, "mw": ",".join(m for m, _ in partes), "nombre": nombre, "badge": badge, "lead": lead,
                   "bullets": bullets, "fotos": fotos, "opciones": ops, "personal": personal}

# Orden de la rejilla
ORDEN = ["G:adorno-nombre", "G:adorno-foto", "3485874", "G:corona-texto", "817845", "2083881",
         "G:cuenta-regresiva", "G:bandeja-santa", "G:camara-santa", "G:porta-paneton", "G:arbolitos",
         "14093", "2070704", "2087313", "2027611", "3175033", "3337730", "3397234", "3407142", "2101416",
         "2052441", "1935739", "3471108", "2078410"]
# Mismo precio para variantes parecidas (Lilian: "cuando se pueda que todos tengan el mismo precio").
# Se sube al más alto para no quedar abajo de la regla; tamaños, niveles y modelos muy distintos se quedan.
IGUALAR = {
 "NVG-adorno-foto": {"Corona": 59, "Estrella": 59, "Reno de nariz roja": 59},
 "NVG-adorno-nombre": {"Bota": 59, "Esfera muñeco de nieve": 59, "Suéter navideño": 59, "Foquito · nombre sencillo": 59,
                       "Foquito · nombre con efecto de sombra": 59, "Reno con inicial": 99, "Galleta de jengibre": 99},
 "NVG-bandeja-santa": {"Botanas para Santa": 159},
 "NVG-camara-santa": {"Domo de pared": 149},
 "NVG-porta-paneton": {"Duende · panetón tradicional (500 g)": 269},
 "NVG-arbolitos": {"Japandi": 139, "Cuerda trenzada": 139},
}
for d in list(grupos.values()) + list(SRC.values()):
    for o in d["opciones"]:
        nuevo = IGUALAR.get(d["id"], {}).get(o["label"])
        if nuevo: assert nuevo >= o["precio"], (d["id"], o["label"]); o["precio"] = nuevo

out = []
for x in ORDEN:
    out.append(grupos[x[2:]] if x.startswith("G:") else SRC[x])
faltan = [m for m in SRC if m not in usados and m not in ORDEN]
assert not faltan, faltan

js = "// Generado con tools/navidad_productos.py — no editar a mano.\nwindow.NAVIDAD = " + json.dumps(out, ensure_ascii=False, indent=1) + ";\n"
open("assets/navidad-productos.js", "w", encoding="utf-8").write(js)
json.dump(out, open("tools/navidad_productos.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "productos")
for p in out:
    print(p["id"], p["nombre"], [(o["label"], o["precio"]) for o in p["opciones"]])
