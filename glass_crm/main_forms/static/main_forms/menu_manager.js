var openMenu = document.getElementById('open-menu');
var invBlock = document.querySelector('.inv_block');
var toHideAndShow = document.querySelectorAll('.tohideandshow');


function handleMouseOver() {
    toHideAndShow.forEach(function(element) {
        element.style.display = 'block';
    });
}

function handleClick() {
    toHideAndShow.forEach(function(element) {
        element.style.display = 'none';
    });
}
openMenu.addEventListener('mouseover', handleMouseOver);
invBlock.addEventListener('click', handleClick);
