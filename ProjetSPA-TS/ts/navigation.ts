const navButtons = document.querySelectorAll<HTMLButtonElement>('.nav-btn');
const sections = document.querySelectorAll<HTMLElement>('.app-section');

navButtons.forEach(button => {
    button.addEventListener('click', () => {
        const targetId = button.dataset.target;

        sections.forEach(section => {
            if (section.id === targetId) {
                section.hidden = false;
            } else {
                section.hidden = true;
            }
        });

        navButtons.forEach((btn) => btn.classList.remove("active"));
        button.classList.add("active");
    });
});