var updateBtns = document.getElementsByClassName('update-cart')

for(var i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',cartInfo)

    console.log('USER : ',this.dataset.user)
    if (this.dataset.user == 'AnonymousUser'){
        console.log('User is not Authenticated')
    }
    else{
        console.log('User is authenticated, sending data....')
    }
}

function cartInfo(){
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('productId:',productId, 'action:',action)
}