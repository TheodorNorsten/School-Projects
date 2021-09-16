/**
 * @preserve 9e3583a9bf0be5faaf41cf9ca4b4ab3f
 *
 * 9e3583a9bf0be5faaf41cf9ca4b4ab3f
 * js
 * lab3
 * v1
 * thno20
 * 2020-11-20 16:55:44
 * v4.0.0 (2019-03-05)
 *
 * Generated 2020-11-20 17:55:45 by dbwebb lab-utility v4.0.0 (2019-03-05).
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
 * Lab 3 - functions
 *
 * Practice to write functions.
 *
 */



/** ----------------------------------------------------------------------
 * Section 1 . Basic functions
 *
 * Practice on basic functions.
 *
 */



/**
 * Exercise 1.1 (1 points)
 *
 * Create a function `sumRangeNumbers()` that returns the sum of all numbers
 * between two chosen numbers. The function should take two arguments, one
 * representing the lowest boundary and one that represents the highest
 * boundary. For example, the arguments 10 and 20 should return the sum of
 * 10+11+12+13...+20.
 *
 * Test it using the values `47 and 94`, answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */
//sumRangeNumbers(4,12);
function sumRangeNumbers(min, max) {
  let tot = 0;

  for (min; min <= max; min++) {
    tot += min;
    //console.log(summa);
  }
  return tot;
}






ANSWER = sumRangeNumbers(47, 94);


// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.1", ANSWER, false);

/**
 * Exercise 1.2 (1 points)
 *
 * Create a function called `fruitColor()` that takes one argument called
 * `fruit` and returns the color of the fruit.
 *
 * The function should be aware of the following fruits (`banana, apple, kiwi,
 * plum`) with respective color (`yellow, green, green, red`).
 *
 * Try it out using the fruit `banana` and answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function fruitColor(fruit) {
  if (fruit == 'banana') {
    return 'yellow';
  } else if (fruit == 'apple') {
    return 'green';
  } else if (fruit == 'kiwi') {
    return 'green';
  } else {
    return 'red';
  }
}
//console.log(fruitColor('kiwi'));









ANSWER = fruitColor('banana');

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.2", ANSWER, false);

/**
 * Exercise 1.3 (1 points)
 *
 * Create a function `printRange()` that takes two arguments `rangeStart` and
 * `rangeStop` and returns a string with all numbers comma-separated in the
 * range.
 *
 * Try it using the arguments `24 and 45`.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function printRange(rangeStart, rangeStop) {
  let string = '';

  for (rangeStart; rangeStart <= rangeStop; rangeStart++) {
    if ( rangeStart == rangeStop) {
      string += rangeStart.toString();
    } else {
      string += rangeStart.toString() + ',';
    }
}
  return string;
}
//console.log(printRange(24,45));



ANSWER = printRange(24, 45);

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.3", ANSWER, false);

/**
 * Exercise 1.4 (1 points)
 *
 * Create a function `printRangeReversed()` that takes two arguments
 * `rangeStart` and `rangeStop` and returns a string with all numbers
 * comma-separated in the range.
 *
 * Try it using the arguments `45 and 24`.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

 function printRangeReversed(rangeStop, rangeStart) {
   let string = '';

   for (rangeStop; rangeStop >= rangeStart; rangeStop--) {
     if ( rangeStart == rangeStop) {
       string += rangeStop.toString();
     } else {
       string += rangeStop.toString() + ',';
     }
     }
   return string;
 }

//console.log(printRangeReversed(45,24));





ANSWER = printRangeReversed(45, 24);

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.4", ANSWER, false);

/**
 * Exercise 1.5 (1 points)
 *
 * Create a function `printAnyRange()` that takes two arguments `rangeStart`
 * and `rangeStop` and returns a string with all numbers comma-separated in
 * the range.
 *
 * If `rangeStart` is smaller than `rangeStop` then call the function
 * `printRange()`.
 *
 * If `rangeStart` is greater than `rangeStop` the call the function
 * `printRangeReversed()`.
 *
 * Try it using the arguments `24 and 45` (both ways).
 *
 * Answer with the result using arguments 24 and 45.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */
function printAnyRange(rangeStart, rangeStop) {
  //let string = '';
  if (rangeStart > rangeStop) {
    return printRangeReversed(rangeStop, rangeStart);
     //console.log(string);
   } else {
    return printRange(rangeStart, rangeStop);
    //console.log(string);
  }
}
//console.log(printAnyRange(45,24));








ANSWER = printAnyRange(24, 45);

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.5", ANSWER, false);

