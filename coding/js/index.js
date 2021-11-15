console.log("hello world");

// let num = 6;
// num = num + 20;
// console.log(num);
for (let num = 0; num < 51; num++)
  if (num % 15 === 0) {
    console.log("fuzz buzz");
  } else if (num % 3 === 0) {
    console.log("fuzz");
  } else if (num % 5 === 0) {
    console.log("buzz");
  } else {
    console.log(num);
  }

// const faren = [0,23,140,212,41];

// function getCelsius() {

//   const celsius=faren.map(far => (far-32)*5/9 );
//   console.log(celsius)
// }

// getCelsius();

// const istrue = [11, 1, [], "angels"];
// function checkforfalsey() {
//   return istrue.some((value) => !value);
// }
// console.log(checkforfalsey());

// const gettotal = ["rabbit", "football", "cracking"];
// function total() {
//   return gettotal.reduce((tx, ty) => tx + ty.length, 0);
// }
// console.log(total());

// const square=[9,16,81]
// function checksquare(){
//   return square.every(num=>num*num)
// }
//  console.log(checksquare())

// const word = ["monkey", "donkey", "cat", "mouse"];
// const num = 4;
// function getword() {
//   return word.filter((words) => words.length < num);
// }
// console.log(getword());

// getValues = ["23cm", "5.6cm", "1000cm", "84cm"];

// function getvalue() {
//   return getValues.map(value=>parseFloat(value))

// }

// console.log(getvalue())

// const word= "In West Philadelphia, born and raised";
// const vowel=["a","e","i","o",'u','A',"I","E","O","U"]

// function getVowel() {
//   const letter=word.split("")
//   console.log(letter.filter(isvowel=>vowel.includes(isvowel)));
// }
// // console.log(word.split(""))

// getVowel()

const drinks = ["vodka", "white wine", "beer", "mocktail"];

const randomNumber = Math.random() * drinks.length;
console.log(randomNumber);
const randomInteger = Math.floor(randomNumber);
console.log(randomInteger);
console.log(drinks[randomInteger]);
