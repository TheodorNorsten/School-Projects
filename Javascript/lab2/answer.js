/**
 * @preserve 8fecb0dfd694e897074d9f075f19990e
 *
 * 8fecb0dfd694e897074d9f075f19990e
 * js
 * lab2
 * v1
 * thno20
 * 2020-11-14 10:54:28
 * v4.0.0 (2019-03-05)
 *
 * Generated 2020-11-14 11:54:28 by dbwebb lab-utility v4.0.0 (2019-03-05).
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
 * Lab 2 - statements
 *
 * Statements and expressions in JavaScript.
 *
 * Use MDN as your reference and base to solving the exercises.
 *
 */



/** ----------------------------------------------------------------------
 * Section 1 . If, else if and else
 *
 */



/**
 * Exercise 1.1 (1 points)
 *
 * Create five variables: `card1, card2, card3, card4, card5`.
 *
 * Assign the values `7, 11, 2, 7, 4` to the variables created above.
 *
 * Add them up and put the sum in a variable called `result`.
 *
 * Answer with the variable `result`.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

let card1 = 7;
let card2 = 11;
let card3 = 2;
let card4 = 7;
let card5 = 4;
let result = card1 + card2 + card3 + card4 + card5;





ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.1", ANSWER, false);

/**
 * Exercise 1.2 (1 points)
 *
 * Use an `if statement` to see if the five cards (card1-card5) have a
 * combined sum that is higher than 21.
 *
 * Create a variable `status` and give it a different value depending on the
 * following.
 *
 * * If the sum is higher than 21, give your variable the value `"busted"`.
 * * Else give it the value `"safe"`.
 *
 * Answer with your status-variable.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */
let status;

if (result > 21) {
  status = 'busted';
} else {
  status = 'safe';
}






ANSWER = status;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.2", ANSWER, false);

/**
 * Exercise 1.3 (1 points)
 *
 * Use `if else statements` to see if the combined value of the first three
 * cards (card1-card3) is lower, higher or exactly 21.
 *
 * Answer with a string corresponding to the result:
 * lower = `"safe"`
 * higher = `"busted"`
 * 21 = `"black jack"`
 *
 * Store the response in your status-variable and answer with it.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */
let value;

if ( (card1 + card2 + card3) > 21 ) {
  value = 'busted';
} else if ((card1 + card2 + card3) < 21) {
  value = 'safe';
 } else {
  value = 'black jack';
}







ANSWER = value;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.3", ANSWER, false);

/**
 * Exercise 1.4 (2 points)
 *
 * Create three variables: `dealer1, dealer2, dealer3`.
 *
 * Assign the values `9, 6, 4` to the variables.
 *
 * Combine the `if`, `else if`, `else` statements and the operator `AND (&&)`
 * to see what the dealer should do. Combine as you feel needed.
 *
 * If the sum of the dealercards is lower than 17, answer with `"pick"`, if
 * the sum is higher than or equal to 17 and lower than 21 answer with
 * `"stop"`. If the sum is 21 answer with `"black jack"`. If the sum is higher
 * than 21 answer with `"busted"`.
 *
 * Store the response in a variable, and answer with it.
 *
 * PS. You can change the sum to test that your if-statement really works for
 * all values, just to try it out.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

let dealer1 = 9;
let dealer2 = 6;
let dealer3 = 4;

let tot = dealer1 + dealer2 + dealer3;

let totString;

if (tot < 17) {
  totString = 'pick';
} else if (tot >= 17 && tot < 21) {
  totString = 'stop';
 } else if (tot == 21) {
  totString = 'black jack';
} else {
  totString = 'busted';
}







ANSWER = totString;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.4", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 2 . Switch, case
 *
 */



