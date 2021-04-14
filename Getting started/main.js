//var,let,const
//String, NUmbers, BOolean, null, undefined
const name = 'John'
const age = 30
//Concatenation
const hello = 'My name is '+name+ ' and I am '+ age
console.log(`My name is ${name} and I am ${age}`)
//const hello = "Hello World"
const s = 'technology, computer, it, coding, programming, life'
console.log(s.split(', '))
var x = 123
console.log((100+23).toString())

const numbers = ['apple','orrenges','car','bus',1,2,3,4,5]
numbers.push('mangos')
numbers.unshift('Grapes')
numbers.pop()
console.log(numbers)
const person ={
    firstName: "John",
    lastName: "Doe",
    age:30,
    hobbies: ['music','movies','sports'],
    address:{
        street:'50 main st',
        city:'Boston',
        state:'MA'
    }
}
person.email = "john@gmail.com"
console.log(person)
console.log(person.firstName, person.lastName)
console.log(person.address.street)
const {firstName,lastName, address: {city} } = person
console.log(firstName, lastName,city)

const todos=[
    {
        id:1,
        text: 'Take out trash',
        isCompleted: true
    },
    {
        id:2,
        text:"Meeting with Boss",
        isCompleted:true
    },
    {
        id:3,
        text:"Dentist appointment",
        isCompleted:false
    }
]
console.log(todos[1])
const todoJSON = JSON.stringify(todos)
console.log(todoJSON)

//Loops
for (key in person){
    console.log(person[key])
}
for (let todo of todos){
    console.log(todo)
}
//for each
todos.forEach(function(todo){
    console.log(todo.text)
})
//map
const todoText = todos.map(function(todo){
    return todo.text
})
console.log(todoText)
//filter
const todoCompleted = todos.filter(function(todo){
    return todo.isCompleted === true
})
console.log(todoCompleted)

const todoCompletedText = todos.filter(function(todo){
    return todo.isCompleted===true
}).map(function(todo){
    return todo.text
})
console.log(todoCompletedText)
//Differences between double and triple equal
const numb = "10"
if (numb === 10){
    console.log("Number is = 10")
}
else{
    console.log("Number is not 10")
}

//Functions
function addNums(num1, num2){
    
    return num1+num2
}
console.log(addNums(5,10))

//Constructor Function

function Person(firstName, lastName, dob){
    this.firstName = firstName
    this.lastName = lastName
    this.dob = new Date(dob)
    this.getBirthYear = this.dob.getFullYear()
    //this.getFullName = function(){
        //return `${this.firstName} ${this.lastName}`
    //}
    //We can declare this function out of this scope as well

}
//declaretion of Person function out of its scope
Person.prototype.getFullName = function(){
    return `${this.firstName} ${this.lastName}`
}

//Instantiate Objects
const person1 = new Person('John','Doe','3-13-1995')
console.log(person1)
console.log(person1.firstName)
console.log(person1.getBirthYear)
console.log(person1.getFullName())

//Class does the exact same thing as the previous Person object
//Class
class ClPerson{
    constructor(firstName,lastName,dob){
        this.firstName = firstName
        this.lastName = lastName
        this.dob = new Date(dob)

    }
    getFullName(){
        return `${this.firstName} ${this.lastName}`

    }
    getBirthYear(){
        return this.dob.getFullYear()
    }
}
const person2 = new ClPerson('Mary','Smith','6-15-1984')
console.log(person2)
