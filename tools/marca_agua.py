"""Pone la marca de agua de Lival a las fotos propias y las deja listas para la tienda.

Uso: python3 tools/marca_agua.py <foto_original> <salida.jpg> [--medidas]
  --medidas: el sello va arriba para no tapar el letrero de medidas de abajo.
La marca: "LIVAL CREATIVE STUDIO" en diagonal, suave, y el sello "© Lival Creative Studio".
"""
import sys
from PIL import Image, ImageDraw, ImageFont

FUENTE = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
ANCHO = 900


def marcar(src, dst, medidas=False):
    im = Image.open(src).convert("RGB")
    h = round(im.height * ANCHO / im.width)
    im = im.resize((ANCHO, h), Image.LANCZOS)
    W, H = im.size

    # Texto en diagonal repetido
    capa = Image.new("RGBA", (W * 2, H * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    f = ImageFont.truetype(FUENTE, 34)
    texto = "LIVAL CREATIVE STUDIO"
    tw = d.textlength(texto, font=f) + 90
    y, fila = 0, 0
    while y < H * 2:
        x = -(fila % 2) * tw / 2
        while x < W * 2:
            d.text((x, y), texto, font=f, fill=(255, 255, 255, 52))
            x += tw
        y += 150; fila += 1
    capa = capa.rotate(30, resample=Image.BICUBIC)
    capa = capa.crop((W // 2, H // 2, W // 2 + W, H // 2 + H))
    im = Image.alpha_composite(im.convert("RGBA"), capa)

    # Sello
    d = ImageDraw.Draw(im)
    fs = ImageFont.truetype(FUENTE, 24)
    s = "© Lival Creative Studio"
    sw = d.textlength(s, font=fs)
    pw, ph = sw + 32, 44
    x1 = W - pw - 18
    y1 = round(H * 0.11) if medidas else round(H * 0.885) - ph
    caja = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(caja).rounded_rectangle((x1, y1, x1 + pw, y1 + ph), 10, fill=(0, 0, 0, 120))
    im = Image.alpha_composite(im, caja)
    ImageDraw.Draw(im).text((x1 + 16, y1 + 8), s, font=fs, fill=(255, 255, 255, 255))
    im.convert("RGB").save(dst, "JPEG", quality=82, optimize=True, progressive=True)


if __name__ == "__main__":
    marcar(sys.argv[1], sys.argv[2], "--medidas" in sys.argv)
