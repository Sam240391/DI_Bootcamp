// // Function Decleration and Calling

// function greet (){
//     console.log('Welcome to the page');
// }

// greet();


// // Parameters

// function greet (username){
//     console.log(`Welcome to the page ${username}`);
// }

// greet('Samuel Chemla');


// function greet1 (username, age){
//     console.log(`Welcome to the page ${username} you have ${age}`);
// }

// greet1('Samuel Chemla', 32);


// EXERCISE 1

// function ageMomAndDad (myAge){
//     let ageMom = myAge * 2;
//     let ageDad = ageMom * 1.2;
//     console.log(`I'm ${myAge} my mom are ${ageMom} and my dad are ${ageDad} `);
// }

// ageMomAndDad(22)


// Function Return

// function userInfo(userName, userAge) {
//     let result = "My name is " + userName + ", my age is " + userAge;
//     return result;
// }

// let girlInfo = userInfo("Sarah", 22);
// console.log(girlInfo); //My name is Sarah, my age is 22

// EXERCISE 2

// function ageMom(myAge){
//     let ageMom = myAge * 2;
//     return ageMom
// }


// console.log(ageMom(20))


// Try/catch/finally -> EXCEPTION





// const func = () => {
//     try {
//         console.log("starting the try block")
//         //Unexisting variable
//         hello
//         //not accessed if there is an error with the above code
//         console.log("finishing the try block")
//     } catch (err) {
//         console.log("starting the catch block")
//         console.log(err)
//     } finally {
//         console.log("Function done")
//     }
// }

// func()



// const func = () => {
//     try {
//         console.log("starting the try block")
//         hello
//         console.log("finishing the try block")
//     } catch (err) {
//         //Check the type of error
//         if (err instanceof ReferenceError) {
//             console.log(`
//                 Error Name : ${err.name}, 
//                 Error Msg : ${err.message},
//                 Error Stack : ${err.stack}`)
//         } else {
//             console.log("Other Error")
//         }
//     } finally {
//         console.log("Function done")
//     }
// }

// func()

//  OBJECT

// let object= {
//     property : value,
//     property : value,
//     property : function () {
//         statement
//     }
// }

// let name = 'Samuel'


// let person= {
//     name : "Sarah",
//     eyeColor: "blue",
//     eat : function () {
//         console.log(`${this.name} love chocolate`);
//     },
// };

// person.eat();


// Document Object Model
// HTML is the structure of your page, the skeleton
// CSS controls the style of the page
// JavaScript makes the page dynamic.
// The browser is a program that interprets HTML and CSS and renders the structure and style into the page that you see.
// It creates a representation of the document called Document Object Model.
// This model allows JavaScript to access the text content and elements of the website document as objects.


// EXERCISE 1

let paragraphs = document.getElementsByTagName("p");
alert("Content in the second paragraph is " + paragraphs[1].innerHTML);
// document.getElementById("second").innerHTML = "The orginal message is changed.";