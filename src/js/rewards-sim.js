// src/js/rewards-sim.js — Interactive Live Rewards & ZP Gamification Simulator

export const RANKS = [
  { name: 'Rookie Pioneer', min: 0, max: 499, badge: '🌱', color: '#38bdf8' },
  { name: 'Campus Innovator', min: 500, max: 1199, badge: '⚡', color: '#00ff99' },
  { name: 'Elite Architect', min: 1200, max: 2499, badge: '🔥', color: '#ffcc00' },
  { name: 'Master Fellow', min: 2500, max: Infinity, badge: '👑', color: '#ff0077' }
];

let currentXP = 845;

export function getRank(xp) {
  return RANKS.find(r => xp >= r.min && xp <= r.max) || RANKS[0];
}

export function initRewardsSimulator() {
  const savedXP = localStorage.getItem('zunix_simulated_xp');
  if (savedXP !== null) {
    currentXP = parseInt(savedXP, 10) || 845;
  }

  updateDisplay(currentXP, false);

  // Wire buttons
  document.getElementById('btnDailyBonus')?.addEventListener('click', () => {
    addPoints(150, 'Daily Campus Check-in');
  });

  document.getElementById('btnPeerReview')?.addEventListener('click', () => {
    addPoints(250, 'Peer Code & Project Review');
  });

  document.getElementById('btnHackathon')?.addEventListener('click', () => {
    addPoints(500, 'Campus Hackathon Milestone');
  });

  document.getElementById('btnResetXP')?.addEventListener('click', () => {
    resetPoints();
  });
}

export function addPoints(amount, reason) {
  const oldRank = getRank(currentXP);
  const targetXP = currentXP + amount;
  currentXP = targetXP;
  localStorage.setItem('zunix_simulated_xp', currentXP);

  animateScore(targetXP);
  showScoreToast(amount, reason);

  const newRank = getRank(currentXP);
  if (newRank.name !== oldRank.name) {
    showLevelUpCelebration(newRank);
  }
}

export function resetPoints() {
  currentXP = 845;
  localStorage.setItem('zunix_simulated_xp', currentXP);
  updateDisplay(currentXP, true);
  showScoreToast(0, 'Progress reset to initial preview state');
}

function animateScore(target) {
  const scoreEl = document.getElementById('simScoreValue');
  if (!scoreEl) return;

  const start = parseInt(scoreEl.textContent.replace(/[^0-9]/g, ''), 10) || 0;
  const duration = 600;
  const startTime = performance.now();

  function step(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const easeOut = 1 - Math.pow(1 - progress, 3);
    const value = Math.floor(start + (target - start) * easeOut);

    scoreEl.textContent = value.toLocaleString();
    updateDisplay(value, false);

    if (progress < 1) {
      requestAnimationFrame(step);
    } else {
      scoreEl.textContent = target.toLocaleString();
      updateDisplay(target, true);
    }
  }

  requestAnimationFrame(step);
}

function updateDisplay(xp, updateScoreText = true) {
  const scoreEl = document.getElementById('simScoreValue');
  const rankBadgeEl = document.getElementById('simRankBadge');
  const progressBar = document.getElementById('simProgressFill');
  const nextTargetEl = document.getElementById('simNextTarget');

  if (scoreEl && updateScoreText) {
    scoreEl.textContent = xp.toLocaleString();
  }

  const rank = getRank(xp);
  if (rankBadgeEl) {
    rankBadgeEl.innerHTML = ;
    rankBadgeEl.style.borderColor = rank.color;
    rankBadgeEl.style.color = rank.color;
  }

  let pct = 100;
  if (rank.max !== Infinity) {
    const range = rank.max - rank.min;
    const progressIntoTier = xp - rank.min;
    pct = Math.min(Math.max((progressIntoTier / range) * 100, 5), 100);
  }

  if (progressBar) {
    progressBar.style.width = pct + '%';
    progressBar.style.backgroundColor = rank.color;
    progressBar.style.boxShadow = '0 0 15px ' + rank.color;
  }

  if (nextTargetEl) {
    if (rank.max === Infinity) {
      nextTargetEl.textContent = 'Maximum Zunix Pioneer Tier Reached!';
    } else {
      const remaining = rank.max + 1 - xp;
      nextTargetEl.textContent = remaining.toLocaleString() + ' ZP until next rank';
    }
  }
}

function showScoreToast(amount, reason) {
  const existing = document.getElementById('xp-toast');
  if (existing) existing.remove();

  const toast = document.createElement('div');
  toast.id = 'xp-toast';
  toast.className = 'zunix-toast';
  toast.style.borderColor = '#00ff99';
  toast.innerHTML = amount > 0 
    ? '<span>✨</span> <strong>+' + amount + ' ZP!</strong> ' + reason
    : '<span>ℹ️</span> ' + reason;

  document.body.appendChild(toast);

  setTimeout(() => {
    toast.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    setTimeout(() => toast.remove(), 400);
  }, 2500);
}

function showLevelUpCelebration(newRank) {
  const celebration = document.createElement('div');
  celebration.className = 'zunix-level-up-modal';
  celebration.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(10px);display:flex;align-items:center;justify-content:center;z-index:10000;padding:20px;';
  celebration.innerHTML = 
    '<div style="background:#111625;border:2px solid ' + newRank.color + ';box-shadow:0 0 50px ' + newRank.color + '66;border-radius:24px;padding:36px 28px;text-align:center;max-width:440px;width:100%;animation:toastSlideUp 0.4s ease;">' +
      '<div style="font-size:4.5rem;margin-bottom:12px;">' + newRank.badge + '</div>' +
      '<h2 style="color:' + newRank.color + ';margin:0 0 8px;font-size:1.8rem;letter-spacing:1px;">TIER UNLOCKED!</h2>' +
      '<h3 style="color:#fff;font-size:1.3rem;margin:0 0 12px;">' + newRank.name + '</h3>' +
      '<p style="color:#94a3b8;font-size:0.95rem;margin:0 0 24px;line-height:1.5;">' +
        'Outstanding achievement! Your active campus engagement has elevated your status in the Zunix ecosystem.' +
      '</p>' +
      '<button id="closeLevelUpBtn" style="background:' + newRank.color + ';color:#000;border:none;padding:12px 30px;border-radius:30px;font-weight:800;font-size:1rem;cursor:pointer;box-shadow:0 4px 15px rgba(0,0,0,0.4);">' +
        'Awesome, Keep Going!' +
      '</button>' +
    '</div>';
  document.body.appendChild(celebration);

  document.getElementById('closeLevelUpBtn')?.addEventListener('click', () => {
    celebration.remove();
  });
}

if (typeof window !== 'undefined') {
  window.ZunixRewards = { initRewardsSimulator, addPoints, resetPoints, getRank };
}

if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initRewardsSimulator);
  } else {
    initRewardsSimulator();
  }
}
