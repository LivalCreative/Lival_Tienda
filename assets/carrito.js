// Carrito compartido entre secciones (Duende, Navidad, Más productos) y productos fuera del catálogo del duende.
// Para agregar un producto nuevo: súmalo a EXTRA_PRODUCTOS con su precio y horas de impresión.
(function () {
  const COLORES_FOCO = [
    { id: "rojo", nombre: "Rojo", color: "#e53935" },
    { id: "verde", nombre: "Verde", color: "#2ecc40" },
    { id: "azul", nombre: "Azul", color: "#1e6fd9" },
    { id: "blanco", nombre: "Blanco", color: "#f4efe6" }
  ];
  const H_FOCO = 1.42;
  const EXTRA = {};
  COLORES_FOCO.forEach(c => { EXTRA["FOCO-" + c.id] = { name: `Foco navideño ${c.nombre.toLowerCase()}`, price: 79, horas: H_FOCO }; });
  EXTRA["FOCO-set4"] = { name: "Set de 4 focos navideños (rojo, verde, azul, blanco)", price: 289, horas: H_FOCO * 4 };

  const KEY = "lival_carrito_v1";
  function leer() { try { return JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { return {}; } }
  function guardar(q) { try { const o = {}; Object.keys(q).forEach(k => { if (q[k] > 0) o[k] = q[k]; }); localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {} }

  // Línea extra para el mensaje y el resumen: cuántos focos de cada color hay que imprimir.
  function resumenColores(q) {
    const s = q["FOCO-set4"] || 0;
    const tot = COLORES_FOCO.map(c => ({ c, n: (q["FOCO-" + c.id] || 0) + s })).filter(x => x.n);
    return tot.length ? "Focos por color: " + tot.map(x => `${x.n} ${x.c.nombre.toLowerCase()}`).join(" · ") : "";
  }

  window.LIVAL = { EXTRA, COLORES_FOCO, leer, guardar, resumenColores, KEY };
})();
