// js/main.js — root entry for the student-setup flow

/* ---------- UI Controls ---------- */
import { initUI, populateSummary } from './ui.js';

/* ---------- Firebase Services ---------- */
import { auth, onAuthChange } from './firebase.js';

/* ---------- Form Handler ---------- */
import { initFormHandler } from './form-handler.js';

/* ---------- Setup Form Dynamics ---------- */
import { initSetupForm } from './setup-student.js';

/* ---------- App Boot ---------- */
document.addEventListener('DOMContentLoaded', () => {
  // Build the multi-step UI
  initUI();

  // Wire dynamic dropdowns (state → city etc.)
  initSetupForm();

  // Listen for Firebase auth state
  try {
    onAuthChange(user => {
      if (user) {
        populateSummary(user.email, user.displayName || '');
        initFormHandler(user);
      } else {
        // Enable preview/guest testing mode without blocking with a redirect
        initFormHandler(null);
        populateSummary();
      }
    });
  } catch (err) {
    console.warn('Auth observer unavailable, falling back to preview mode:', err);
    initFormHandler(null);
    populateSummary();
  }
});

/* -------------------------------------------------- *
 *  Fallback direct listener (optional, not required) *
 * -------------------------------------------------- *
 *  If you ever need raw access to auth in another     *
 *  script, you can still use this pattern:            *
 *
 *    auth.onAuthStateChanged(user => { ... });        *
 * -------------------------------------------------- */
