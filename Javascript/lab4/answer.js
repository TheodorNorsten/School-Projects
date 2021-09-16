/**
 * @preserve 317289fb3e31a0dd19c8700e44af81fd
 *
 * 317289fb3e31a0dd19c8700e44af81fd
 * js
 * lab4
 * v1
 * thno20
 * 2020-11-27 11:58:37
 * v4.0.0 (2019-03-05)
 *
 * Generated 2020-11-27 12:58:37 by dbwebb lab-utility v4.0.0 (2019-03-05).
 * https://github.com/dbwebb-se/lab
 */

/*jshint maxcomplexity:false */
/* eslint-disable indent */
/* jscs:disable indent */
(function (dbwebb) {
"use strict";

var ANSWER = null;

console.log("Ready to begin.");


/** ======================================================================
 * Lab 4 - arrays
 *
 * Practise arrays. You might find useful help here:
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Ob
 * jects/Array
 *
 */



/** ----------------------------------------------------------------------
 * Section 1 . Arrays
 *
 * To copy an array use array.slice() to make a real copy, not a shallow one.
 *
 */



/**
 * Exercise 1.1 (1 points)
 *
 * Create a variable `array2` holding an array with the words:
 * `[candy,cake,cupcakes,lollipop,pringles]`. Return the element on position:
 * `1` in array2.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

let array2 = ['candy', 'cake', 'cupcakes', 'lollipop', 'pringles'];











ANSWER = array2[1];

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.1", ANSWER, false);

/**
 * Exercise 1.2 (1 points)
 *
 * Use the variable `array2`. Concatenate the first item and the last item as
 * a string. Separate the string with `-`.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */
let first = array2[0];
let last = array2[array2.length - 1];
//console.log(`${first}, ${last}`);
let string = first + '-' + last;
//console.log(string);








ANSWER = string;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.2", ANSWER, false);

/**
 * Exercise 1.3 (1 points)
 *
 * Create an array, `array1`, with the items `42,78,-1,0,-432,799,2,1100`.
 *
 * Merge the two arrays, `array1` and `array2`, into a third variable
 * `array3`.
 *
 * Answer with array3.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

let array1 = [42, 78, -1, 0, -432, 799, 2, 1100];
let array3 = array1.concat(array2);
//console.log(array3);



ANSWER = array3;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.3", ANSWER, false);

/**
 * Exercise 1.4 (1 points)
 *
 * Create a variable `array21` as a clone of `array2`.
 * Sort `array21`.
 * (Hint:
 * http://stackoverflow.com/questions/3978492/javascript-fastest-way-to-duplic
 * ate-an-array-slice-vs-for-loop)
 *
 * Answer with the resulting array.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

let array21 = array2.slice();

array21.sort();
//console.log(array21);




ANSWER = array21;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.4", ANSWER, false);

/**
 * Exercise 1.5 (1 points)
 *
 * Create a variable `array11` as a copy of `array1`.
 * Sort `array11` according to its values. The smallest value comes first and
 * the largest value comes last.
 *
 * Answer with the resulting array.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */
let array11 = array1.slice();

array11.sort(function(a, b) {return a-b;});
//console.log(array11);





ANSWER = array11;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.5", ANSWER, false);

/**
 * Exercise 1.6 (1 points)
 *
 * Create a variable `array22` which holds the same content as `array2` - but
 * all strings are uppercase.
 * Use the built-in Array-function `map()` to solve it.
 *
 * Answer with the array.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

let array22 = array2.map(function(i) {
  return i.toUpperCase();
});
//console.log(array22)






ANSWER = array22;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.6", ANSWER, false);

/**
 * Exercise 1.7 (1 points)
 *
 * Create a new array, `array12`. It should contain all positive numbers from
 * the `array1`.
 * Use the built-in array-function `filter()` to solve it.
 *
 * Answer with the resulting array.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

let array12 = array1.filter(function(i) {
  return i > 0;
});
//console.log(array12);



ANSWER = array12;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.7", ANSWER, false);

/**
 * Exercise 1.8 (1 points)
 *
 * Create a function `arrayAverage()` that takes one array as argument and
 * returns the average of all elements in that array.
 *
 * Try out the function using `array1` and answer with the rounded integer
 * result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function arrayAverage(array) {
  let sum = array.reduce((tot, currentvalue) => tot + currentvalue);

  return Math.round(sum/array.length);
}
//console.log(arrayAverage(array1));





ANSWER = arrayAverage(array1);

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.8", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 2 . Modify arrays
 *
 * Learn how to modify arrays.
 *
 */



/**
 * Exercise 2.1 (1 points)
 *
 * Create a new array `myArray` and make it a copy of `array1`. Switch place
 * on the first and the last element, with the help of built-in
 * array-functions.
 * Use the array-functions `pop(), push(), shift() and unshift()`.
 *
 * Answer with `myArray`.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

 let myArray = array1.slice();
 let lastEl = myArray.pop();
 let firstEl = myArray.shift();

 myArray.unshift(lastEl);
 //console.log(myArray);
 myArray.push(firstEl);
 //console.log(myArray);




ANSWER = myArray;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.1", ANSWER, false);

/**
 * Exercise 2.2 (1 points)
 *
 * In `myArray` change the `3rd and 4th` value to the boolean value `false`
 * using built-in array-function `splice()`.
 *
 * Answer with the resulting array.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */
//console.log(myArray);
myArray.splice(2, 2, false, false);
//console.log(myArray);
//console.log(myArray[3]);




ANSWER = myArray;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.2", ANSWER, false);

/**
 * Exercise 2.3 (1 points)
 *
 * Remove the `4th and 5th` item in 'myArray'. Then insert the string `MEGA`
 * after the item `3rd`. Answer with the resulting array.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */
//console.log(myArray);
myArray.splice(3, 2);
//console.log(myArray);
myArray.splice(3, -1, 'MEGA');
//console.log(myArray);






ANSWER = myArray;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.3", ANSWER, false);


console.log(dbwebb.exitWithSummary());
}(window.dbwebb));
