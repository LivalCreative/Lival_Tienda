# Tienda Lival Creative Studio

Sitio estático publicado con GitHub Pages: https://livalcreative.github.io/Lival_Tienda/
Todo en español (México). La dueña es Lilian; los clientes compran desde el celular.

## Estructura
- `index.html` — inicio con las secciones (estilo Lival: lavanda y durazno, `assets/lival.css`).
- `duende/index.html` — sección especial Travesuras del Duende (verde pino y rojo). Contiene el catálogo, el carrito y el formulario de pedido.
  **En pausa:** la página manda al inicio (bloque `DUENDE-PAUSA` en su `<head>`), su enlace está comentado en la barra de cada página y la banda del inicio está guardada en `<template id="duende-en-pausa">`. Para reactivarla: borra el bloque, descomenta los enlaces, saca la banda del `<template>` y corre `build_pedido.py`.
- `pedido/index.html` — checkout compartido. **No se edita a mano**: se genera con `python3 tools/build_pedido.py` a partir de `duende/index.html`. Córrelo después de cada cambio al duende.
- `disfraces/index.html` — "Disfraces para tu duende": el cliente escoge paquete (3 $180, 6 $330, 9 $465, colección completa 13 con Frosty $580) y marca los disfraces; Frosty solo va en la colección completa o aparte ($130). Datos (nombres, horas, fotos) en el script de la página. Fotos con marca de agua en `img/disfraces/`; el casco sigue con foto de MakerWorld hasta tener propia. Aviso verde arriba de todo en el inicio y en Navidad (`.aviso-dz` en lival.css), botón rojo en la portada y banda más abajo en el inicio.
- `navidad/index.html` — productos navideños en rejilla (3 por fila en computadora, 2 en celular); cada tarjeta se abre en vista completa.
- `productos/index.html` — "Más productos" (muy pronto).
- `assets/carrito.js` — carrito compartido (localStorage), precios y horas de los productos fuera del duende, productos personalizados (chimenea).
- `assets/tienda.js` — detalles compartidos de la vista (número del carrito en la barra, animaciones, nieve, cuenta regresiva, fotos protegidas). No toca precios ni pedidos.
- Estilo "Taller de regalos": `assets/lival.css` (lavanda y durazno, letra Bricolage Grotesque + Nunito en `fonts/`). El duende tiene su estilo propio en verde pino, rojo y oro.
- Tema de temporada navideña: `assets/temporada.css` + clase `temporada-navidad` en `<body>` (nieve sobre la página, aldea de casitas de jengibre en los `data-aldea`, marcos de jengibre en las fotos). Para quitarlo: borra la clase, el `<link>` de `temporada.css` y los `<div data-aldea>` de cada página, ajusta `tools/build_pedido.py` y córrelo.
- `ocupacion.json` — fechas ocupadas, lo actualiza una tarea programada desde el tablero privado "Pedidos 3D". No contiene nombres ni montos; nunca agregues datos de clientes al repositorio.
- `tools/` — `ocupacion.py`, `build_pedido.py`, `horas_duende.json`.
- Lo privado del negocio (licencias, costos y precios, archivos 3D, fotos originales) va en Google Drive, carpeta "Catalogo Lival"; este repositorio solo tiene lo que usa la tienda.
- `img/` — fotos con marca de agua "LIVAL CREATIVE STUDIO". Toda foto nueva de producto lleva marca de agua.

## Reglas del negocio
- Pedidos por WhatsApp 442 279 1488; anticipo siempre por transferencia (BBVA, CLABE 012680004682074457, a nombre de Lilian Valladares López).
- Anticipo: 50 % redondeado a decenas; paquete de 24: $750.
- Entregas: lunes a viernes y domingo; sábados no hay. Puntos de entrega en `duende/index.html` (LUGARES). La hora se confirma por WhatsApp.
- Fechas: máximo 4 entregas por día; 16 horas de impresión = 1 día de trabajo.
- Cupo de Navidad: `tools/ocupacion.py` suma las horas reales de lo pendiente en el tablero y calcula las horas libres hasta el 23 de diciembre (sin sábados, reservando 25 % o mínimo 32 h para piezas chicas). Las piezas de 8 h o más que ya no caben se marcan "Agotado" en la tienda y se quitan de los carritos (`assets/carrito.js` → `LIVAL.cerrado`). Ajustes al inicio de `ocupacion.py`.
- Precios: los pone Lilian en su lista de Google Drive (Catalogo Lival / Precios) y se pasan a `tools/precios_lilian.json`. Costos, márgenes y regla de precio son privados: viven en Drive, nunca en este repositorio (es público).
- Decir "duende navideño", nunca la marca registrada del muñeco.
- La dueña ya tiene las licencias comerciales de los diseños que pide subir.

## Al cambiar algo
- Si cambias `assets/lival.css`, `assets/tienda.js` o `assets/carrito.js`, sube el número `?v=` con el que los cargan todas las páginas (y corre `build_pedido.py`); si no, los celulares mezclan archivos viejos del caché con los nuevos.
- Probar en un celular de 390 px de ancho (Playwright) y que no haya errores en consola.
- Mantener el carrito compartido funcionando entre Duende, Navidad y Pedido.
