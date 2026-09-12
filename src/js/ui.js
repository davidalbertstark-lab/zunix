import {
  validateDateOfBirth,
  validateGradYear,
  validateLevel
} from './validation.js';

let currentStep = 0;
let steps = [];
let locationData = {}; // holds regions / states / cities

/* -------------------------------------------------- *
 * UI boot – called from main.js                      *
 * -------------------------------------------------- */
export async function initUI() {
  steps = document.querySelectorAll('.step');

  const campusRegionSelect = document.getElementById('campusRegion');
  const stateSelect        = document.getElementById('state');
  const citySelect         = document.getElementById('city');
  const levelSelect        = document.getElementById('level');
  const genderSelect       = document.getElementById('gender');

  /* ---- Load region → state → city JSON (relative + fallback) ---- */
  try {
    let res = await fetch('./data/location-data.json');
    if (!res.ok) res = await fetch('/data/location-data.json');
    locationData = await res.json();
  } catch (err) {
    console.error('Failed to load location data:', err);
  }

  populateCampusRegions();

  /* ---- Cascading listeners ---- */
  campusRegionSelect.addEventListener('change', () => {
    populateStates(campusRegionSelect.value);
    citySelect.innerHTML = '<option value="">Select city</option>';
    populateInstitutionOptions('');
  });

  stateSelect.addEventListener('change', () => {
    populateCities(campusRegionSelect.value, stateSelect.value);
    populateInstitutionOptions('');
  });

  citySelect.addEventListener('change', () =>
    populateInstitutionOptions(citySelect.value.trim())
  );

  levelSelect.addEventListener('change', populateGradYears); // auto-update grad years

  if (genderSelect) {
    genderSelect.addEventListener('change', () => {
      const avatarImg = document.getElementById('summaryAvatar');
      if (avatarImg) {
        avatarImg.src = genderSelect.value === 'female' ? 'src/img/girls.png' : 'src/img/boyss.png';
      }
    });
  }

  /* ---- Step navigation buttons ---- */
  document.getElementById('step1NextBtn')?.addEventListener('click', nextStep);
  document.getElementById('step2NextBtn')?.addEventListener('click', nextStep);
  document.getElementById('step3NextBtn')?.addEventListener('click', nextStep);
  document.getElementById('step4NextBtn')?.addEventListener('click', nextStep);

  document.getElementById('step2BackBtn')?.addEventListener('click', prevStep);
  document.getElementById('step3BackBtn')?.addEventListener('click', prevStep);
  document.getElementById('step4BackBtn')?.addEventListener('click', prevStep);
  document.getElementById('step5BackBtn')?.addEventListener('click', prevStep);
  document.getElementById('step6BackBtn')?.addEventListener('click', prevStep);

  /* ---- Strict Step-5 guard ---- */
  document.getElementById('finishBtn').addEventListener('click', () => {
    const institution = document.getElementById('institution');
    const course      = document.getElementById('course');
    const faculty     = document.getElementById('faculty');
    const level       = document.getElementById('level');
    const gradYear    = document.getElementById('gradYear');

    let isValid = true;

    ['institution','course','faculty','level','gradYear'].forEach(id =>
      (document.getElementById(`${id}Error`).textContent = '')
    );

    if (!institution.value.trim()) {
      document.getElementById('institutionError').textContent = 'Institution is required';
      institution.focus(); isValid = false;
    } else if (!course.value.trim()) {
      document.getElementById('courseError').textContent = 'Course is required';
      course.focus(); isValid = false;
    } else if (!faculty.value.trim()) {
      document.getElementById('facultyError').textContent = 'Faculty is required';
      faculty.focus(); isValid = false;
    } else if (!level.value.trim()) {
      document.getElementById('levelError').textContent = 'Level is required';
      level.focus(); isValid = false;
    } else if (!gradYear.value.trim()) {
      document.getElementById('gradYearError').textContent = 'Graduation year is required';
      gradYear.focus(); isValid = false;
    }

    const upperAbbrevPattern = /^[A-Z]{1,4}$/;
    if (isValid && upperAbbrevPattern.test(course.value.trim())) {
      document.getElementById('courseError').textContent =
        'Course name looks like an abbreviation.';
      course.focus(); isValid = false;
    }
    if (isValid && upperAbbrevPattern.test(faculty.value.trim())) {
      document.getElementById('facultyError').textContent =
        'Faculty name looks like an abbreviation.';
      faculty.focus(); isValid = false;
    }

    if (isValid && !validateLevel(level.value)) {
      document.getElementById('levelError').textContent = 'Invalid level.';
      level.focus(); isValid = false;
    }
    if (isValid && !validateGradYear(gradYear.value)) {
      document.getElementById('gradYearError').textContent = 'Invalid graduation year.';
      gradYear.focus(); isValid = false;
    }

    if (isValid) {
      nextStep();
      populateSummary();    
    }
  });

  const completeBtn = document.getElementById('completeSetupBtn');
  if (completeBtn) completeBtn.addEventListener('click', () => {
    // window.location.href = '/dashboard.html';
  });

  populateLevels();         //  order matters now
  populateGradYears();      //  triggers based on default or selected level
  populateInstitutionOptions('');
}

