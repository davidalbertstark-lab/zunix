// src/js/card-generator.js — Dynamic Student ID Card Generator, 3D Tilt & Canvas PNG Export

export function initCardGenerator() {
  setupTiltEffect();
  setupCanvasDownload();
  loadSavedProfile();
}

// Interactive 3D Card Tilt
function setupTiltEffect() {
  const card = document.getElementById('previewCard');
  if (!card) return;

  card.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    const rotateX = (-y / (rect.height / 2)) * 12;
    const rotateY = (x / (rect.width / 2)) * 12;

    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
  });

  card.addEventListener('mouseleave', () => {
    card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
  });
}

// Download High-Resolution Student ID Badge as PNG
function setupCanvasDownload() {
  const downloadBtn = document.getElementById('downloadCardBtn');
  if (!downloadBtn) return;

  downloadBtn.addEventListener('click', async () => {
    const originalText = downloadBtn.innerHTML;
    downloadBtn.innerHTML = '<span>⏳</span> Generating Badge...';
    downloadBtn.disabled = true;

    try {
      await exportCardAsPng();
    } catch (err) {
      console.error('Failed to export card PNG:', err);
      alert('Could not export image. Printing dialog opened instead.');
      window.print();
    } finally {
      downloadBtn.innerHTML = originalText;
      downloadBtn.disabled = false;
    }
  });
}

