// Mobile menu toggle
const menuToggle = document.querySelector('.menu-toggle');
const navList = document.querySelector('.nav-list');

menuToggle.addEventListener('click', () => {
    navList.classList.toggle('active');
    menuToggle.classList.toggle('active');
});

// Close menu when clicking a link
navList.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
        navList.classList.remove('active');
        menuToggle.classList.remove('active');
    });
});

// Optional: Close menu when clicking outside
document.addEventListener('click', (e) => {
    if (!e.target.closest('.nav') && navList.classList.contains('active')) {
        navList.classList.remove('active');
        menuToggle.classList.remove('active');
    }
});