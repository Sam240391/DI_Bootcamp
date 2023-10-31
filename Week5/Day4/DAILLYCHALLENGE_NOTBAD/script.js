// 1
let sentence = "The movie is not that bad, I like it"
// 2
let wordNot = sentence.indexOf("not")
console.log(wordNot)
// 3
let wordBad = sentence.indexOf("bad")
console.log(wordBad)


if (wordBad > wordNot){
    const modifiedSentence = sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
    console.log("The result is: " + modifiedSentence);
} else {
    console.log("The result is: " + sentence);
}