/**
 * Exercise 2.1 (1 points)
 *
 * Use a switch-case statement to create a message with the type of fruit and
 * its color. You have the following type of fruits with a corresponding
 * color:
 *
 * * banana: yellow
 * * apple: green
 * * kiwi: green
 * * plum: purple
 *
 * Create a variable `myFruit` which holds the current type of your fruit. If
 * 'myFruit' is banana, the result should be a variable containing the string
 * value `"The banana is yellow."`
 *
 * Ensure that your switch-case works for all values.
 *
 * Answer with the result where `myFruit = "apple"`.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

let myFruit = 'apple';
let string;

switch (myFruit) {
  case 'banana':
    string = `The ${myFruit} is yellow.`;
    break;
  case 'apple':
    string = `The ${myFruit} is green.`;
    break;
  case 'kiwi':
    string = `The ${myFruit} is green.`;
    break;
  case 'plum':
    string = `The ${myFruit} is putple.`;
    break;
  default:
    string = 'That is an unknown fruit.';
}



ANSWER = string;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.1", ANSWER, false);

/**
 * Exercise 2.2 (1 points)
 *
 * Extend your switch-case statement with a `default value`. The result should
 * be:
 *
 * `"That is an unknown fruit."` when the variable 'myFruit' has an unknown
 * value.
 *
 * Answer with the result where 'myFruit = pear'.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */
 myFruit = 'pear';


 switch (myFruit) {
   case 'banana':
     string = `The ${myFruit} is yellow.`;
     break;
   case 'apple':
     string = `The ${myFruit} is green.`;
     break;
   case 'kiwi':
     string = `The ${myFruit} is green.`;
     break;
   case 'plum':
     string = `The ${myFruit} is putple.`;
     break;
   default:
     string = 'That is an unknown fruit.';
 }





ANSWER = string;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.2", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 3 . For loops
 *
 */



/**
 * Exercise 3.1 (1 points)
 *
 * Use a `for-loop` to increment `211` with the value `9`, `19` times.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

let numb = 211;

for (let i = 0; i < 19; i++) {
  numb += 9;
//  console.log(numb);
}




ANSWER = numb;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.1", ANSWER, false);

/**
 * Exercise 3.2 (1 points)
 *
 * Use a for-loop to decrement `556` with the value `7`, `20` times.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */
let numbTwo = 556;

for (let i = 0; i < 20; i++) {
  numbTwo -= 7;
  //console.log(numbTwo);
}





ANSWER = numbTwo;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.2", ANSWER, false);

/**
 * Exercise 3.3 (3 points)
 *
 * Use a for-loop to add all the odd values in the range `20` to `48` to a
 * string with each number separated by a comma `,`.
 *
 * The result should not end with a comma. You should neither have a space
 * after the comma.
 *
 * Answer with the resulting string.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

let stringNumb = '';

for (let i = 20; i < 48; i++) {
  if (i % 2 != 0) {
    i = i.toString();
    if (i != 47) {
      stringNumb += i +',';
    } else {
      stringNumb += i;
    }
    }
}
//console.log(stringNumb);

ANSWER = stringNumb;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.3", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 4 . While loops
 *
 */



/**
 * Exercise 4.1 (1 points)
 *
 * Use a `while-loop` to increment `19` with the value `9` until it has
 * reached or passed `211`.
 *
 * Answer with the amount of steps needed.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

let i = 19;
let step = 0;

while (i <= 211) {
  i += 9;
  step += 1;
}





ANSWER = step;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("4.1", ANSWER, false);

/**
 * Exercise 4.2 (1 points)
 *
 * Use a while-loop to subtract `7` from `556` until the value has reached or
 * passed `0`.
 *
 * Answer with the amount of steps needed.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */
let tal = 556;
let stepTwo = 0;

while (tal >= 0) {
  tal -= 7;
  stepTwo += 1;
}


ANSWER = stepTwo;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("4.2", ANSWER, false);

/**
 * Exercise 4.3 (3 points)
 *
 * Use a while-loop to add all the values, to a comma-separated string, in the
 * range `25` to `63`, where the value is divisable by 5 or 7.
 *
 * Answer with the resulting string.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

let stringValue ='';
let range = 25;

while (range >= 25 && range <= 63) {
  if (range % 5 == 0 || range % 7 == 0) {
    stringValue += range.toString() +',';
  }
  range ++;
}
stringValue = stringValue.substr(0, stringValue.length-1);

//console.log(stringValue);





ANSWER = stringValue;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("4.3", ANSWER, false);


console.log(dbwebb.exitWithSummary());
}(window.dbwebb));
