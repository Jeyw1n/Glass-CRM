const container = document.querySelector('.table-container');
const resizeHandle = document.querySelector('.resize-handle');

let isResizing = false;
let startY = 0;

resizeHandle.addEventListener('mousedown', startResize);
resizeHandle.addEventListener('touchstart', startResize);

function startResize(e) {
    e.preventDefault();
    isResizing = true;
    startY = e.clientY || e.touches[0].clientY;
}

document.addEventListener('mousemove', resize);
document.addEventListener('touchmove', resize);

function resize(e) {
    if (!isResizing) return;

    const newY = e.clientY || e.touches[0].clientY;
    const deltaY = newY - startY;
    const newHeight = container.offsetHeight + deltaY;

    container.style.height = `${newHeight}px`;
    startY = newY;
}

document.addEventListener('mouseup', stopResize);
document.addEventListener('touchend', stopResize);

function stopResize() {
    isResizing = false;
}