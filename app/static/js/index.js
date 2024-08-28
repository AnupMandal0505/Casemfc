// index.js (Create this file if you haven't already)

document.addEventListener("DOMContentLoaded", function () {
    const fadeInElements = document.querySelectorAll('.fade-in');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
            }
        });
    }, {
        threshold: 0.1 // Adjust this value based on when you want the animation to trigger
    });

    fadeInElements.forEach(el => {
        observer.observe(el);
    });
});
