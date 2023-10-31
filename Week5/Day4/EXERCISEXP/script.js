// // Exercise 1

// const people = ["Greg", "Mary", "Devon", "James"];


// // 1
// console.log(people)
// people.shift();
// console.log(people)

// // 2
// people[people.indexOf("James")] = "Jason";
// console.log(people)

// // 3
// people.push('Samuel');
// console.log(people)

// // 4
// console.log(people.indexOf("Mary"))

// // 5
// const copyOfPeople = people.slice(0, -1);
// console.log(copyOfPeople)


// // 6
// console.log(people.indexOf("Foo"))

// // it returns -1 to signal that the element is not present. This allows you to easily check whether an element is part of the array or not, without having to write additional code to handle such cases.

// // 7
// const last = people.slice(-1)
// console.log(last)


// // Part II - Loops

// // 8. 
// console.log(people.length)

// for (let i = 0; i < people.length; i++) {
//     console.log(people[i]);
//   }

// // 9.


//   for (let i = 0; i < people.length; i++) {
//     console.log(people[i]);
//     if (people[i] === "Devon") {
//       break;
//     }
//   }



//   🌟 Exercise 2 : Your Favorite Colors
// Instructions
// Create an array called colors where the value is a list of your five favorite colors.
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus


// const colors = ["blue", "red", "green", "purple", "yellow"];
// const suffixes = ["st", "nd", "rd", "th", "th"];

// for (let i = 0; i < colors.length; i++) {
//     console.log(`My ${i + 1}${suffixes[i]} choice is ${colors[i]}`);
//   }


//   🌟 Exercise 3 : Repeat The Question
// Instructions
// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?


// let userNumber;
// do {
//   userNumber = prompt("Please enter a number:");
//   userNumber = Number(userNumber); 
// } while (typeof userNumber == 'number' && userNumber < 10);



// 🌟 Exercise 4 : Building Management
// Instructions:

// 1
// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }
// 2
// console.log(building.numberOfFloors)
// 3
// let numberOfAptFloor1 = building.numberOfAptByFloor.firstFloor
// let numberOfAptFloor3 = building.numberOfAptByFloor.thirdFloor

// console.log(numberOfAptFloor1)
// console.log(numberOfAptFloor3)

// let result3 = (`there is ${numberOfAptFloor1} appartment in the first floor and ${numberOfAptFloor3} at the third floor`);
// console.log(result3)
// // 4

// let name2nd = building.nameOfTenants[1]
// console.log(`the name of the second tenant is ${name2nd}`)


// let sarahRent = building.numberOfRoomsAndRent.sarah[1]
// console.log(sarahRent)
// let davidRent = building.numberOfRoomsAndRent.david[1]
// console.log(davidRent)
// let danRent = building.numberOfRoomsAndRent.dan[1]
// console.log(danRent)

// let sum = sarahRent + davidRent

// if (sum > danRent){
//   building.numberOfRoomsAndRent.dan[1] = 1200;
//   console.log("Dan's rent has been increased to 1200.");
// } else {
//   console.log("The sum of Sarah's and David's rent is not bigger than Dan's rent.");
// }


// 🌟 Exercise 5 : Family
// Instructions
// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.

// const family = {
//   name: "Chemla",
//   members: 5,
//   city: "Ashdod",
// };

// console.log("Keys of the family object:");
// for (let key in family) {
//     console.log(key);
// }

// console.log("\nValues of the family object:");
// for (let key in family) {
//     console.log(family[key]);
// }

// Exercise 6 : Rudolf
// Instructions
// const details = {
//   my: 'name',
//   is: 'Rudolf',
//   the: 'raindeer'
// }
// Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”

// let result = "";

// for (let key in details){
//   result += `${key} ${details[key]} `
// }
// console.log(result)

// Exercise 7 : Secret Group
// Instructions
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”

let sortedNames = names.sort()

console.log(sortedNames)

let namesOfSociety = ''

for (let key of names){
  namesOfSociety += key[0]
}

console.log(namesOfSociety)