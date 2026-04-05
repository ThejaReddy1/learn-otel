/* ============================================
   progress.js — Day completion tracking (localStorage)
   ============================================ */

const STORAGE_KEY = 'otel-learning-progress';

function getProgress() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {};
  } catch {
    return {};
  }
}

function saveProgress(data) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
}

/* --- Initialize Checklists --- */
document.addEventListener('DOMContentLoaded', () => {
  initChecklists();
  updateSidebarProgress();
  updateProgressBar();
});

function initChecklists() {
  const progress = getProgress();
  
  document.querySelectorAll('.checklist-item input[type="checkbox"]').forEach(checkbox => {
    const id = checkbox.id;
    if (!id) return;
    
    // restore state
    if (progress[id]) {
      checkbox.checked = true;
    }
    
    checkbox.addEventListener('change', () => {
      const p = getProgress();
      if (checkbox.checked) {
        p[id] = true;
      } else {
        delete p[id];
      }
      saveProgress(p);
      updateSidebarProgress();
      updateProgressBar();
    });
  });
}

function updateSidebarProgress() {
  const progress = getProgress();
  
  document.querySelectorAll('.sidebar-link[data-day]').forEach(link => {
    const day = link.dataset.day;
    const checklistItems = document.querySelectorAll(
      `.checklist-item input[id^="day${day}-"]`
    );
    
    if (checklistItems.length === 0) return;
    
    const allChecked = Array.from(checklistItems).every(cb => progress[cb.id]);
    
    if (allChecked) {
      link.classList.add('completed');
    } else {
      link.classList.remove('completed');
    }
  });
}

function updateProgressBar() {
  const bar = document.querySelector('.progress-fill');
  const label = document.querySelector('.progress-count');
  if (!bar) return;
  
  const totalDays = 8;
  const progress = getProgress();
  
  // Count completed days (all checklists for a day are done)
  let completedDays = 0;
  for (let d = 0; d <= 7; d++) {
    const items = document.querySelectorAll(
      `.checklist-item input[id^="day${d}-"]`
    );
    if (items.length > 0 && Array.from(items).every(cb => progress[cb.id])) {
      completedDays++;
    }
  }
  
  const percent = Math.round((completedDays / totalDays) * 100);
  bar.style.width = percent + '%';
  if (label) label.textContent = `${completedDays}/${totalDays} days`;
}

/* --- Mark Day as Complete --- */
function markDayComplete(dayNumber) {
  const p = getProgress();
  p[`day-${dayNumber}-complete`] = true;
  saveProgress(p);
  updateSidebarProgress();
}
