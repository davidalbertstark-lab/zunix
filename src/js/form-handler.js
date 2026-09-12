// src/js/form-handler.js
import { db } from './firebase.js';
import {
  doc,
  setDoc,
  getDoc, // NEW: Needed to check if student profile already exists
  serverTimestamp
} from 'https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js';
import { populateSummary, finishSetup } from './ui.js';

/* -------------------------------------------------- *
 * Attach listener once user is available             *
 * -------------------------------------------------- */
export function initFormHandler(user) {
  const submitBtn = document.getElementById('submitBtn');
  if (!submitBtn) return;

  // Prevent duplicate listeners on hot reloads
  const freshBtn = submitBtn.cloneNode(true);
  submitBtn.parentNode.replaceChild(freshBtn, submitBtn);

  freshBtn.addEventListener('click', e => handleFormSubmit(e, user, freshBtn));
}

/* -------------------------------------------------- *
 * Submit handler                                     *
 * -------------------------------------------------- */
async function handleFormSubmit(event, user, btn) {
  event.preventDefault();

  btn.disabled = true;
  btn.textContent = 'Saving...';

  const data = extractFormData();
  if (!data) {
    btn.disabled = false;
    btn.textContent = 'Confirm & Submit';
    alert('Please complete all required fields.');
    return;
  }

  // If authenticated user exists, persist to Firestore
  if (user?.uid) {
    try {
      const ref = doc(db, 'students', user.uid);
      const snapshot = await getDoc(ref);

      const payload = {
        ...data,
        uid: user.uid,
        email: user.email,
        ...(snapshot.exists() ? {} : { createdAt: serverTimestamp() })
      };

      await setDoc(ref, payload, { merge: true });
      localStorage.setItem('zunix_student_profile', JSON.stringify(payload));
      populateSummary(user.email, user.displayName || data.fullName);
      finishSetup();
      console.log('Student profile stored successfully in Firestore.');
      return;
    } catch (err) {
      console.warn('Firestore write failed, falling back to local session:', err);
    }
  }

  // Fallback for guest preview / demo mode
  const localPayload = {
    ...data,
    uid: user?.uid || 'guest_' + Date.now(),
    email: user?.email || localStorage.getItem('zunix_userEmail') || 'student@zunix.africa',
    createdAt: new Date().toISOString()
  };
  localStorage.setItem('zunix_student_profile', JSON.stringify(localPayload));
  populateSummary(localPayload.email, data.fullName || 'Student Member');
  finishSetup();
  console.log('Student profile stored in local session.');
}

/* -------------------------------------------------- *
 * Extract & sanitize form values                     *
 * -------------------------------------------------- */
function extractFormData() {
  try {
    const safe = id => (document.getElementById(id)?.value || '').trim();

    return {
      fullName:     safe('fullName'),
      username:     safe('username'),
      gender:       safe('gender'),
      dob:          safe('dob'),
      region:       safe('campusRegion'),
      state:        safe('state'),
      city:         safe('city'),
      institution:  safe('institution'),
      course:       safe('course'),
      faculty:      safe('faculty'),
      level:        safe('level'),
      gradYear:     safe('gradYear')
    };
  } catch (err) {
    console.error('Error extracting form data:', err);
    return null;
  }
}
