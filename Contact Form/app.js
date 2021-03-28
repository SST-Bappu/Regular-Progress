const form = document.getElementById("login")
const email = document.getElementById("emailAddress")
const pass = document.getElementById("password")
form.addEventListener('submit',(e)=>{
    e.preventDefault()
    checkInputs();
});
function checkInputs(){
    const usr_email = email.Value
    const usr_pass = pass.value

    if (usr_pass===""){
        alert("Enter Valid Password")
    }
    else{
        alert("Your password is = "+usr_pass)
    }
}