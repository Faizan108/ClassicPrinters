"use strict"


const carouselButtons = document.querySelectorAll(".carousel-btn");
const carouselButtonLeft = document.querySelector(".btn-left");
const carouselButtonRight = document.querySelector(".btn-right");
const carouselButtonLeft1 = document.querySelector(".btn-left1");
const carouselButtonRight1 = document.querySelector(".btn-right1");
const carouselButtonLeft2 = document.querySelector(".btn-left2");
const carouselButtonRight2 = document.querySelector(".btn-right2");
const carouselButtonLeft3 = document.querySelector(".btn-left3");
const carouselButtonRight3 = document.querySelector(".btn-right3");
const carouselImage1 = document.querySelector(".carousel-image-1");
const carouselImage2 = document.querySelector(".carousel-image-2");
const carouselImage3 = document.querySelector(".carousel-image-3");
const carouselImage1_1 = document.querySelector(".carousel-image-1_1");
const carouselImage2_1 = document.querySelector(".carousel-image-2_1");
const carouselImage4 = document.querySelector(".carousel-image-4");
const carouselImage5 = document.querySelector(".carousel-image-5");
const carouselImage6 = document.querySelector(".carousel-image-6");
const carouselImage4_1 = document.querySelector(".carousel-image-4_1");
const carouselImage5_1 = document.querySelector(".carousel-image-5_1");
const carouselImage7 = document.querySelector(".carousel-image-7");
const carouselImage8 = document.querySelector(".carousel-image-8");
const carouselImage9 = document.querySelector(".carousel-image-9");
const carouselImage7_1 = document.querySelector(".carousel-image-7_1");
const carouselImage8_1 = document.querySelector(".carousel-image-8_1");
const carouselImage10 = document.querySelector(".carousel-image-10");
const carouselImage11= document.querySelector(".carousel-image-11");
const carouselImage12= document.querySelector(".carousel-image-12");
const numberOfImages = document.querySelectorAll(".carousel-image").length;
let imageIndex = 1;
let translateX = 0;

carouselButtonLeft.addEventListener("click", slideLeft);
carouselButtonRight.addEventListener("click", slideRight);
carouselButtonLeft1.addEventListener("click", slideLeft1);
carouselButtonRight1.addEventListener("click", slideRight2);
carouselButtonLeft2.addEventListener("click", slideLeft3);
carouselButtonRight2.addEventListener("click", slideRight3);
carouselButtonLeft3.addEventListener("click", slideLeft4);
carouselButtonRight3.addEventListener("click", slideRight4);

function slideLeft(){
    if (imageIndex !== 1){
        imageIndex--;
        translateX += 700;
        carouselImage1.style.transform = `translateX(${translateX}px)`;
        carouselImage2.style.transform = `translateX(${translateX}px)`;
        carouselImage3.style.transform = `translateX(${translateX}px)`;
        carouselImage1_1.style.transform = `translateX(${translateX}px)`;
        carouselImage2_1.style.transform = `translateX(${translateX}px)`;
    }
    
}
function slideLeft1(){
    if (imageIndex !== 1){
        imageIndex--;
        translateX += 650;
        carouselImage4.style.transform = `translateX(${translateX}px)`;
        carouselImage5.style.transform = `translateX(${translateX}px)`;
        carouselImage6.style.transform = `translateX(${translateX}px)`;
        carouselImage4_1.style.transform = `translateX(${translateX}px)`;
        carouselImage5_1.style.transform = `translateX(${translateX}px)`;
    }
    
}
function slideLeft3(){
    if (imageIndex !== 1){
        imageIndex--;
        translateX += 939;
        carouselImage7.style.transform = `translateX(${translateX}px)`;
        carouselImage8.style.transform = `translateX(${translateX}px)`;
        carouselImage9.style.transform = `translateX(${translateX}px)`;
        carouselImage7_1.style.transform = `translateX(${translateX}px)`;
        carouselImage8_1.style.transform = `translateX(${translateX}px)`;
    }
    
}
function slideLeft4(){
    if (imageIndex !== 1){
        imageIndex--;
        translateX += 700;
        carouselImage10.style.transform = `translateX(${translateX}px)`;
        carouselImage11.style.transform = `translateX(${translateX}px)`;
        carouselImage12.style.transform = `translateX(${translateX}px)`;
    }
    
}

function slideRight(){
    if (imageIndex !== 5){
        imageIndex++;
        translateX -= 700;
        carouselImage1.style.transform = `translateX(${translateX}px)`;
        carouselImage2.style.transform = `translateX(${translateX}px)`;
        carouselImage3.style.transform = `translateX(${translateX}px)`;
        carouselImage1_1.style.transform = `translateX(${translateX}px)`;
        carouselImage2_1.style.transform = `translateX(${translateX}px)`;
    }
    
}

function slideRight2(){
    if (imageIndex !== 5){
        imageIndex++;
        translateX -= 650;
        carouselImage4.style.transform = `translateX(${translateX}px)`;
        carouselImage5.style.transform = `translateX(${translateX}px)`;
        carouselImage6.style.transform = `translateX(${translateX}px)`;
        carouselImage4_1.style.transform = `translateX(${translateX}px)`;
        carouselImage5_1.style.transform = `translateX(${translateX}px)`;
    }
    
}
function slideRight3(){
    if (imageIndex !== 5){
        imageIndex++;
        translateX -= 939;
        carouselImage7.style.transform = `translateX(${translateX}px)`;
        carouselImage8.style.transform = `translateX(${translateX}px)`;
        carouselImage9.style.transform = `translateX(${translateX}px)`;
        carouselImage7_1.style.transform = `translateX(${translateX}px)`;
        carouselImage8_1.style.transform = `translateX(${translateX}px)`;
    }
    
}
function slideRight4(){
    if (imageIndex !== 3){
        imageIndex++;
        translateX -= 700;
        carouselImage10.style.transform = `translateX(${translateX}px)`;
        carouselImage11.style.transform = `translateX(${translateX}px)`;
        carouselImage12.style.transform = `translateX(${translateX}px)`;
    }
    
}
var counter=1;
setInterval(function(){
    document.getElementById('radio'+counter).checked=true;
    counter++;
    
    if(counter>5)
    {
        counter=1;
    }
    document.querySelector('.radio').addEventListener('click',function(event){
        let id1=event.target.id;
        counter=parseInt(id1[id1.length-1]);
    });
},2000)

window.onscroll = function() {myFunction()};
var navbar = document.getElementById("navbar2");
var head=document.getElementById("first-head");
var sticky = navbar.offsetTop;
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky");
    head.classList.add("sticky2");
  } else {
    navbar.classList.remove("sticky");
    head.classList.remove("sticky2");
  }
}