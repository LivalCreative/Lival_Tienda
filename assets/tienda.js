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

  // Palabra que cambia sola en la portada (Navidad, cumpleaños, tu boda…)
  document.querySelectorAll("[data-giro]").forEach(el => {
    const ps = el.dataset.giro.split("|"); let i = 0;
    if (quieto || ps.length < 2) return;
    setInterval(() => {
      el.classList.add("sale");
      setTimeout(() => {
        i = (i + 1) % ps.length; el.textContent = ps[i];
        el.classList.remove("sale"); el.classList.add("entra");
        requestAnimationFrame(() => requestAnimationFrame(() => el.classList.remove("entra")));
      }, 260);
    }, 2200);
  });

  // Fotos: no se arrastran ni se guardan con clic derecho o pulsación larga
  document.addEventListener("contextmenu", e => { if (e.target.tagName === "IMG") e.preventDefault(); });
  document.addEventListener("dragstart", e => { if (e.target.tagName === "IMG") e.preventDefault(); });

  // Letrero en vivo del inicio: el texto viaja a la chimenea en Navidad
  const campo = document.getElementById("apellido");
  if (campo) {
    const salida = document.querySelectorAll("[data-letrero]"), pedir = document.getElementById("pedirChimenea");
    const botas = [...document.querySelectorAll("[data-bota-campo]")];
    // Achica la letra si el texto no cabe en el letrero o en la etiqueta de la bota
    const ajusta = () => document.querySelectorAll("[data-ajusta]").forEach(s => {
      s.style.fontSize = "";
      const k = s.clientWidth / s.scrollWidth;
      if (k < 1) s.style.fontSize = parseFloat(getComputedStyle(s).fontSize) * k * 0.97 + "px";
    });
    if ("ResizeObserver" in window) new ResizeObserver(ajusta).observe(salida[0].parentElement);
    const pinta = () => {
      const v = campo.value.trim().slice(0, 22);
      salida.forEach(s => { s.textContent = v || "Familia López"; });
      const nombres = botas.map(b => b.value.trim().slice(0, 10));
      nombres.forEach((n, i) => document.querySelectorAll(`[data-bota="${i}"]`).forEach(s => { s.textContent = n || s.dataset.defecto; }));
      ajusta();
      const q = new URLSearchParams();
      if (v) q.set("letrero", v);
      if (nombres.some(Boolean)) q.set("botas", nombres.join("|"));
      if (pedir) pedir.href = "navidad/" + (q.toString() ? "?" + q : "") + "#chimenea";
    };
    [campo, ...botas].forEach(c => c.addEventListener("input", pinta)); pinta();
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

  // ===== Temporada navideña (assets/temporada.css + clase "temporada-navidad" en <body>) =====
  if (document.body.classList.contains("temporada-navidad")) {
    // Aldea de casitas de jengibre (dibujada aquí para no repetir el SVG en cada página)
    const casa = (x, s, cuerpo, luz) => `<g class="casa" transform="translate(${x} ${120 - 110 * s}) scale(${s})">
      <rect x="80" y="16" width="13" height="26" fill="#8a4f2a"/><rect x="77" y="12" width="19" height="7" rx="3" fill="#fffaf2"/>
      <rect x="18" y="48" width="84" height="62" rx="3" fill="${cuerpo}"/>
      <path d="M18 52q5 7 10 0t10 0 10 0 10 0 10 0 10 0 10 0 10 0 4 0" fill="none" stroke="#fffaf2" stroke-width="3.2" stroke-linecap="round"/>
      <path d="M8 54L60 12l52 42z" fill="#9a5a30"/>
      <path d="M8 54L60 12l52 42" fill="none" stroke="#fffaf2" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="35" cy="42" r="4" fill="#d6313a"/><circle cx="85" cy="42" r="4" fill="#2f8a4e"/>
      <circle cx="60" cy="34" r="7" fill="#fffaf2"/><path d="M60 27a7 7 0 0 1 0 14M53 34a7 7 0 0 1 14 0" fill="none" stroke="#d6313a" stroke-width="2.4"/>
      <rect class="ventana" x="27" y="66" width="17" height="17" rx="2" fill="${luz}" stroke="#fffaf2" stroke-width="3"/>
      <rect class="ventana" x="76" y="66" width="17" height="17" rx="2" fill="${luz}" stroke="#fffaf2" stroke-width="3"/>
      <path d="M35.5 66v17M27 74.5h17M84.5 66v17M76 74.5h17" stroke="#fffaf2" stroke-width="2"/>
      <path d="M50 110V88a10 10 0 0 1 20 0v22z" fill="#7a4424" stroke="#fffaf2" stroke-width="3"/>
      <circle cx="65" cy="99" r="2" fill="#fffaf2"/></g>`;
    const pino = (x, s) => `<g transform="translate(${x} ${120 - 70 * s}) scale(${s})">
      <rect x="17" y="58" width="6" height="12" fill="#7a4424"/>
      <path d="M20 0L4 26h7L0 44h9L-2 60h44L31 44h9L29 26h7z" fill="#2f8a4e"/>
      <path d="M20 0l-6 10 6-3 6 3zM11 26l4-4 5 3 5-3 4 4M9 44l5-4 6 3 6-3 5 4" fill="none" stroke="#fffaf2" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></g>`;
    const tramo = `${pino(6, .9)}${casa(40, .78, "#c27a43", "#ffd77a")}${pino(140, .7)}${casa(170, 1, "#b06b38", "#ffcf66")}
      ${pino(292, .85)}${casa(326, .86, "#cf8a52", "#ffd77a")}${pino(436, .75)}${casa(466, .95, "#c27a43", "#ffcf66")}${pino(575, .8)}`;
    // Se repite el tramo de casitas según el ancho, para que nunca se estire ni se corten los techos
    const aldea = n => `<svg viewBox="0 0 ${600 * n} 130" preserveAspectRatio="xMidYMax slice" aria-hidden="true" focusable="false">
      ${Array.from({ length: n }, (_, k) => `<g transform="translate(${600 * k} 0)">${tramo}</g>`).join("")}
      <path d="M0 122${"q30-9 60 0t60 0 60 0 60 0 60 0 60 0 60 0 60 0 60 0 60 0".repeat(1)}${" t60 0".repeat(10 * (n - 1))}V130H0z" fill="#fffaf2"/></svg>`;
    const pintaAldeas = () => document.querySelectorAll("[data-aldea]").forEach(a => {
      const n = Math.max(1, Math.round(a.clientWidth / Math.max(1, a.clientHeight) / (600 / 130)));
      if (a.dataset.n !== String(n)) { a.dataset.n = n; a.innerHTML = aldea(n); }
    });
    pintaAldeas(); addEventListener("resize", pintaAldeas);

    // Nieve sobre toda la página
    if (!quieto) {
      const n = document.createElement("div"); n.className = "nieve-global"; n.setAttribute("aria-hidden", "true");
      const cuantos = innerWidth < 600 ? 24 : 42;
      n.innerHTML = Array.from({ length: cuantos }, (_, k) => {
        const copo = k % 4 === 0, z = copo ? 12 + Math.random() * 10 : 3 + Math.random() * 5;
        return `<i${copo ? ' class="copo"' : ""} style="width:${z}px;height:${z}px;opacity:${.6 + Math.random() * .4};--x:${(Math.random() * 100).toFixed(1)}vw;--dx:${(Math.random() * 60 - 30) | 0}px;animation-duration:${(9 + Math.random() * 10).toFixed(1)}s;animation-delay:-${(Math.random() * 19).toFixed(1)}s"></i>`;
      }).join("");
      document.body.appendChild(n);
    }
  }

  // Nieve
  if (!quieto) document.querySelectorAll(".nieve").forEach(n => {
    n.innerHTML = Array.from({ length: 28 }, () => {
      const z = 2 + Math.random() * 4;
      return `<i style="left:${Math.random() * 100}%;width:${z}px;height:${z}px;--dx:${(Math.random() * 40 - 20) | 0}px;animation-duration:${7 + Math.random() * 9}s;animation-delay:-${Math.random() * 14}s"></i>`;
    }).join("");
  });
})();
