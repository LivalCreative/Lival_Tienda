// Detalles compartidos de la tienda (no toca precios ni pedidos):
// número del carrito en la barra, logo de la barra en el inicio, entradas suaves, nieve, cuenta regresiva y fotos protegidas.
(function () {
  document.documentElement.classList.add("js");
  const quieto = matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Cuántos productos hay en el carrito compartido (assets/carrito.js)
  function contar() {
    if (!window.LIVAL) return;
    const c = LIVAL.leer();
    const n = Object.values(c).reduce((s, x) => s + (x > 0 ? x : 0), 0);
    document.querySelectorAll("[data-carrito-n]").forEach(el => { el.textContent = n; });
  }
  contar();
  document.addEventListener("click", () => setTimeout(contar, 0));
  window.addEventListener("pageshow", contar);
  window.addEventListener("storage", contar);

  // Cuenta regresiva al 1 de diciembre
  const hoy = new Date(); hoy.setHours(0, 0, 0, 0);
  let meta = new Date(hoy.getFullYear(), 11, 1);
  if (hoy > new Date(hoy.getFullYear(), 11, 24)) meta = new Date(hoy.getFullYear() + 1, 11, 1);
  const d = Math.round((meta - hoy) / 864e5);
  document.querySelectorAll("[data-dias]").forEach(el => { el.textContent = d <= 0 ? "¡Ya!" : d; });
  document.querySelectorAll("[data-dias-txt]").forEach(el => {
    el.textContent = d <= 0 ? "Ya empezaron las travesuras" : d === 1 ? "día para el 1 de diciembre" : "días para el 1 de diciembre";
  });

  // Fotos: no se arrastran ni se guardan con clic derecho o pulsación larga
  document.addEventListener("contextmenu", e => { if (e.target.tagName === "IMG") e.preventDefault(); });
  document.addEventListener("dragstart", e => { if (e.target.tagName === "IMG") e.preventDefault(); });

  // Letrero en vivo del inicio: el texto viaja a la chimenea en Navidad
  const campo = document.getElementById("apellido");
  if (campo) {
    const salida = document.querySelectorAll("[data-letrero]"), pedir = document.getElementById("pedirChimenea");
    // Achica la letra si el texto no cabe entre las estrellas del letrero
    const ajusta = () => salida.forEach(s => {
      s.style.fontSize = "";
      const k = s.clientWidth / s.scrollWidth;
      if (k < 1) s.style.fontSize = parseFloat(getComputedStyle(s).fontSize) * k * 0.97 + "px";
    });
    if ("ResizeObserver" in window) new ResizeObserver(ajusta).observe(salida[0].parentElement);
    const pinta = () => {
      const v = campo.value.trim().slice(0, 22);
      salida.forEach(s => { s.textContent = v || "Familia López"; });
      ajusta();
      if (pedir) pedir.href = "navidad/" + (v ? "?letrero=" + encodeURIComponent(v) : "") + "#chimenea";
    };
    campo.addEventListener("input", pinta); pinta();
  }

  // En el inicio el logo de la barra aparece cuando el logo grande sale de la pantalla
  const grande = document.querySelector("[data-logo-grande]"), chico = document.querySelector("[data-logo-chico]");
  if (grande && chico && "IntersectionObserver" in window) {
    chico.classList.add("oculto");
    new IntersectionObserver(([e]) => chico.classList.toggle("oculto", e.isIntersecting)).observe(grande);
  }

  // Entradas suaves, una vez por bloque, escalonadas
  const io = "IntersectionObserver" in window && !quieto ? new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add("visto"); io.unobserve(e.target); }
  }), { rootMargin: "0px 0px -8% 0px" }) : null;
  document.querySelectorAll("[data-entra]").forEach(el => {
    [...el.children].forEach((c, i) => c.style.setProperty("--i", i));
    io ? io.observe(el) : el.classList.add("visto");
  });

  // Nieve
  if (!quieto) document.querySelectorAll(".nieve").forEach(n => {
    n.innerHTML = Array.from({ length: 28 }, () => {
      const z = 2 + Math.random() * 4;
      return `<i style="left:${Math.random() * 100}%;width:${z}px;height:${z}px;--dx:${(Math.random() * 40 - 20) | 0}px;animation-duration:${7 + Math.random() * 9}s;animation-delay:-${Math.random() * 14}s"></i>`;
    }).join("");
  });
})();
