/* ============================================
   main.js — Navigation, sidebar, scroll animations
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
  initSidebar();
  initScrollAnimations();
  initCollapsibles();
  initCodeCopy();
  highlightActiveNav();
  generateTableOfContents();
});

/* --- Sidebar Toggle (Mobile) --- */
function initSidebar() {
  const toggle = document.querySelector('.menu-toggle');
  const sidebar = document.querySelector('.sidebar');
  const overlay = document.querySelector('.sidebar-overlay');

  if (!toggle || !sidebar) return;

  toggle.addEventListener('click', () => {
    sidebar.classList.toggle('open');
    if (overlay) overlay.classList.toggle('active');
  });

  if (overlay) {
    overlay.addEventListener('click', () => {
      sidebar.classList.remove('open');
      overlay.classList.remove('active');
    });
  }
}

/* --- Scroll-triggered Animations --- */
function initScrollAnimations() {
  const elements = document.querySelectorAll('.animate-on-scroll');
  if (!elements.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, index * 80);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  elements.forEach(el => observer.observe(el));
}

/* --- Collapsible Sections --- */
function initCollapsibles() {
  document.querySelectorAll('.collapsible-trigger').forEach(trigger => {
    trigger.addEventListener('click', () => {
      const parent = trigger.closest('.collapsible');
      parent.classList.toggle('open');
    });
  });
}

/* --- Code Copy Buttons --- */
function initCodeCopy() {
  document.querySelectorAll('.code-copy-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const block = btn.closest('.code-block');
      const code = block.querySelector('pre').textContent;
      navigator.clipboard.writeText(code).then(() => {
        btn.textContent = '✓ Copied';
        btn.classList.add('copied');
        setTimeout(() => {
          btn.textContent = 'Copy';
          btn.classList.remove('copied');
        }, 2000);
      });
    });
  });
}

/* --- Highlight Active Page in Nav --- */
function highlightActiveNav() {
  const path = window.location.pathname.split('/').pop() || 'index.html';
  
  document.querySelectorAll('.sidebar-link, .header-nav a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === path || (path === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });
}

/* --- Dynamic Table of Contents for Active Day --- */
function generateTableOfContents() {
  const activeLink = document.querySelector('.sidebar-link.active');
  if (!activeLink) return;

  const headings = document.querySelectorAll('.content h2[id]');
  if (headings.length === 0) return;

  const sublinksContainer = document.createElement('div');
  sublinksContainer.className = 'sidebar-sublinks';

  headings.forEach(h2 => {
    // Skip checklist reading and learning outcomes because they are generic
    if (h2.id === 'checklist' || h2.id === 'learning-outcomes') return;

    const link = document.createElement('a');
    link.href = `#${h2.id}`;
    link.className = 'sidebar-sublink';
    
    // clean up module prefix if any
    let text = h2.textContent.replace(/^Module:\s*/i, '');
    link.textContent = text;
    sublinksContainer.appendChild(link);
  });

  // Only append if we found meaningful headings
  if (sublinksContainer.children.length > 0) {
    activeLink.insertAdjacentElement('afterend', sublinksContainer);
  }
}
