document.addEventListener('DOMContentLoaded', function() {
    const pictures = document.querySelectorAll('.picture');
    const overlay = document.getElementById('overlay');
    const overlayImg = document.getElementById('overlayImg');

    pictures.forEach(picture => {
        picture.addEventListener('click', function() {
            overlayImg.src = this.src;
            overlay.style.display = 'flex';
        });
    });

    overlay.addEventListener('click', function() {
        overlay.style.display = 'none';
    });
});

function toggleMobileMenu() {
    var menuList = document.querySelector('.mobile-menu-list');
    menuList.classList.toggle('active');
}

function hideMobileMenu() {
    var menuList = document.querySelector('.mobile-menu-list');
    menuList.classList.remove('active');
}

//additional begins
// Close menu when clicking outside
document.addEventListener('click', function (event) {
    var menuList = document.querySelector('.mobile-menu-list');
    var menuIcon = document.querySelector('.menu-icon');
    if (
        menuList.classList.contains('active') &&
        !menuList.contains(event.target) &&
        !menuIcon.contains(event.target)
    ) {
        hideMobileMenu();
    }
});

// Close menu on Escape key press
document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
        hideMobileMenu();
    }
});

//additioanl ends
