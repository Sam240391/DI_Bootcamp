// Exercise 1 : Find The Numbers Divisible By 23

// function displayNumbersDivisible(){
//     let sum = 0
//     for (let i = 0; i < 500; i++){
//         if (i % 23 == 0){
//         console.log(i)
//         sum += i
//         }
//     }
//     console.log(sum)
// }

// displayNumbersDivisible()

// Bonus

// function displayNumbersDivisible(x){
//     let sum = 0
//     for (let i = 0; i < 500; i++){
//         if (i % x == 0){
//         console.log(i)
//         sum += i
//         }
//     }
//     console.log(sum)
// }

// displayNumbersDivisible(3)
// displayNumbersDivisible(45)

//  Exercise 2 : Shopping List

// Instructions
//1
// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 
//2
// let shoppingList = ['banana', 'orange', 'apple']
// // console.log(shoppingList)
// //3


// function myBill() {
//     let total = 0;
    
//     for (const item of shoppingList) {
//         if (item in stock && stock[item] > 0) {
//             total += prices[item];
//             stock[item] -= 1;
//         }
//     }
    
//     return total;
// }

// for (let item of shoppingList){
//     console.log(stock[item])
//     console.log(item)
//     console.log(prices[item])
// }

// console.log(myBill());



// Exercise 3 : What’s In My Wallet ?

// const quarters = 0.25
// const dimes = 0.10
// const nickel = 0.05
// const penny = 0.01

// function changeEnough(itemPrice, amountOfChange){
//     let result = amountOfChange[0]*quarters + amountOfChange[1]*dimes + amountOfChange[2]*nickel +amountOfChange[3]*penny
//     if (result >= itemPrice){
//         console.log(true)
//     }else{
//         console.log(false)
//     }
// }

// changeEnough(14.11, [2,100,0,0])
// changeEnough(0.75, [0,0,20,5])

// 🌟 Exercise 4 : Vacations Costs

// function hotelCost() {
//     let numberOfNights;
//     do {
//         const input = prompt("Enter the number of nights you would like to stay in the hotel:");
//         numberOfNights = parseInt(input);
//     } while (isNaN(numberOfNights) || numberOfNights <= 0);

//     const costPerNight = 140;
//     const totalCost = numberOfNights * costPerNight;

//     return totalCost;
// }

// function planeRideCost() {
//     let destination;
//     do {
//         destination = prompt("Enter your destination (London, Paris, or other):");
//     } while (!destination || typeof destination !== "string");

//     switch (destination.toLowerCase()) {
//         case "london":
//             return 183;
//         case "paris":
//             return 220;
//         default:
//             return 300;
//     }
// }

// function rentalCarCost() {
//     let numberOfDays;
//     do {
//         const input = prompt("Enter the number of days you'd like to rent the car:");
//         numberOfDays = parseInt(input);
//     } while (isNaN(numberOfDays) || numberOfDays <= 0);

//     const costPerDay = 40;
//     let totalCost = numberOfDays * costPerDay;

//     if (numberOfDays > 10) {
//         totalCost *= 0.95; 
//     }

//     return totalCost;
// }

// function totalVacationCost() {
//     const hotelCost = hotelCost();
//     const planeCost = planeRideCost();
//     const carCost = rentalCarCost();

//     const totalCost = hotelCost + planeCost + carCost;
//     console.log(`The hotel cost: $${hotelCost}, the plane tickets cost: $${planeCost}, the car rental cost: $${carCost}.`);
//     console.log(`Total vacation cost: $${totalCost}`);
//     return totalCost;
// }

// totalVacationCost();

// function hotelCost() {
//     let numberOfNights;
//     do {
//         const input = prompt("Enter the number of nights you'd like to stay in the hotel:");
//         numberOfNights = parseInt(input);
//     } while (isNaN(numberOfNights) || numberOfNights <= 0);

//     const costPerNight = 140;
//     const totalCost = numberOfNights * costPerNight;
//     return totalCost;
// }


// function planeRideCost() {
//     let destination;
//     do {
//         destination = prompt("Enter your destination (London, Paris, or other):");
//     } while (!destination || typeof destination !== "string");

//     switch (destination.toLowerCase()) {
//         case "london":
//             return 183;
//         case "paris":
//             return 220;
//         default:
//             return 300;
//     }
// }

// function rentalCarCost() {
//     let numberOfDays;
//     do {
//         const input = prompt("Enter the number of days you'd like to rent the car:");
//         numberOfDays = parseInt(input);
//     } while (isNaN(numberOfDays) || numberOfDays <= 0);

//     const costPerDay = 40;
//     let totalCost = numberOfDays * costPerDay;

//     if (numberOfDays > 10) {
//         totalCost *= 0.95; 
//     }

//     return totalCost;
// }

// function totalVacationCost() {
//     const hotelCost2 = hotelCost();
//     const planeCost = planeRideCost();
//     const carCost = rentalCarCost();

//     const totalCost = hotelCost2 + planeCost + carCost;
//     console.log(`The hotel cost: $${hotelCost2}, the plane tickets cost: $${planeCost}, the car rental cost: $${carCost}.`);
//     console.log(`Total vacation cost: $${totalCost}`);
//     return totalCost;
// }

// totalVacationCost();

// BONUS 

// function hotelCost(numberOfNights) {
//     const costPerNight = 140;
//     const totalCost = numberOfNights * costPerNight;
//     return totalCost;
// }

