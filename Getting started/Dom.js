console.log(window)
//Single element
const form=document.getElementById('my-form')
console.log(form)
console.log(document.querySelector('.container'))

//Multiple Element

console.log(document.querySelectorAll('.item'))
console.log(document.getElementsByClassName('item'))

//looping through
const items = document.querySelectorAll('.item')
items.forEach(function(item){
    console.log(item)
})
//or
//items.forEach((item)=> console.log(item))

const ul = document.querySelector('.items')
//ul.remove() //Completely remove ul items from web page
//ul.lastElementChild.remove() //remove the last ul item
//ul.firstElementChild.textContent='Hello' //Change the first element 'item 2' to 'Hello'
//ul.children[1].innerText = 'Brad' //For changing second one
//ul.lastElementChild.innerHTML='<h1>World</h1>' //For changin the last one

const btn = document.querySelector('.btn')
btn.style.background ='red' // We can change and add anything we want

//btn.addEventListener('click',(e)=>{ //Here instead of "click", if we put "mouseover" or "mouseout" then changes will take place when mouse goes over and when we put mouse out respectively.
  //  e.preventDefault()
    //console.log(e.target.className)
    //document.querySelector('#my-form').style.background='#ccc' //It changes the form background color
    //document.querySelector('body').classList.add('bg-dark') //It changes the body and form background after click
    //document.querySelector('.items').lastElementChild.innerHTML='<h1>Clicked</h1>' //It changes the ul item after click
//})

const FormItems = document.querySelector('#my-form')
const nameInput = document.querySelector('#name')
const emailInput = document.querySelector('#email')
const msg = document.querySelector('.msg')
const userList = document.querySelector('#users')
FormItems.addEventListener('submit',onsubmit)
function onsubmit(e){
    e.preventDefault()
    if(nameInput.value==='' || emailInput.value===''){
        //alert('Please enter all the fields')
        msg.classList.add('error')
        msg.innerHTML='Please enter all the fields'
        setTimeout(()=>msg.remove(),3000)
    }else{
        //console.log('Success')
        const li = document.createElement('li')
        li.appendChild(document.createTextNode(`${nameInput.value} : ${emailInput.value}`))
        userList.appendChild(li) 
        //clear fields
        nameInput.value=""
        emailInput.value=""
    }
}