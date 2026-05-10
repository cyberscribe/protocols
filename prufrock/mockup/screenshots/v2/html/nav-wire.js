// Prufrock Protocol — shared navigation wiring for screencast demo

const NAV_ROUTES = {
  'Timeline':    '01-seed-panel.html',
  'Lineage':     '05-lineage-path.html',
  'Map':         '06-map-full.html',
  'Poem':        '07-poem-sidebyside.html',
  'Participant': '08-participant.html',
  'Concerns':    '10-concerns-network.html',
};

const VIEW_ROUTES = {
  'Theme river':    null,
  'Theme network':  '10-concerns-network.html',
  'Long view':      '11-long-view.html',
  'Deep Time':      '12b-deep-time.html',
};

const POEM_ROUTES = {
  '2026 ↔ 2126':      '07-poem-sidebyside.html',
  'Chain of Attention': '12b-deep-time.html',
  'The Inheritance':    '12c-handoff.html',
};

document.addEventListener('DOMContentLoaded', () => {

  // Nav tabs
  document.querySelectorAll('.nav-tab').forEach(tab => {
    const label = tab.textContent.trim();
    const route = NAV_ROUTES[label];
    if (route && !tab.classList.contains('active')) {
      tab.addEventListener('click', () => location.href = route);
    }
  });

  // Cohort buttons — toggle active class only
  document.querySelectorAll('.cohort-btns').forEach(grp => {
    grp.querySelectorAll('.cbt').forEach(btn => {
      btn.addEventListener('click', () => {
        grp.querySelectorAll('.cbt').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      });
    });
  });

  // Era buttons (07) — toggle active class
  document.querySelectorAll('.era-btns').forEach(grp => {
    grp.querySelectorAll('.ebt').forEach(btn => {
      btn.addEventListener('click', () => {
        grp.querySelectorAll('.ebt').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      });
    });
  });

  // View buttons (Concerns sub-views) — navigate when not active
  document.querySelectorAll('.view-btns').forEach(grp => {
    grp.querySelectorAll('.vbt').forEach(btn => {
      const label = btn.textContent.trim();
      const route = VIEW_ROUTES[label];
      if (route && !btn.classList.contains('active')) {
        btn.addEventListener('click', () => location.href = route);
      }
    });
  });

  // Poem sub-nav buttons
  document.querySelectorAll('.poem-sub-btns').forEach(grp => {
    grp.querySelectorAll('.psbt').forEach(btn => {
      const label = btn.textContent.trim();
      const route = POEM_ROUTES[label];
      if (route && !btn.classList.contains('active')) {
        btn.addEventListener('click', () => location.href = route);
      }
    });
  });

  // Begin Experiment button (01)
  const beginBtn = document.querySelector('.begin-btn');
  if (beginBtn) beginBtn.addEventListener('click', () => location.href = '06-map-full.html');

});
