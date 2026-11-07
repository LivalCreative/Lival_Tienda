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
  COLORES_FOCO.forEach(c => { EXTRA["FOCO-" + c.id] = { name: `Foco navideño ${c.nombre.toLowerCase()}`, price: 70, horas: H_FOCO }; });
  EXTRA["FOCO-set4"] = { name: "Set de 4 focos navideños (rojo, verde, azul, blanco)", price: 250, horas: H_FOCO * 4 };
  EXTRA["CASA-abierta"] = { name: "Casita de jengibre para utensilios (interior abierto)", price: 270, horas: 9.67 };
  EXTRA["CORONA-1"] = { name: "Adorno corona con foto (mándanos la foto por WhatsApp)", price: 59, horas: 0.34 };
  EXTRA["CORONA-3"] = { name: "3 adornos corona con foto (mándanos las 3 fotos por WhatsApp)", price: 159, horas: 1.02 };
  EXTRA["CASA-div"] = { name: "Casita de jengibre para utensilios (interior con divisiones)", price: 300, horas: 11.41 };

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

  // Cupo de Navidad (ocupacion.json, lo actualiza el tablero Pedidos 3D): cuando ya no caben más horas de impresión
  // antes del corte, las piezas grandes se marcan como agotadas, empezando por las de más horas.
  let cupo = null;
  function cerrado(horas) { return !!cupo && horas >= cupo.pieza_grande_horas && horas > cupo.horas_libres; }
  function aviso(txt) {
    const d = document.createElement("div"); d.className = "lival-aviso"; d.setAttribute("role", "status");
    d.style.cssText = "position:fixed;left:12px;right:12px;top:12px;z-index:200;max-width:520px;margin:0 auto;background:#2b2240;color:#fff;padding:14px 44px 14px 16px;border-radius:16px;box-shadow:0 8px 24px rgba(0,0,0,.25);font:inherit;line-height:1.4";
    d.innerHTML = txt + '<button type="button" aria-label="Cerrar" style="position:absolute;top:8px;right:8px;width:32px;height:32px;border:0;border-radius:50%;background:rgba(255,255,255,.15);color:#fff;font-weight:800;cursor:pointer">✕</button>';
    d.querySelector("button").onclick = () => d.remove();
    (document.body || document.documentElement).appendChild(d); setTimeout(() => d.remove(), 15000);
  }
  try { const m = sessionStorage.getItem("lival_aviso"); if (m) { sessionStorage.removeItem("lival_aviso"); document.addEventListener("DOMContentLoaded", () => aviso(m)); } } catch (e) {}
  const yo = document.currentScript && document.currentScript.src;
  if (yo && window.fetch) {
    fetch(new URL("../ocupacion.json", yo).href + "?t=" + Date.now()).then(r => r.ok ? r.json() : null).then(j => {
      if (!j || !j.navidad) return;
      cupo = { horas_libres: +j.navidad.horas_libres || 0, pieza_grande_horas: +j.navidad.pieza_grande_horas || 8 };
      // Quitar del carrito lo que ya no alcanzamos a hacer antes de Navidad
      const c = leer(), quitados = [];
      Object.keys(c).forEach(k => { if (EXTRA[k] && cerrado(EXTRA[k].horas)) { quitados.push(EXTRA[k].name); delete c[k]; } });
      const per = personales(), quedan = per.filter(x => { if (cerrado(+x.horas || 0)) { quitados.push(x.name); delete c[x.id]; return false; } return true; });
      if (quitados.length) {
        guardar(c); guardarPersonales(quedan);
        try { sessionStorage.setItem("lival_aviso", "Quitamos de tu pedido " + quitados.map(n => "<b>" + n.replace(/[<>&]/g, "") + "</b>").join(", ") + ": ya no alcanzamos a imprimirlo antes de Navidad. Escríbenos por WhatsApp si lo quieres para después."); } catch (e) {}
        const r = leer(); if (Object.keys(c).length === Object.keys(r).length && !quitados.some(n => Object.keys(r).some(k => EXTRA[k] && EXTRA[k].name === n))) { location.reload(); return; }
      }
      document.dispatchEvent(new CustomEvent("lival:cupo"));
    }).catch(() => {});
  }

  window.LIVAL = { EXTRA, COLORES_FOCO, leer, guardar, resumenColores, KEY, personales, agregarPersonal, quitarPersonal, cerrado, get cupo() { return cupo; } };
})();
