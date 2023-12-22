var openMenu = document.getElementById('open-menu');
var invBlock = document.querySelector('.invBlock');
var toHideAndShow = document.querySelectorAll('.tohideandshow');
var menu = document.querySelector('.menu');

var timeout;

let touchstartX = 0
let touchendX = 0

// Открыть, если навестись курсором мыши.
function handleMouseOver() {
    timeout = setTimeout(function() {
        toHideAndShow.forEach(function(element) {
            menu.classList.add('show');
            element.style.display = 'block';
        });
    }, 128);
}
function handleMouseOut() {
    clearTimeout(timeout);
}


// Открыть свайпом на телефоне.
function checkDirection() {
  const threshold = 100; // Минимальная длина свайпа для открытия меню
  const maxWidth = 767; // Максимальная ширина экрана для определения мобильного устройства

  if (window.innerWidth <= maxWidth && touchendX > touchstartX && (touchendX - touchstartX) > threshold) {
    toHideAndShow.forEach(function(element) {
      element.style.display = 'block';
      menu.classList.add('show');
    });
  }
}


// Закрываем.
function handleClick() {
    toHideAndShow.forEach(function(element) {
        element.style.display = 'none';
        menu.classList.remove('show');
    });
}
openMenu.addEventListener('mouseover', handleMouseOver);
invBlock.addEventListener('click', handleClick);
document.addEventListener('touchstart', e => {
  touchstartX = e.changedTouches[0].screenX
})
document.addEventListener('touchend', e => {
  touchendX = e.changedTouches[0].screenX;

  const scrolledElement = e.target.closest('table'); // Здесь '.scrollable' должен быть заменен на селектор прокручиваемых элементов

  if (touchendX !== touchstartX && !scrolledElement) {
    checkDirection();
  }
});
