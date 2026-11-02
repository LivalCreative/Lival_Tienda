# Tienda Lival Creative Studio

Sitio estático publicado con GitHub Pages: https://villamichel.github.io/Lival_Tienda/
Todo en español (México). La dueña es Lilian; los clientes compran desde el celular.

## Estructura
- `index.html` — inicio con las secciones (estilo Lival: lavanda y durazno, `assets/lival.css`).
- `duende/index.html` — sección especial Travesuras del Duende (verde pino y rojo). Contiene el catálogo, el carrito y el formulario de pedido.
  **En pausa:** la página manda al inicio (bloque `DUENDE-PAUSA` en su `<head>`), su enlace está comentado en la barra de cada página y la banda del inicio está guardada en `<template id="duende-en-pausa">`. Para reactivarla: borra el bloque, descomenta los enlaces, saca la banda del `<template>` y corre `build_pedido.py`.
- `pedido/index.html` — checkout compartido. **No se edita a mano**: se genera con `python3 tools/build_pedido.py` a partir de `duende/index.html`. Córrelo después de cada cambio al duende.
- `navidad/index.html` — productos navideños en rejilla (3 por fila en computadora, 2 en celular); cada tarjeta se abre en vista completa.
- `productos/index.html` — "Más productos" (muy pronto).
- `assets/carrito.js` — carrito compartido (localStorage), precios y horas de los productos fuera del duende, productos personalizados (chimenea).
- `assets/tienda.js` — detalles compartidos de la vista (número del carrito en la barra, animaciones, nieve, cuenta regresiva, fotos protegidas). No toca precios ni pedidos.
- Estilo "Taller de regalos": `assets/lival.css` (lavanda y durazno, letra Bricolage Grotesque + Nunito en `fonts/`). El duende tiene su estilo propio en verde pino, rojo y oro.
- Tema de temporada navideña: `assets/temporada.css` + clase `temporada-navidad` en `<body>` (nieve sobre la página, aldea de casitas de jengibre en los `data-aldea`, marcos de jengibre en las fotos). Para quitarlo: borra la clase, el `<link>` de `temporada.css` y los `<div data-aldea>` de cada página, ajusta `tools/build_pedido.py` y córrelo.
- `ocupacion.json` — fechas ocupadas, lo actualiza una tarea programada desde el tablero privado "Pedidos 3D". No contiene nombres ni montos; nunca agregues datos de clientes al repositorio.
- `tools/` — `ocupacion.py`, `build_pedido.py`, `horas_duende.json`.
- `img/` — fotos con marca de agua "LIVAL CREATIVE STUDIO". Toda foto nueva de producto lleva marca de agua.

## Reglas del negocio
- Pedidos por WhatsApp 442 279 1488; anticipo siempre por transferencia (BBVA, CLABE 012680004682074457, a nombre de Lilian Valladares López).
- Anticipo: 50 % redondeado a decenas; paquete de 24: $750.
- Entregas: lunes a viernes y domingo; sábados no hay. Puntos de entrega en `duende/index.html` (LUGARES). La hora se confirma por WhatsApp.
- Fechas: máximo 4 entregas por día; 16 horas de impresión = 1 día de trabajo.
- Regla de precio: (costo × 2) + $15 por hora + $30, redondeado a terminación 9, mínimo $49. Filamento $0.25/g, máquina $0.75/h.
- Decir "duende navideño", nunca la marca registrada del muñeco.
- La dueña ya tiene las licencias comerciales de los diseños que pide subir.

## Al cambiar algo
- Si cambias `assets/lival.css`, `assets/tienda.js` o `assets/carrito.js`, sube el número `?v=` con el que los cargan todas las páginas (y corre `build_pedido.py`); si no, los celulares mezclan archivos viejos del caché con los nuevos.
- Probar en un celular de 390 px de ancho (Playwright) y que no haya errores en consola.
- Mantener el carrito compartido funcionando entre Duende, Navidad y Pedido.