async function exportCardAsPng() {
  const canvas = document.createElement('canvas');
  const width = 800;
  const height = 1100;
  canvas.width = width;
  canvas.height = height;
  const ctx = canvas.getContext('2d');

  // Background gradient (cyber dark obsidian)
  const bgGrad = ctx.createLinearGradient(0, 0, width, height);
  bgGrad.addColorStop(0, '#0a0d14');
  bgGrad.addColorStop(0.5, '#111625');
  bgGrad.addColorStop(1, '#06130e');
  ctx.fillStyle = bgGrad;
  ctx.fillRect(0, 0, width, height);

  // Outer glowing border
  ctx.strokeStyle = '#00ff99';
  ctx.lineWidth = 6;
  ctx.strokeRect(20, 20, width - 40, height - 40);

  ctx.strokeStyle = 'rgba(0, 240, 255, 0.4)';
  ctx.lineWidth = 2;
  ctx.strokeRect(32, 32, width - 64, height - 64);

  // Top Verified Badge
  ctx.fillStyle = '#00ff99';
  ctx.font = 'bold 22px "Poppins", sans-serif';
  ctx.textAlign = 'center';
  ctx.fillText('★ VERIFIED STUDENT IDENTITY ★', width / 2, 80);

  // ID Tag
  const idTag = document.getElementById('cardIdTag')?.textContent || 'ID: ZUN-2025-0042';
  ctx.fillStyle = '#00f0ff';
  ctx.font = 'bold 24px monospace';
  ctx.fillText(idTag, width / 2, 120);

  // Brand Name
  ctx.fillStyle = '#ffffff';
  ctx.font = '900 42px "Poppins", sans-serif';
  ctx.fillText('ZUNIX OFFICIAL ID', width / 2, 180);

  // Subtitle
  ctx.fillStyle = '#94a3b8';
  ctx.font = '18px "Poppins", sans-serif';
  ctx.fillText('Official Digital Campus Credential', width / 2, 215);

  // Student Avatar
  const avatarImg = document.getElementById('cardAvatar');
  const avatarSize = 220;
  const avatarX = (width - avatarSize) / 2;
  const avatarY = 250;

  // Draw avatar circle border
  ctx.save();
  ctx.beginPath();
  ctx.arc(width / 2, avatarY + avatarSize / 2, avatarSize / 2, 0, Math.PI * 2);
  ctx.closePath();
  ctx.clip();

  if (avatarImg && avatarImg.complete) {
    try {
      ctx.drawImage(avatarImg, avatarX, avatarY, avatarSize, avatarSize);
    } catch (e) {
      // Fallback if cross-origin
      ctx.fillStyle = '#1e293b';
      ctx.fillRect(avatarX, avatarY, avatarSize, avatarSize);
    }
  } else {
    ctx.fillStyle = '#1e293b';
    ctx.fillRect(avatarX, avatarY, avatarSize, avatarSize);
  }
  ctx.restore();

  // Avatar Ring
  ctx.strokeStyle = '#00ff99';
  ctx.lineWidth = 6;
  ctx.beginPath();
  ctx.arc(width / 2, avatarY + avatarSize / 2, (avatarSize / 2) + 2, 0, Math.PI * 2);
  ctx.stroke();

  // Details Box
  const startY = 530;
  const lineHeight = 55;
  const name = document.getElementById('cardName')?.textContent || 'Student Name';
  const uname = document.getElementById('cardUsername')?.textContent || '@student';
  const inst = document.getElementById('cardInstitution')?.textContent || 'University';
  const course = document.getElementById('cardCourse')?.textContent || 'Course';
  const level = document.getElementById('cardLevel')?.textContent || 'Level';

  const rows = [
    { label: 'Full Name:', val: name },
    { label: 'Username:', val: uname },
    { label: 'Institution:', val: inst },
    { label: 'Course of Study:', val: course },
    { label: 'Current Level:', val: level }
  ];

  rows.forEach((row, i) => {
    const y = startY + (i * lineHeight);

    // Subtle row background
    ctx.fillStyle = i % 2 === 0 ? 'rgba(255, 255, 255, 0.03)' : 'rgba(0, 0, 0, 0.2)';
    ctx.fillRect(80, y - 35, width - 160, 48);

    ctx.textAlign = 'left';
    ctx.fillStyle = '#94a3b8';
    ctx.font = '600 22px "Poppins", sans-serif';
    ctx.fillText(row.label, 100, y);

    ctx.textAlign = 'right';
    ctx.fillStyle = '#f0f6fc';
    ctx.font = 'bold 24px "Poppins", sans-serif';
    ctx.fillText(row.val, width - 100, y);
  });

  // Simulated Barcode / Secure Seal at bottom
  const sealY = startY + (rows.length * lineHeight) + 60;
  ctx.strokeStyle = '#00f0ff';
  ctx.lineWidth = 2;
  ctx.strokeRect(80, sealY, width - 160, 90);

  ctx.fillStyle = '#00ff99';
  ctx.font = 'bold 18px monospace';
  ctx.textAlign = 'center';
  ctx.fillText('SECURITY HASH: 9F8A-38DE-ZUNX-2025-VALID', width / 2, sealY + 38);

  ctx.fillStyle = '#64748b';
  ctx.font = '16px "Poppins", sans-serif';
  ctx.fillText('Issued by Zunix Digital Trust Network • zunix.africa', width / 2, sealY + 68);

  // Trigger Download
  const link = document.createElement('a');
  link.download = `zunix-id-${name.toLowerCase().replace(/[^a-z0-9]/g, '-')}.png`;
  link.href = canvas.toDataURL('image/png');
  link.click();
}

function loadSavedProfile() {
  try {
    const saved = JSON.parse(localStorage.getItem('zunix_student_profile') || '{}');
    if (saved.fullName && document.getElementById('inputName')) {
      document.getElementById('inputName').value = saved.fullName;
    }
    if (saved.username && document.getElementById('inputUsername')) {
      document.getElementById('inputUsername').value = saved.username;
    }
    if (saved.institution && document.getElementById('inputInstitution')) {
      document.getElementById('inputInstitution').value = saved.institution;
    }
    if (saved.course && document.getElementById('inputCourse')) {
      document.getElementById('inputCourse').value = saved.course;
    }
  } catch (e) {}
}

if (typeof window !== 'undefined') {
  window.ZunixCard = { initCardGenerator, exportCardAsPng };
}

if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCardGenerator);
  } else {
    initCardGenerator();
  }
}