/**
 * Exercise 1.6 (1 points)
 *
 * Create a function called `stringRepeat()` that returns a string a specific
 * number of times. The function should take two arguments, one string and one
 * number: `blue` and `6`. The number represents the number of times the
 * string should be added to a string.
 *
 * Test the function and answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function stringRepeat(string, number) {
  let totString = '';

  for (let i = 0; i < number; i++) {
    totString += string;
  }
  return totString;
}
//console.log(stringRepeat('blue',6))








ANSWER = stringRepeat('blue', 6);

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.6", ANSWER, false);

/**
 * Exercise 1.7 (1 points)
 *
 * Create a function `inRange()` that takes three arguments, `rangeStart`,
 * `rangeStop` and `value`.
 *
 * The function should return boolean `true` if value is greater than
 * rangeStart and less than rangeStop. Otherwise it should return boolean
 * `false`.
 *
 * Try it out using the range `125 - 545` and the value `274`.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function iRange(rangeStart, rangeStop, value) {
  if (value > rangeStart && value < rangeStop) {
    return true;
  } else {
    return false;
  }
}
//console.log(iRange(125,545,274));








ANSWER = iRange(125, 545, 274);

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.7", ANSWER, false);

/**
 * Exercise 1.8 (1 points)
 *
 * Try out the function `inRange()` using the range `125 - 545` and the value
 * `659`.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */


ANSWER = iRange(125, 545, 659);

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.8", ANSWER, false);

/**
 * Exercise 1.9 (1 points)
 *
 * Create a function called `degreesToRadians()` that should take one
 * argument, a degree value. The function should convert the value to radians
 * and return the result with max 4 decimals.
 *
 * Test your function with the value `210` and answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function degreesToRadians(degree) {
  const convertion = 180;
  let radius = degree*(Math.PI/convertion);

  return Math.round(radius*10000)/10000;
}
//console.log(degreesToRadians(210));




ANSWER = degreesToRadians(210);

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.9", ANSWER, false);

/**
 * Exercise 1.10 (1 points)
 *
 * Create a function called `fizzBuzz()` that takes two arguments `start` and
 * `stop` and returns a comma-separated string.
 *
 * The arguments represents the starting point and stop point of the game
 * `Fizz Buzz` (http://en.wikipedia.org/wiki/Fizz_buzz). The function should
 * run from start to stop and add `Fizz`, `Buzz` or both to your
 * result-variable at appropriate numbers.
 *
 * Each entry to your result should be comma-separated. If `stop` is equal or
 * lower than `start`, the function should return an appropriate error
 * message.
 *
 * Test the function using `start=2 and stop=20`.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function fizzBuzz(start, stop) {
  if ( start >= stop) {
    return 'the variable start cannot be >= variabel stop';
  }
  let string = '';

  for (start; start <= stop; start ++) {
    if (start % 3 == 0 && start % 5 == 0) {
      if (start == stop) {
        string += 'FizzBuzz';
      } else {
          string += 'Fizz Buzz' + ',';
        }
      } else if (start % 3 == 0) {
      if (start == stop) {
        string += 'Fizz';
      } else {
            string += 'Fizz' + ',';
          }
      } else if ( start % 5 == 0) {
      if (start == stop) {
        string += 'Buzz';
      } else {
      string += 'Buzz' + ',';
    }
      } else {
      if (start == stop) {
        string += start;
      } else {
        string += start + ',';
      }
}
  }
  return string;
    }

//console.log(fizzBuzz(2,20));



ANSWER = fizzBuzz(2, 20);

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.10", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 2 . Extra assignments
 *
 * These questions are worth 3 points each. Solve them for extra points. In
 * this section, you could re-use your code from lab 1 in exercise 2.1 and
 * 2.2.
 *
 */



/**
 * Exercise 2.1 (3 points)
 *
 * Create a function called `printSum()` that should take two variables, the
 * sum of the players hand and the sum of the dealers hand.
 *
 * Your hand should be three cards with the values: `10, 9 and 2`.
 * The dealers hand should be three card with the values: `7, 6, 10`.
 * The function should return the sum and the player: `Player: 21, Dealer:
 * 23`.
 *
 * Test your function with the given values and answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */






ANSWER = "Replace this text with the variable holding the answer.";

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.1", ANSWER, false);

/**
 * Exercise 2.2 (3 points)
 *
 * Create a function called `printResult()` that should take two variables,
 * the sum of the players hand and the sum of the dealers hand.
 *
 * Players hand should be three cards with the values: `10, 9 and 2`. The
 * dealers hand should be three card with the values: `7, 6, 10`.
 *
 * This time you should include the check from lab 2 where you find out the
 * boundaries of the player and the dealer.
 * Player hand = 21 (black jack).
 * Player hand less than 21 (safe).
 * Player hand larger than 21 (busted).
 * Dealer hand less than 17 (safe).
 * Dealer hand larger or equal to 17 and less than 21 (stop).
 * Dealer hand = 21 (black jack).
 * Delaer hand larger than 21 (busted).
 *
 * Return a string in the format: `Player: safe, Dealer: busted`.
 *
 * Test your function with the given values and answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */






ANSWER = "Replace this text with the variable holding the answer.";

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.2", ANSWER, false);

/**
 * Exercise 2.3 (3 points)
 *
 * Create a function called `calculateInterest()` that returns the money you
 * have after x years of interest, given three arguments: `652, 15 and 2`.
 * First argument represents the start money, the second argument represents
 * the number of years your money produces interest. The third argument is the
 * interest rate in percent (%).
 *
 * Test your function and answer with the result with a maximum of 4 decimals.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */






ANSWER = "Replace this text with the variable holding the answer.";

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.3", ANSWER, false);


console.log(dbwebb.exitWithSummary());
}(window.dbwebb));
