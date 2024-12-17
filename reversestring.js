// Create a funtion that reverses a string :
// 'Hello how are you' should be: 'uoy era woh olleH'

//method 1
function reverse(str) {
  if (!str || typeof str !== "string" || str.length < 2) {
    return "Wrong";
  }
  const stringArray = [];
  const stringLength = str.length - 1;
  for (let i = stringLength; i >= 0; i--) {
    stringArray.push(str[i]);
  }
  return stringArray.join("");
}

const reversed = reverse("Hello how are you");

console.log(reversed);

//Method 2 using built-in method
function reverse2(str) {
  return str.split("").reverse().join("");
}
const reversed2 = reverse2("Hello how are you");

console.log(reversed2);

//method 3 with ES6 syntax

const reverse3 = (str) => str.split("").reverse().join("");

const reversed3 = reverse3("Hello how are you");

console.log(reversed3);

//method 4 with spread operator (which removes the need for split())

const reverse4 = (str) => [...str].reverse().join("");

const reversed4 = reverse4("Hello how are you");

console.log(reversed4);


//output: 'uoy era woh olleH'
