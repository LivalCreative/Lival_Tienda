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
  EXTRA["CASA-abierta"] = { name: "Casita de jengibre para utensilios (interior abierto)", price: 349, horas: 9.67 };
  EXTRA["CORONA-1"] = { name: "Adorno corona con foto (mándanos la foto por WhatsApp)", price: 59, horas: 0.34 };
  EXTRA["CORONA-3"] = { name: "3 adornos corona con foto (mándanos las 3 fotos por WhatsApp)", price: 159, horas: 1.02 };
  EXTRA["CASA-div"] = { name: "Casita de jengibre para utensilios (interior con divisiones)", price: 409, horas: 11.41 };

  // Productos de la colección Navidad 2026 (assets/navidad-productos.js, si la página lo carga antes que este archivo).
  (window.NAVIDAD || []).forEach(p => p.opciones.forEach(o => {
    EXTRA[`${p.id}-${o.k}`] = { name: (p.opciones.length > 1 ? `${p.nombre} (${o.label})` : p.nombre) + (p.nota ? ` — ${p.nota}` : ""), price: o.precio, horas: o.horas };
  }));

  const KEY = "lival_carrito_v1";
  function leer() { try { return JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { return {}; } }
  function guardar(q) { try { const o = {}; Object.keys(q).forEach(k => { if (q[k] > 0) o[k] = q[k]; }); localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {} }

  // Línea extra para el mensaje y el resumen: cuántos focos de cada color hay que imprimir.
  function resumenColores(q) {
    const s = q["FOCO-set4"] || 0;
    const tot = COLORES_FOCO.map(c => ({ c, n: (q["FOCO-" + c.id] || 0) + s })).filter(x => x.n);
    return tot.length ? "Focos por color: " + tot.map(x => `${x.n} ${x.c.nombre.toLowerCase()}`).join(" · ") : "";
  }

  // Productos personalizados (cada uno es una pieza única con sus nombres). Se guardan aparte.
  const KEYP = "lival_personal_v1";
  function personales() { try { return JSON.parse(localStorage.getItem(KEYP) || "[]") || []; } catch (e) { return []; } }
  function guardarPersonales(l) { try { localStorage.setItem(KEYP, JSON.stringify(l)); } catch (e) {} }
  function agregarPersonal(item) { const l = personales(); l.push(item); guardarPersonales(l); const c = leer(); c[item.id] = 1; guardar(c); }
  function quitarPersonal(id) { guardarPersonales(personales().filter(p => p.id !== id)); const c = leer(); delete c[id]; guardar(c); }

  window.LIVAL = { EXTRA, COLORES_FOCO, leer, guardar, resumenColores, KEY, personales, agregarPersonal, quitarPersonal };
})();
