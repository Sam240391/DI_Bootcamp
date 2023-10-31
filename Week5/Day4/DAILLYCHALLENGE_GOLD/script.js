const numbers = [5,0,9,1,7,4,2,6,3,8];
console.log(numbers)
let stringsNumbers = numbers.toString()
console.log(stringsNumbers)

let joinNumbers1 = numbers.join("+")
console.log(joinNumbers1)

let joinNumbers2 = numbers.join("/")
console.log(joinNumbers2)

let joinNumbers3 = numbers.join(" ")
console.log(joinNumbers3)


for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length - i - 1; j++) {
      if (numbers[j] < numbers[j + 1]) {
        let temp = numbers[j];
        numbers[j] = numbers[j + 1];
        numbers[j + 1] = temp;
      }
    }
    console.log("Iteration " + (i + 1) + ": " + numbers);
  }
  
  console.log("Sorted array in descending order: " + numbers);