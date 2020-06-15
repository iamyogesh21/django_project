// preloder start
var preloder = document.getElementById('preloder')

function show() {
    preloder.style.display = 'none';
}
// preloder end

// game trailer started
function toggle() {
    var trailer = document.querySelector('#onetra');
    var video = document.querySelector('video');
    onetra.classList.toggle('active')
    video.currentTime = 0;
    video.pause();
}

function toggletwo() {
    var trailer = document.querySelector('#twotra');
    var video = document.querySelector('video');
    twotra.classList.toggle('active')
    video.currentTime = 0;
    video.pause();
}

function togglethree() {
    var trailer = document.querySelector('#threetra');
    var video = document.querySelector('video');
    threetra.classList.toggle('active')
    video.currentTime = 0;
    video.pause();
}
// game trailer end

$(function($) {
    $(document).on('click', '.box-btn', function(event) {
        $(this).find('.icon').toggleClass('red').toggleClass('icon-heart-o icon-heart');
    });
});
var updateBtns = document.getElementsByClassName('update-cart')


for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)
    });

}
console.log('hello')