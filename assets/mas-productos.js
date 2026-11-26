// Productos de "Más productos" (todo el año). Mismo formato que assets/navidad-productos.js.
// Se suman a window.NAVIDAD para que el carrito (carrito.js) y el pedido los conozcan; cárgalo ANTES de carrito.js.
// En productos/ se dibujan con navidad-render.js; en Navidad no se carga este archivo.
window.MAS = [
 {
  "id": "MP1709436",
  "mw": "1709436",
  "nombre": "Joyero lata de sardinas",
  "badge": "Regalo",
  "lead": "Una lata de sardinas que en vez de sardinas guarda tus aretes, anillos y collares. La tapa se desliza para abrir y tiene su anillita como lata de verdad.",
  "bullets": ["Tapa deslizable con anillita.", "Para aretes, anillos, collares o cositas chiquitas.", "Ideal para regalar o para llevar en la bolsa de viaje."],
  "fotos": ["../img/mas/joyero-sardinas.jpg", "../img/mas/joyero-sardinas-abierto.jpg"],
  "opciones": [{"k": "u", "label": "Joyero", "precio": 130, "horas": 3.5, "gramos": 66, "mw": "1709436", "f": 0}],
  "personal": null,
  "cat": "regalo"
 }
];
window.NAVIDAD = (window.NAVIDAD || []).concat(window.MAS);
