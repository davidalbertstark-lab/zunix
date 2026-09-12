// src/js/theme.js — Unified Zunix Dark/Light Theme Engine

export function initTheme() {
  const savedTheme = localStorage.getItem('zunix_theme');
  const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const activeTheme = savedTheme || (systemPrefersDark ? 'dark' : 'dark'); // Default to dark cyberpunk

  applyTheme(activeTheme);

  // Attach listener to all theme toggle buttons on page
  document.querySelectorAll('.theme-toggle-btn').forEach(btn => {
    btn.addEventListener('click', toggleTheme);
  });
}

export function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('zunix_theme', theme);

  document.querySelectorAll('.theme-toggle-btn').forEach(btn => {
    const icon = btn.querySelector('.theme-icon') || btn;
    if (theme === 'light') {
      icon.textContent = '🌙';
      btn.setAttribute('title', 'Switch to Dark Cyberpunk Theme');
      btn.setAttribute('aria-label', 'Switch to Dark Theme');
    } else {
      icon.textContent = '☀️';
      btn.setAttribute('title', 'Switch to Light Theme');
      btn.setAttribute('aria-label', 'Switch to Light Theme');
    }
  });
}

export function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme') || 'dark';
  const next = current === 'dark' ? 'light' : 'dark';
  applyTheme(next);
}

// Attach to window for global access
if (typeof window !== 'undefined') {
  window.ZunixTheme = { initTheme, applyTheme, toggleTheme };
}

// Auto-run if loaded via module or script
if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTheme);
  } else {
    initTheme();
  }
}

