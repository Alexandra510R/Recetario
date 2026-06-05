/* ═══════════════════════════════════════════════
   script.js — Lógica compartida entre todas las páginas
   Sabores Colombianos
   ═══════════════════════════════════════════════ */

const API_URL = "https://recetario-backend-276307409989.us-central1.run.app";

/* ── TEMA OSCURO ── */
function initTheme() {
  const saved = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', saved);
  const btn = document.getElementById('btn-theme');
  if (btn) btn.textContent = saved === 'dark' ? '☀️' : '🌙';
}
function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
  const btn = document.getElementById('btn-theme');
  if (btn) btn.textContent = next === 'dark' ? '☀️' : '🌙';
}

/* ── TOAST ── */
function mostrarToast(msg, tipo = 'success') {
  let t = document.getElementById('toast');
  if (!t) {
    t = document.createElement('div');
    t.id = 'toast';
    t.className = 'toast';
    document.body.appendChild(t);
  }
  t.textContent = msg;
  t.className = `toast ${tipo} show`;
  clearTimeout(t._timer);
  t._timer = setTimeout(() => { t.className = 'toast'; }, 3500);
}

/* ── NAV SCROLL ── */
function initNavScroll() {
  const nav = document.getElementById('navbar');
  if (!nav) return;
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 20);
  });
}

/* ── MOBILE NAV ── */
function toggleMobileNav() {
  const m = document.getElementById('mobile-nav');
  if (m) m.classList.toggle('open');
}

/* ── PROFILE DROPDOWN ── */
function toggleDropdown() {
  const d = document.getElementById('profile-dropdown');
  if (d) d.classList.toggle('open');
}
document.addEventListener('click', (e) => {
  const btn = document.querySelector('.profile-btn');
  const d = document.getElementById('profile-dropdown');
  if (d && btn && !btn.contains(e.target)) d.classList.remove('open');
});

/* ── AUTH STATE: renderiza header según sesión ── */
function renderAuthHeader() {
  const preLogin  = document.getElementById('nav-pre-login');
  const postLogin = document.getElementById('nav-post-login');
  const usuario   = getUsuario();

  if (!preLogin || !postLogin) return;

  if (usuario) {
    // Restaurar datos de perfil guardados (persisten entre sesiones)
    const perfilExtra = JSON.parse(localStorage.getItem('perfil_datos') || 'null');
    if (perfilExtra) {
      const fusionado = { ...usuario, ...perfilExtra };
      localStorage.setItem('usuario', JSON.stringify(fusionado));
    }

    preLogin.classList.add('hidden');
    postLogin.classList.remove('hidden');

    const nameEl   = document.getElementById('profile-name');
    const avatarEl = document.getElementById('profile-avatar');
    if (nameEl) nameEl.textContent = usuario.nombre.split(' ')[0];

    // Mostrar foto de perfil si existe
    if (avatarEl) {
      const foto = localStorage.getItem('perfil_foto');
      if (foto && foto.length < 10) {
        // Es un emoji
        avatarEl.textContent = foto;
        avatarEl.style.fontSize = '1rem';
      } else if (foto) {
        // Es una imagen base64
        avatarEl.innerHTML = `<img src="${foto}" style="width:100%;height:100%;object-fit:cover;border-radius:50%;"/>`;
      } else {
        avatarEl.textContent = usuario.nombre[0].toUpperCase();
      }
    }
  } else {
    preLogin.classList.remove('hidden');
    postLogin.classList.add('hidden');
  }
}

/* ── HELPERS ── */
function getUsuario() {
  try { return JSON.parse(localStorage.getItem('usuario')); } catch { return null; }
}
function getToken() {
  return localStorage.getItem('token');
}
function cerrarSesion() {
  // Mantener 'perfil_datos' y 'perfil_foto' para que persistan al volver a entrar
  localStorage.removeItem('usuario');
  localStorage.removeItem('token');
  window.location.href = 'PaginaInicial.html';
}

/* ── INIT ── */
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initNavScroll();
  renderAuthHeader();
});