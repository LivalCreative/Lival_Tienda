// Dibuja en Navidad los productos de assets/navidad-productos.js (mismo formato de tarjeta que los demás).
(function () {
  const lista = window.NAVIDAD || [];
  const box = document.querySelector(".prods");
  if (!box || !lista.length) return;
  const money = n => "$" + n.toLocaleString("es-MX");
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const key = (p, o) => `${p.id}-${o.k}`;

  lista.forEach(p => {
    const desde = Math.min(...p.opciones.map(o => o.precio));
    const art = document.createElement("article");
    art.className = "prod gen"; art.id = p.id;
    const fotos = p.fotos.map(f => `<img class="foto" src="${esc(f)}" width="900" height="900" alt="${esc(p.nombre)}" loading="lazy" draggable="false">`).join("");
    const dots = p.fotos.map((_, i) => `<i${i ? "" : ' class="on"'}></i>`).join("");
    let det;
    if (p.personal) {
      det = `${p.opciones.length > 1 ? `<div class="lbl">Elige</div><div class="opts">${p.opciones.map((o, i) => `<button type="button" class="opt${i ? "" : " on"}" data-op="${o.k}">${esc(o.label)} · ${money(o.precio)}</button>`).join("")}</div>` : ""}
        <label class="lbl" for="t-${p.id}">${esc(p.personal.label)}</label>
        <input class="campo" id="t-${p.id}" maxlength="${p.personal.max}" placeholder="${esc(p.personal.ph)}">
        <div class="buy"><span class="price" data-precio>${money(p.opciones[0].precio)}</span><button type="button" class="btn add" data-addp="${p.id}">Agregar al pedido</button></div>
        <p class="err" data-err></p>
        <div class="sel" data-lista hidden></div>`;
    } else {
      det = `<div class="var">${p.opciones.map(o => `<div class="vrow"><div class="nm"><div>${esc(o.label)}${o.sub ? `<small>${esc(o.sub)}</small>` : ""}</div></div><span class="pr">${money(o.precio)}</span>
          <div class="qty"><button aria-label="Quitar" data-g="${key(p, o)}" data-d="-1">−</button><span data-q="${key(p, o)}">0</span><button class="mas" aria-label="Agregar" data-g="${key(p, o)}" data-d="1">+</button></div></div>`).join("")}</div>
        <div class="sel" data-sel></div>`;
      if (p.paquete) {
        const pk = p.paquete, ops = p.opciones.map(o => `<option value="${o.k}">${esc(o.label)}</option>`).join("");
        det += `<div class="paq">
          <div class="lbl">Arma tu paquete de ${pk.n} · ahorras ${money(pk.ahorro)}</div>
          <p class="paq-tx">Elige el modelo de cada uno; puedes repetir o combinar.</p>
          ${Array.from({ length: pk.n }, (_, i) => `<label class="paq-f"><span>${i + 1}</span><select class="campo" data-paq>${ops}</select></label>`).join("")}
          <div class="buy"><span class="price" data-paqprecio></span><button type="button" class="btn add" data-addpaq="${p.id}">Agregar paquete</button></div>
          <div class="sel" data-lista hidden></div>
        </div>`;
      }
    }
    art.innerHTML = `<div class="galwrap"><div class="gal">${fotos}</div><span class="wm" aria-hidden="true"></span></div>
      <div class="dots">${dots}</div>
      <div class="info">
        <span class="badge">${esc(p.badge)}</span>
        <h3>${esc(p.nombre)}</h3>
        <p class="lead">${esc(p.lead)}</p>
        <div class="mini"><span class="desde">${new Set(p.opciones.map(o => o.precio)).size > 1 ? "Desde " : ""}<b>${money(desde)}</b></span><button type="button" class="btn ver" data-abrir="${p.id}">Ver opciones</button></div>
        <div class="det"><ul>${p.bullets.map(b => `<li>${esc(b)}</li>`).join("")}</ul>${det}</div>
        <button type="button" class="cerrar" data-cerrar aria-label="Cerrar">✕</button>
      </div>`;
    box.insertBefore(art, box.querySelector(":scope > aside"));
  });

  function paqSel(art, p) { return [...art.querySelectorAll("[data-paq]")].map(x => p.opciones.find(o => o.k === x.value)); }
  function paqPrecio(art, p) { return paqSel(art, p).reduce((t, o) => t + o.precio, 0) - p.paquete.ahorro; }
  function pintarPaq(art, p) { const e = art.querySelector("[data-paqprecio]"); if (e) e.textContent = money(paqPrecio(art, p)); }

  function verFoto(art, o) {
    if (!o || o.f == null) return;
    const g = art.querySelector(".gal"); if (g) g.scrollTo({ left: o.f * g.clientWidth, behavior: "smooth" });
  }
  function bump() { const bar = document.getElementById("nbar"); if (!bar) return; bar.classList.remove("bump"); void bar.offsetWidth; bar.classList.add("bump"); }
  function refrescarBarra() { if (typeof cart !== "undefined") cart = LIVAL.leer(); if (typeof pintar === "function") pintar(); }

  function pintarGen() {
    const c = LIVAL.leer(), per = LIVAL.personales();
    lista.forEach(p => {
      const art = document.getElementById(p.id); if (!art) return;
      if (p.paquete) pintarPaq(art, p);
      if (p.personal || p.paquete) {
        const mios = per.filter(x => x.tipo === p.id), b = art.querySelector("[data-lista]");
        b.hidden = !mios.length;
        b.innerHTML = mios.length ? `<b>En tu pedido</b>` + mios.map(x => `<div class="ch-item"><div>${esc(x.resumen)}<br><b>${money(x.price)}</b></div><button type="button" data-qp="${x.id}">Quitar</button></div>`).join("") : "";
      }
      if (!p.personal) {
        let t = 0; const l = [];
        p.opciones.forEach(o => { const n = c[key(p, o)] || 0; const s = art.querySelector(`[data-q="${key(p, o)}"]`); if (s) s.textContent = n; if (n) { t += n * o.precio; l.push(`${n} × ${o.label}`); } });
        art.querySelector("[data-sel]").innerHTML = l.length ? `<div><b>Tu selección</b></div>${l.map(x => `<div>• ${esc(x)}</div>`).join("")}<div style="margin-top:6px">Subtotal: <b class="tot">${money(t)}</b></div>` : `<span style="color:var(--muted)">Elige cuántos quieres.</span>`;
      }
    });
  }

  box.addEventListener("click", e => {
    const g = e.target.closest("button[data-g]");
    if (g) {
      const c = LIVAL.leer(); c[g.dataset.g] = Math.max(0, (c[g.dataset.g] || 0) + (+g.dataset.d)); LIVAL.guardar(c);
      const art = g.closest("article"), p = lista.find(x => x.id === art.id);
      if (+g.dataset.d > 0) verFoto(art, p.opciones.find(o => key(p, o) === g.dataset.g));
      pintarGen(); refrescarBarra(); bump(); return;
    }
    const op = e.target.closest("button[data-op]");
    if (op) { const art = op.closest("article"), p = lista.find(x => x.id === art.id); art.querySelectorAll("[data-op]").forEach(b => b.classList.toggle("on", b === op)); const o = p.opciones.find(x => x.k === op.dataset.op); art.querySelector("[data-precio]").textContent = money(o.precio); verFoto(art, o); return; }
    const fila = e.target.closest(".vrow .nm");
    if (fila) { const art = fila.closest("article"), p = lista.find(x => x.id === art.id), b = fila.closest(".vrow").querySelector("[data-g]"); verFoto(art, p.opciones.find(o => key(p, o) === b.dataset.g)); return; }
    const add = e.target.closest("button[data-addp]");
    if (add) {
      const art = add.closest("article"), p = lista.find(x => x.id === add.dataset.addp);
      const inp = art.querySelector(".campo"), txt = inp.value.trim(), err = art.querySelector("[data-err]");
      if (!txt) { err.textContent = "Escribe " + p.personal.label.toLowerCase().replace(/ \(.*/, "") + "."; inp.focus(); return; }
      err.textContent = "";
      const sel = art.querySelector("[data-op].on"), o = sel ? p.opciones.find(x => x.k === sel.dataset.op) : p.opciones[0];
      const det = p.opciones.length > 1 ? ` (${o.label})` : "";
      LIVAL.agregarPersonal({ id: p.id + "-" + Date.now().toString(36), tipo: p.id, name: `${p.nombre}${det} — ${p.personal.label.replace(/ \(.*/, "")}: "${txt}"`, resumen: `${o.label}: "${txt}"`, price: o.precio, horas: o.horas });
      inp.value = ""; pintarGen(); refrescarBarra(); bump(); return;
    }
    const ap = e.target.closest("button[data-addpaq]");
    if (ap) {
      const art = ap.closest("article"), p = lista.find(x => x.id === ap.dataset.addpaq), sel = paqSel(art, p);
      const cuenta = {}; sel.forEach(o => { cuenta[o.label] = (cuenta[o.label] || 0) + 1; });
      const txt = Object.entries(cuenta).map(([l, n]) => n > 1 ? `${l} ×${n}` : l).join(" + ");
      LIVAL.agregarPersonal({ id: p.id + "-paq-" + Date.now().toString(36), tipo: p.id, name: `${p.nombre} — paquete de ${p.paquete.n} (${txt})${p.nota ? " — " + p.nota.replace("la foto", "las fotos") : ""}`,
        resumen: `Paquete de ${p.paquete.n}: ${txt}`, price: paqPrecio(art, p), horas: +sel.reduce((t, o) => t + o.horas, 0).toFixed(2) });
      pintarGen(); refrescarBarra(); bump(); return;
    }
    const q = e.target.closest("button[data-qp]");
    if (q) { LIVAL.quitarPersonal(q.dataset.qp); pintarGen(); refrescarBarra(); }
  });
  box.addEventListener("change", e => {
    const s = e.target.closest("select[data-paq]"); if (!s) return;
    const art = s.closest("article"), p = lista.find(x => x.id === art.id);
    pintarPaq(art, p); verFoto(art, p.opciones.find(o => o.k === s.value));
  });
  pintarGen();
  window.addEventListener("pageshow", pintarGen);
})();
