/* Balai Taltalon concept site: small, dependency-free */
(function () {
  "use strict";
  var doc = document.documentElement;
  var body = document.body;
  var PAGE = "balaitaltalonnatureresort";
  var PHONE = "+639429727377";

  /* ---------- header + floating chat ---------- */
  var header = document.querySelector(".site-header");
  var chat = document.querySelector(".float-chat");
  var inquireSec = document.getElementById("inquire");
  function onScroll() {
    var y = window.scrollY;
    header.classList.toggle("scrolled", y > 40);
    // hide the floating button while the inquiry form is on screen (it has its own buttons)
    var r = inquireSec.getBoundingClientRect();
    var overForm = r.top < window.innerHeight * 0.85 && r.bottom > 120;
    chat.classList.toggle("show", y > window.innerHeight * 0.6 && !overForm);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- mobile menu ---------- */
  var toggle = document.querySelector(".menu-toggle");
  function setMenu(open) {
    body.classList.toggle("menu-open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  }
  toggle.addEventListener("click", function () { setMenu(!body.classList.contains("menu-open")); });
  document.querySelectorAll(".nav a").forEach(function (a) {
    a.addEventListener("click", function () { setMenu(false); });
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });

  /* ---------- reveal on scroll ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- lightbox ---------- */
  var lb = document.getElementById("lightbox");
  var lbImg = lb.querySelector("img");
  var items = Array.prototype.slice.call(document.querySelectorAll(".g-item"));
  var idx = 0, lastFocus = null;
  function show(i) {
    idx = (i + items.length) % items.length;
    var a = items[idx];
    lbImg.src = a.getAttribute("href");
    lbImg.alt = (a.querySelector("img") || {}).alt || "";
  }
  function openLb(i) { lastFocus = document.activeElement; show(i); lb.hidden = false; body.style.overflow = "hidden"; lb.querySelector(".lb-close").focus(); }
  function closeLb() { lb.hidden = true; body.style.overflow = ""; if (lastFocus) lastFocus.focus(); }
  items.forEach(function (a, i) {
    a.addEventListener("click", function (e) { e.preventDefault(); openLb(i); });
  });
  lb.querySelector(".lb-close").addEventListener("click", closeLb);
  lb.querySelector(".lb-prev").addEventListener("click", function () { show(idx - 1); });
  lb.querySelector(".lb-next").addEventListener("click", function () { show(idx + 1); });
  lb.addEventListener("click", function (e) { if (e.target === lb) closeLb(); });
  document.addEventListener("keydown", function (e) {
    if (lb.hidden) return;
    if (e.key === "Escape") closeLb();
    if (e.key === "ArrowLeft") show(idx - 1);
    if (e.key === "ArrowRight") show(idx + 1);
  });
  var tx = null;
  lb.addEventListener("touchstart", function (e) { tx = e.touches[0].clientX; }, { passive: true });
  lb.addEventListener("touchend", function (e) {
    if (tx === null) return;
    var dx = e.changedTouches[0].clientX - tx;
    if (Math.abs(dx) > 40) show(idx + (dx < 0 ? 1 : -1));
    tx = null;
  });

  /* ---------- inquiry: ready-made message ---------- */
  var form = document.getElementById("inquiryForm");
  var preview = document.getElementById("msgPreview");
  var status = document.getElementById("formStatus");
  var smsBtn = document.getElementById("sendSms");
  var edited = false;

  // dates: no past check-in; check-out after check-in
  var today = new Date(); today.setMinutes(today.getMinutes() - today.getTimezoneOffset());
  var iso = today.toISOString().slice(0, 10);
  document.querySelectorAll('input[type="date"]').forEach(function (d) { d.min = iso; });
  function linkDates(inEl, outEl) {
    inEl.addEventListener("change", function () {
      outEl.min = inEl.value || iso;
      if (outEl.value && outEl.value <= inEl.value) outEl.value = "";
    });
  }
  linkDates(form.checkin, form.checkout);
  linkDates(document.getElementById("planIn"), document.getElementById("planOut"));

  function fmt(d) {
    if (!d) return "";
    var p = d.split("-");
    var dt = new Date(+p[0], +p[1] - 1, +p[2]);
    return dt.toLocaleDateString("en-PH", { weekday: "short", month: "short", day: "numeric", year: "numeric" });
  }
  function nights(a, b) {
    if (!a || !b) return 0;
    return Math.round((new Date(b) - new Date(a)) / 86400000);
  }

  function buildMessage() {
    var f = form;
    var name = f.name.value.trim();
    var lines = [];
    lines.push("Hi Balai Taltalon! 🌿");
    lines.push("");
    lines.push((name ? "This is " + name + ". " : "") + "I'd like to ask about rates and availability:");
    lines.push("");
    lines.push("• Stay: " + f.stay.value);
    if (f.checkin.value || f.checkout.value) {
      var n = nights(f.checkin.value, f.checkout.value);
      lines.push("• Dates: " + (fmt(f.checkin.value) || "?") + " to " + (fmt(f.checkout.value) || "?") + (n > 0 ? " (" + n + " night" + (n > 1 ? "s" : "") + ")" : ""));
    } else {
      lines.push("• Dates: flexible, not set yet");
    }
    if (f.guests.value) lines.push("• Guests: " + f.guests.value);
    if (f.occasion.value) lines.push("• Occasion: " + f.occasion.value);
    if (f.pets.value) lines.push("• Bringing pets: Yes");
    if (f.notes.value.trim()) { lines.push(""); lines.push(f.notes.value.trim()); }
    lines.push("");
    lines.push("Thank you!");
    return lines.join("\n");
  }
  function refresh() {
    if (!edited) preview.value = buildMessage();
    smsBtn.href = "sms:" + PHONE + "?&body=" + encodeURIComponent(preview.value);
  }
  form.addEventListener("input", function (e) { if (e.target !== preview) refresh(); });
  form.addEventListener("change", function (e) { if (e.target !== preview) refresh(); });
  preview.addEventListener("input", function () { edited = true; refresh(); });
  refresh();

  function copy(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text).then(function () { return true; }, function () { return fallbackCopy(text); });
    }
    return Promise.resolve(fallbackCopy(text));
  }
  function fallbackCopy(text) {
    var ta = document.createElement("textarea");
    ta.value = text; ta.setAttribute("readonly", ""); ta.style.position = "fixed"; ta.style.opacity = "0";
    document.body.appendChild(ta); ta.select();
    var ok = false; try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
    document.body.removeChild(ta); return ok;
  }
  function validName() {
    var ok = form.name.value.trim().length > 0;
    form.name.classList.toggle("invalid", !ok);
    if (!ok) { status.textContent = "Please add your name so we know who's asking."; form.name.focus(); }
    return ok;
  }

  document.getElementById("sendMessenger").addEventListener("click", function () {
    if (!validName()) return;
    // open the window synchronously (popup blockers), then copy
    var win = window.open("https://m.me/" + PAGE + "?text=" + encodeURIComponent(preview.value), "_blank", "noopener");
    copy(preview.value).then(function (ok) {
      status.textContent = ok
        ? "Message copied. Paste it into the Messenger chat and hit send."
        : "Messenger is opening. Copy the message above and paste it into the chat.";
    });
    if (!win) status.textContent = "Couldn't open Messenger. Copy the message above and send it to m.me/" + PAGE;
  });
  document.getElementById("copyOnly").addEventListener("click", function () {
    copy(preview.value).then(function (ok) {
      status.textContent = ok ? "Copied to your clipboard." : "Select the message above and copy it manually.";
    });
  });
  smsBtn.addEventListener("click", function (e) {
    if (!validName()) { e.preventDefault(); return; }
    status.textContent = "Opening your messages app…";
  });
  form.name.addEventListener("input", function () { form.name.classList.remove("invalid"); if (status.textContent.indexOf("name") > -1) status.textContent = ""; });

  /* ---------- plan bar + "stay" links prefill the form ---------- */
  document.getElementById("planForm").addEventListener("submit", function (e) {
    e.preventDefault();
    var pi = document.getElementById("planIn").value, po = document.getElementById("planOut").value, pg = document.getElementById("planGuests").value;
    if (pi) form.checkin.value = pi;
    if (po) form.checkout.value = po;
    if (pg) {
      form.guests.value = pg.replace(" / event", "");
      if (pg.indexOf("event") > -1) form.stay.value = "Event / team building";
      else if (pg === "10–15") form.stay.value = "Whole resort (villa + guest wing)";
    }
    edited = false; refresh();
    document.getElementById("inquire").scrollIntoView({ behavior: "smooth" });
    setTimeout(function () { form.name.focus({ preventScroll: true }); }, 700);
  });
  document.querySelectorAll("[data-stay]").forEach(function (a) {
    a.addEventListener("click", function () {
      form.stay.value = a.getAttribute("data-stay");
      edited = false; refresh();
    });
  });

  var yr = document.getElementById("year");
  if (yr) yr.textContent = new Date().getFullYear();
})();