// function planeRideCost(destination) {
//     switch (destination.toLowerCase()) {
//         case "london":
//             return 183;
//         case "paris":
//             return 220;
//         default:
//             return 300;
//     }
// }

// function rentalCarCost(numberOfDays) {
//     const costPerDay = 40;
//     let totalCost = numberOfDays * costPerDay;

//     if (numberOfDays > 10) {
//         totalCost *= 0.95;
//     }

//     return totalCost;
// }

// function totalVacationCost() {
//     const numberOfNights = parseInt(prompt("Enter the number of nights you'd like to stay in the hotel:"));
//     const destination = prompt("Enter your destination:");
//     const numberOfDays = parseInt(prompt("Enter the number of days you'd like to rent a car:"));

//     const hotelCost2 = hotelCost(numberOfNights);
//     const planeCost = planeRideCost(destination);
//     const carCost = rentalCarCost(numberOfDays);

//     const totalCost = hotelCost2 + planeCost + carCost;
//     console.log(`The hotel cost: $${hotelCost2}, the plane tickets cost: $${planeCost}, the car rental cost: $${carCost}.`);
//     console.log(`Total vacation cost: $${totalCost}`);
//     return totalCost;
// }

// totalVacationCost();

// 🌟 Exercise 5 : Users


// const container = document.getElementById('container');
// //other way// const container = document.getElementsByTagName('div');
// // other way//const container = document.querySelector('div');
// console.log(container);

// const peteElement = document.querySelector(".list li:nth-child(2)");

// console.log(peteElement.textContent);
// peteElement.textContent = 'Richard';
// console.log(peteElement.textContent);

// const secondUL = document.querySelectorAll(".list")[1];
// console.log(secondUL.textContent);
// const secondLIs = secondUL.querySelectorAll("li");
// console.log(secondLIs[1].textContent);
// secondUL.removeChild(secondLIs[1]);
// console.log(secondUL.textContent);


// const uls = document.querySelectorAll(".list");

// //Before
// console.log(uls[0].textContent);
// console.log(uls[1].textContent);

// for (const ul of uls) {
//     const firstLI = ul.querySelector("li");
//     firstLI.textContent = "Samuel"; 
// }

// //After
// console.log(uls[0].textContent);
// console.log(uls[1].textContent);


// for (const ul of uls) {
//     ul.classList.add("student_list")
// }

// console.log(uls);
// uls[0].classList.add('university', 'attedance');

// console.log(uls);

// container.style.background = 'lightblue';
// container.style.padding = "10px";

// const danLI = document.querySelector(".list:nth-child(1) li:last-child");

// let ultwo = uls[1].querySelectorAll("li");
// console.log(ultwo[1].textContent);
// let danIL = ultwo[1];
// danIL.style.display = 'none';

// let ulOne = uls[0].querySelectorAll("li");
// console.log(ulOne[1].textContent);
// let richarLi = ulOne[1]
// richarLi.style.border = 'black 1px solid';

// document.body.style.fontSize = "32px";

// const backgroundColor = getComputedStyle(container).backgroundColor;

// if (backgroundColor === "rgb(173, 216, 230)") {
//     const userList = [];
//     const uls = document.querySelectorAll(".list");
//     for (const ul of uls) {
//         const lis = ul.querySelectorAll("li");
//         for (const li of lis) {
//             userList.push(li.textContent);
//         }
//     }
//     const lastUser = userList[userList.length-1];
//     userList.pop()
//     alert(`Hello ${userList.join(",")} and ${lastUser}`);
// }


// 🌟 Exercise 6 : Change The Navbar

// const classDiv = document.getElementById('navBar');
// console.log(classDiv);
// classDiv.setAttribute('id', 'socialNetworkNavigation');

// const firstUl = document.querySelector('ul');
// console.log(firstUl)


// const newListItem = document.createElement("li");

// const textNode = document.createTextNode("Logout");

// newListItem.appendChild(textNode);

// firstUl.appendChild(newListItem);

// console.log(firstUl)

// const firstLinkText = firstUl.firstElementChild.textContent;
// const lastLinkText = firstUl.lastElementChild.textContent;

// console.log("1st link is  : " + firstLinkText);
// console.log("Last link is : " + lastLinkText);

// Exercise 7 : My Book List

const allBooks = [
    {
        title: "Harry Potter",
        author: "J.K. Rowling",
        image: "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRViJNPZX3IS87fq4X1QbyEGvhlMQERhDRUasptRAepYnFrWDEh",
        alreadyRead: true,
    },
    {
        title: "To Kill a Mockingbird",
        author: "Harper Lee",
        image: "https://images.epagine.fr/637/9781784752637_1_75.jpg",
        alreadyRead: false,
    },
];

const listBooksSection = document.querySelector(".listBooks");

console.log(listBooksSection);


allBooks.forEach((book) => {
    const bookDiv = document.createElement("div");
    const bookInfo = document.createElement("h2");
    const bookRead = document.createElement("p");
    const bookImage = document.createElement("img");

    bookInfo.textContent = `${book.title} written by ${book.author}`;
    bookRead.textContent = book.alreadyRead ? "Already read" : "Not read yet";
    bookImage.src = book.image;
    bookImage.style.width = "100px";

    if (book.alreadyRead) {
        bookInfo.style.color = "red";
        bookRead.style.color = "red";
    }

    bookDiv.appendChild(bookImage);
    bookDiv.appendChild(bookInfo);
    bookDiv.appendChild(bookRead);

    listBooksSection.appendChild(bookDiv);
});