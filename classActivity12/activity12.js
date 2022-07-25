//   MODAL WINDOW
const openItem1 = document.querySelector(`#openItem1`)
const closeModal = document.querySelector(`#closeModal`)
const modalWindow = document.querySelector(`.modalWindow`)

openItem1.addEventListener(`click`, function() {
    modalWindow.style.display = `block`
})
closeModal.addEventListener(`click`, function () {
    modalWindow.style.display = `none`
})

//   STORAGE => FORMS
const firstName = document.querySelector(`#firstN`)
const lastName = document.querySelector(`#lastN`)
const submitForm = document.querySelector(`.input1`)

submitForm.addEventListener(`click`, function () {
    // LOCAL STORAGE STAYS WITHIN BROWSER
    localStorage.setItem(`FN`, firstName.value) //using "name's =" set to the input

    // SESSION STORAGE RESETS WHEN BROWASER IS CLOSED
    sessionStorage.setItem(`LN`, lastName.value)

    //   TO CLEAR TEXT BOX IN CASE USER GOES BACK USING BROWSER ARROWS
    firstName.value = ``
    lastName.value = ``
})
                                                                                                         VIEW PASSWORD
const myPassword = document.querySelector(`#myPassword`)
const viewPassword = document.querySelector(`#viewPassword`)

viewPassword.addEventListener(`click`, function () {
    // CONDITION  ?  EXPRESSION TO EXECUTE IF TRUE  :  EXPRESSION TO EXECUTE IF FLASE / NULL

    const secret = myPassword.getAttribute(`type`) === 'password' ? 'text' : 'password'
    myPassword.setAttribute(`type`, secret)
})

//   AUTOMATIC SLIDESHOW
const slidesAuto = document.querySelectorAll(`.slideAuto`)
let indexSlide = 0
slideshowAuto()

function slideshowAuto () {
    let numberSlides = slidesAuto.length
    if (indexSlide >= numberSlides) {indexSlide = 0}
    if (indexSlide < 0) {indexSlide = numberSlides -1}
    //hiding images, displaying first
    for (let eachIndex = 0; eachIndex < numberSlides; eachIndex++) {
        slidesAuto[eachIndex].style.display = `none`
    }
    slidesAuto[indexSlide].style.display = `block`

    setTimeout(slideshowAuto, 3000) //second * 1000. Keeps calling itself
    indexSlide++
}


//   SLIDESHOW
const slides = document.querySelectorAll(`.slide`)
const prev = document.querySelector(`.prev`)
const next = document.querySelector(`.next`)

let currentSlide = 1 //position
let numberSlides = slides.length
slideshow(currentSlide)


prev.addEventListener(`click`, function () {
    currentSlide--
    slideshow(currentSlide)
})
next.addEventListener(`click`, function () {
    currentSlide++
    slideshow(currentSlide)
})


function slideshow(n) {
    //setup slideshhow to loop
    if (currentSlide > numberSlides) {currentSlide = 1}
    if (currentSlide < 1) {currentSlide = numberSlides}
    //loop to hide all images
    for (let eachSlides = 0; eachSlides < numberSlides; eachSlides++) {
        slides[eachSlides].style.display = `none`
    }
    //set first image to show
    slides[currentSlide - 1].style.display = `block`
}