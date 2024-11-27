const darkModeToggle = document.getElementById('dark-mode-toggle');
const toggleIcon = document.getElementById('toggle-icon');

darkModeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark');
    if (document.body.classList.contains('dark')) {
        toggleIcon.classList.replace('fa-lightbulb', 'fa-lightbulb-o');
    } else {
        toggleIcon.classList.replace('fa-lightbulb-o', 'fa-lightbulb');
    }
});