/* -------------------------------------------------- *
 * Dropdown helpers                                   *
 * -------------------------------------------------- */
function populateCampusRegions() {
  const select = document.getElementById('campusRegion');
  select.innerHTML = '<option value="">Select region</option>';
  Object.keys(locationData).forEach(r => {
    const opt = document.createElement('option');
    opt.value = r; opt.textContent = r; select.appendChild(opt);
  });
}
function populateStates(region) {
  const select = document.getElementById('state');
  select.innerHTML = '<option value="">Select state</option>';
  if (!region || !locationData[region]) return;
  Object.keys(locationData[region]).forEach(st => {
    const opt = document.createElement('option');
    opt.value = st; opt.textContent = st; select.appendChild(opt);
  });
}
function populateCities(region, state) {
  const select = document.getElementById('city');
  select.innerHTML = '<option value="">Select city</option>';
  if (!region || !state || !locationData[region]) return;
  (locationData[region][state] || []).forEach(ct => {
    const opt = document.createElement('option');
    opt.value = ct; opt.textContent = ct; select.appendChild(opt);
  });
}
function populateLevels() {
  const select = document.getElementById('level');
  select.innerHTML = '<option value="">Select level</option>';
  [100, 200, 300, 400, 500].forEach(l => {
    const opt = document.createElement('option');
    opt.value = l;
    opt.textContent = `${l} Level`;
    select.appendChild(opt);
  });
}
function populateGradYears() {
  const select = document.getElementById('gradYear');
  const level = parseInt(document.getElementById('level')?.value || 0);
  const currentYear = new Date().getFullYear();
  let years = [];

  if (level === 100) {
    years = [currentYear + 4, currentYear + 5];
  } else if (level === 200) {
    years = [currentYear + 3, currentYear + 4];
  } else if (level === 300) {
    years = [currentYear + 2, currentYear + 3];
  } else if (level === 400) {
    years = [currentYear + 1, currentYear + 2];
  } else if (level === 500) {
    years = [currentYear + 1];
  } else {
    years = [currentYear + 1, currentYear + 2, currentYear + 3, currentYear + 4];
  }

  years = years.filter(y => y >= currentYear);

  select.innerHTML = '<option value="">Select graduation year</option>';
  years.forEach(year => {
    const opt = document.createElement('option');
    opt.value = year;
    opt.textContent = year;
    select.appendChild(opt);
  });
}
async function populateInstitutionOptions(city) {
  const dl = document.getElementById('institutionList');
  if (!dl) return;
  dl.innerHTML = '';
  if (!city) return;

  try {
    let res = await fetch('./json/institution.json');
    if (!res.ok) res = await fetch('/json/institution.json');
    const map = await res.json();
    (map.institutions[city] || []).forEach(name => {
      const opt = document.createElement('option');
      opt.value = name;
      dl.appendChild(opt);
    });
  } catch (e) {
    console.error('Institution fetch error:', e);
  }
}

/* -------------------------------------------------- *
 * Navigation                                         *
 * -------------------------------------------------- */
function nextStep() {
  if (currentStep < steps.length - 1 && validateStep(currentStep)) {
    steps[currentStep].classList.remove('active');
    steps[++currentStep].classList.add('active');
  }
}
function prevStep() {
  if (currentStep > 0) {
    steps[currentStep].classList.remove('active');
    steps[--currentStep].classList.add('active');
  }
}

/* -------------------------------------------------- *
 * Validation per step                                *
 * -------------------------------------------------- */
