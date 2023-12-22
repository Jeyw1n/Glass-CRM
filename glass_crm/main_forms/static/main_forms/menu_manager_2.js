var invBlock = document.querySelector('.invBlock');
var toHideAndShow = document.querySelectorAll('.tohideandshow');
var menu = document.querySelector('.menu');

function openMenu() {
    toHideAndShow.forEach(function(element) {
        menu.classList.add('show');
        element.style.display = 'block';
    });
}

// Закрываем.
function handleClick() {
    toHideAndShow.forEach(function(element) {
        element.style.display = 'none';
        menu.classList.remove('show');
    });
}

invBlock.addEventListener('click', handleClick);