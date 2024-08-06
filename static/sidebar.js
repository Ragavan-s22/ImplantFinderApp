document.addEventListener('DOMContentLoaded', () => {
    const menuButton = document.getElementById('menu-button');
    const sidebar = document.querySelector('ul');

    menuButton.addEventListener('click', () => {
        sidebar.classList.toggle('open');
    });
});
