// ======== THEME TOGGLE ========
const toggle = document.getElementById('themeToggle');
const saved = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-theme', saved);
toggle.addEventListener('click', () => {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
});

// ======== MOBILE MENU ========
const hamburger = document.querySelector('.hamburger');
const navLinks  = document.querySelector('.nav-links');
hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('open');
});

// ======== DYNAMIC YEAR IN FOOTER ========
document.getElementById('year').textContent = new Date().getFullYear();

// ======== SMOOTH SCROLL FOR CTA BUTTONS (OPTIONAL ENHANCEMENT) ========
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
});s