function validateStep(step) {
  let valid = true;
  steps[step].querySelectorAll('.error').forEach(e => e.textContent = '');
  steps[step].querySelectorAll('input,select').forEach(inp => {
    const err = document.getElementById(`${inp.id}Error`);
    if (inp.hasAttribute('required') && !inp.value.trim()) {
      if (err) err.textContent = 'This field is required.'; valid = false;
    }
    if (inp.id === 'username') {
      if (!/^[a-z0-9_]{3,20}$/.test(inp.value)) {
        if (err) err.textContent = 'Only small letters, numbers, or _ (3–20 chars)'; valid = false;
      }
    }
  });

  if (step === 2) {
    const dobRes = validateDateOfBirth(document.getElementById('dob').value);
    if (!dobRes.valid) {
      document.getElementById('dobError').textContent = dobRes.message; valid = false;
    }
  }

  if (step === 3) {
    if (!document.getElementById('state').value) {
      document.getElementById('stateError').textContent = 'Please select your state.'; valid = false;
    }
    if (!document.getElementById('city').value) {
      document.getElementById('cityError').textContent = 'Please select your city.'; valid = false;
    }
  }

  if (step === 4) {
    const course = document.getElementById('course').value.trim();
    const faculty = document.getElementById('faculty').value.trim();
    const cap4 = /^[A-Z]{1,4}$/;

    if (cap4.test(course)) {
      document.getElementById('courseError').textContent = 'Course name looks like an abbreviation.'; valid = false;
    }
    if (cap4.test(faculty)) {
      document.getElementById('facultyError').textContent = 'Faculty name looks like an abbreviation.'; valid = false;
    }
    if (!validateGradYear(document.getElementById('gradYear').value)) {
      document.getElementById('gradYearError').textContent = 'Invalid graduation year.'; valid = false;
    }
    if (!validateLevel(document.getElementById('level').value)) {
      document.getElementById('levelError').textContent = 'Invalid level.'; valid = false;
    }
  }
  return valid;
}

/* -------------------------------------------------- *
 * Summary display                                    *
 * -------------------------------------------------- */
export function populateSummary(email = null, fullName = null) {
  const enteredFullName = document.getElementById('fullName')?.value?.trim();
  const nameEl = document.getElementById('summaryName');
  if (nameEl) {
    nameEl.textContent = fullName || enteredFullName || localStorage.getItem('zunix_userName') || 'Student Member';
  }

  const emailEl = document.getElementById('summaryEmail');
  if (emailEl) {
    emailEl.textContent = email || localStorage.getItem('zunix_userEmail') || 'student@zunix.africa';
  }

  const uname = document.getElementById('username')?.value?.trim();
  const unameEl = document.getElementById('summaryUsername');
  if (unameEl) {
    unameEl.textContent = uname ? `@${uname}` : '@student';
  }

  const inst = document.getElementById('institution')?.value?.trim();
  const instEl = document.getElementById('summaryInstitution');
  if (instEl) {
    instEl.textContent = inst || 'Institution';
  }

  const course = document.getElementById('course')?.value?.trim();
  const courseEl = document.getElementById('summaryCourse');
  if (courseEl) {
    courseEl.textContent = course || 'General Studies';
  }

  const faculty = document.getElementById('faculty')?.value?.trim();
  const facultyEl = document.getElementById('summaryFaculty');
  if (facultyEl) {
    facultyEl.textContent = faculty || 'Faculty';
  }

  const state = document.getElementById('state')?.value?.trim();
  const city = document.getElementById('city')?.value?.trim();
  const campusEl = document.getElementById('summaryCampus');
  if (campusEl) {
    campusEl.textContent = (city && state) ? `${city}, ${state}` : (state || 'Campus Hub');
  }

  const levelSelect = document.getElementById('level');
  const levelLabel = levelSelect?.options[levelSelect?.selectedIndex]?.text || 'Level';
  const levelEl = document.getElementById('summaryLevel');
  if (levelEl) {
    levelEl.textContent = levelLabel;
  }

  const gradYear = document.getElementById('gradYear')?.value?.trim();
  const gradEl = document.getElementById('summaryGradYear');
  if (gradEl) {
    gradEl.textContent = gradYear || (new Date().getFullYear() + 4).toString();
  }

  // Dynamic Avatar switching based on gender
  const gender = document.getElementById('gender')?.value?.toLowerCase();
  const avatarImg = document.getElementById('summaryAvatar');
  if (avatarImg) {
    avatarImg.src = gender === 'female' ? 'src/img/girls.png' : 'src/img/boyss.png';
    avatarImg.alt = gender === 'female' ? 'Female Student Avatar' : 'Male Student Avatar';
  }

  // Dynamic Student ID badge
  const idTag = document.getElementById('summaryIdTag');
  if (idTag) {
    const seed = (uname || 'STARK').toUpperCase().replace(/[^A-Z0-9]/g, '').slice(0, 4);
    idTag.textContent = `ID: ZUN-${new Date().getFullYear()}-${seed || 'ZUNX'}`;
  }
}

/* -------------------------------------------------- *
 * Final transition after Firestore save              *
 * -------------------------------------------------- */
export function finishSetup() {
  if (currentStep < steps.length - 1) {
    steps[currentStep].classList.remove('active');
    steps[++currentStep].classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}
