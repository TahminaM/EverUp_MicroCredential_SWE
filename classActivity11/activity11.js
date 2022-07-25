// ex 2:
const btn2 = document.querySelector('#btn2')
btn2.onclick = function(){
    alert('Hi there!')
}

/* another way to create the event
function clickBtn(){
    alert('Hi there!')
}
btn2.onclick = clickBtn */


// ex 3:
const qccLink = document.querySelector('#qccLink')
qccLink.onclick = function(){
    console.log('QCClink was clicked!')
}

qccLink.onmouseover = testing;

function testing(){
    console.log('QCC link was hovered or mouseover!')
}


// ex 4:
const title = document.querySelector('.title')
title.onmouseover = function(){
    console.log('The title was hovered on mouseout event')
}


// ex 5:
const btn5 = document.querySelector('#btn5')
btn5.addEventListener('click', function(){
    alert('Button 5 was clicked!')
})


// ex 6:
const btn6 = document.querySelector('#btn6')
btn6.addEventListener('mouseout', click1)
btn6.addEventListener('dblclick', click2)

function click1(){
    console.log('Button 6 = mouseout')
}

function click2(){
    alert('Button 6 was double clicked')
}


// ex 7:
const colorContainer = document.querySelector('.colorContainer')
const btnColor = document.querySelector('#btnColor')

btnColor.addEventListener('click', function(){
    // change background color of the <div>
    colorContainer.style.backgroundColor = changeColor();
})

function changeColor(){
    // rgb values goes from 0 - 255
    const r = Math.floor(Math.random()*256)
    const g = Math.floor(Math.random()*256)
    const b = Math.floor(Math.random()*256)
    return `rgb(${r}, ${g}, ${b})`
}


// ex 9:
const divColor = document.querySelectorAll('.divColor')
for(let eachDiv of divColor){
    eachDiv.addEventListener('mouseout', function(){
        eachDiv.style.backgroundColor = changeColor();
    })
}


// ex 10:
const inputTxt = document.querySelector('.inputTxt')
inputTxt.addEventListener('keydown', function(e){
    alert(`Keydown! key "${e.key}" was pressed \nThe ASCII code for key "${e.key}" is ${e.which}`)
})


// ex 11:
const display9 = document.querySelector('.display9')
window.addEventListener('scroll', function(){
    let pxTop = window.pageYOffset;
    display9.innerHTML = `Browser window is ${pxTop}px away from the top`
})


// ex 12:
const toTop = document.querySelector('.toTop')
window.addEventListener('scroll', function(){
    let pxTop = window.pageYOffset;
    if(pxTop>80){
        toTop.style.display = 'block';
    }
    else{
        toTop.style.display = 'none';
    }
})


// ex 13:
const qccURL = document.querySelector('#qccURL')
qccURL.addEventListener('click', function(e){
    e.preventDefault();
    alert('QCC website is off!')
})


// ex 14: 
const sBubble = document.querySelector('.sBubble')
const pBubble = document.querySelector('.pBubble')
const aBubble = document.querySelector('.aBubble')
sBubble.addEventListener('click', function(){
    alert('Section was clicked')
})
pBubble.addEventListener('click', function(e){
    e.stopPropagation()   
    alert('Paragraph was clicked')
})
aBubble.addEventListener('click', function(e){
    e.stopPropagation()
    alert('Anchor was clicked')
})