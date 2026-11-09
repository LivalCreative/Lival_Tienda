# Lival Creative Studio · Tienda

Sitio público: https://livalcreative.github.io/Lival_Tienda/

Este repositorio es público y solo tiene lo que usa la tienda. Lo privado del negocio
(licencias, costos y precios con márgenes, archivos 3D, fotos originales) está en Google Drive,
en la carpeta "Catalogo Lival".

- `index.html` — inicio con las secciones.
- `navidad/` — productos navideños.
- `productos/` — más productos (muy pronto).
- `pedido/` — carrito y pedido por WhatsApp (se genera con `tools/build_pedido.py`).
- `duende/` — Travesuras del Duende (en pausa).
- `assets/` — estilos y código compartido (carrito, productos de Navidad).
- `img/` — fotos de la tienda, con marca de agua.
- `ocupacion.json` — fechas ocupadas y cupo de Navidad, generado desde el tablero Pedidos 3D con `tools/ocupacion.py`. No contiene nombres ni montos.
- `tools/` — programas para generar la tienda y la lista de fotos del catálogo de Drive.
