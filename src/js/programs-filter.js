// src/js/programs-filter.js — Live Search & Category Filtering for Zunix Programs

export function initProgramsFilter() {
  const searchInput = document.getElementById('programSearchInput');
  const filterPills = document.querySelectorAll('.prog-filter-pill');
  const programs = document.querySelectorAll('.zunix-program');
  const countDisplay = document.getElementById('programCountBadge');

  if (!searchInput && filterPills.length === 0) return;

  let activeCategory = 'all';
  let searchTerm = '';

  function applyFilters() {
    let visibleCount = 0;

    programs.forEach(prog => {
      const text = prog.textContent.toLowerCase();
      const progCategory = prog.getAttribute('data-category') || 'all';

      const matchesSearch = !searchTerm || text.includes(searchTerm);
      const matchesCategory = activeCategory === 'all' || progCategory === activeCategory || progCategory.includes(activeCategory);

      if (matchesSearch && matchesCategory) {
        prog.style.display = 'block';
        prog.style.animation = 'fadeIn 0.3s ease';
        visibleCount++;
      } else {
        prog.style.display = 'none';
      }
    });

    if (countDisplay) {
      countDisplay.textContent = `Showing ${visibleCount} of ${programs.length} programs`;
    }
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchTerm = e.target.value.toLowerCase().trim();
      applyFilters();
    });
  }

  filterPills.forEach(pill => {
    pill.addEventListener('click', (e) => {
      e.preventDefault();
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeCategory = pill.getAttribute('data-filter') || 'all';
      applyFilters();
    });
  });

  applyFilters();
}

if (typeof window !== 'undefined') {
  window.ZunixPrograms = { initProgramsFilter };
}

if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initProgramsFilter);
  } else {
    initProgramsFilter();
  }
}
