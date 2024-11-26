// Dark Mode Toggle
document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("dark-mode-toggle");
    toggle.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");
    });
});
