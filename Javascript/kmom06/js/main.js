(function () {
    'use strict';
    // initiering av variabler
    let hangman = window.Hangman;
    let alphabet = 'abcdefghijklmnopqrstuvwxyzåäö';
    let parentLetters = document.getElementsByClassName('letters')[0];
    let parentLines = document.getElementById('underLines');
    let parentLoseWin = document.getElementById('loseWin');

    // initiering av variabler.
    let selectedWord = hangman.randomIze();
    //let selectedWord = hangman.peek();
    let selectedWordList = selectedWord.split('');
    let currentLinesWords = [];
    let checkList = [];
    let count = 0;

    console.log(selectedWord);


    // funktion som skriver ut start-tillståndet i spelet.
    printLines();

    function printLines() {
        let lenLines = selectedWordList.length;

        for (let i = 0; i < lenLines; i++) {
            let line = document.createElement('div');

            line.className = 'test';
            line.innerHTML = '__';
            parentLines.appendChild(line);
            currentLinesWords.push(line);
        }
    }


    // Starttillståndet där alla delar är gömda.
    for (let i = 0; i < hangman.validParts.length; i++) {
        hangman.hide(hangman.validParts[i]);
    }


    // Funktion som gör en gissning kopplat till eventlistener.
    // kontrollerar om det klickade ordet finns i det sökta ordet.
    // om ja, skrivs rätt bokstav ut om nej, ritas del ut av bilden.
    // kontrollerar om användaren vunnit eller förlorat och skriver ut sträng.
    function makeGuess() {
        let clickedElement = event.target;

        clickedElement.style.backgroundColor = 'red';
        clickedElement.style.pointerEvents = 'none';
        let clickedLetter = clickedElement.innerHTML.toLowerCase();
        //console.log(clickedElement);

        // om det gissade ordet finns i det sökta ordet.
        if (selectedWordList.includes(clickedLetter)) {
            let indexWords = []; // index lista som lagrar index för rätt gissat ord.

            for (let index = 0; index < selectedWordList.length; index++) {
                if (clickedLetter == selectedWordList[index]) {
                    indexWords.push(index);
                }
            }

            // lägger till bokstaven på rätt plats på linjerna.
            if (indexWords.length == 1) {
                currentLinesWords[indexWords[0]].innerHTML = clickedLetter;
                checkList.push(clickedLetter);

                // kontrollerar om vinst eller förlust.
                if (checkList.length == selectedWordList.length) {
                    parentLoseWin.innerHTML = '<h3>You Won!</h3>';
                    let allLetters = document.querySelectorAll('.letter');

                    for (const element of allLetters) {
                        element.style.pointerEvents = 'none';
                    }
                }
                // lägger till bokstäverna på rätt index.
            } else {
                for (const element of indexWords) {
                    currentLinesWords[element].innerHTML = clickedLetter;
                    checkList.push(clickedLetter);
                }
                if (checkList.length == selectedWordList.length) {
                    parentLoseWin.innerHTML = '<h3>You Won!</h3>';
                    let allLetters = document.querySelectorAll('.letter');

                    for (const element of allLetters) {
                        element.style.pointerEvents = 'none';
                    }
                }
            }
            // om ordet inte finns i det sökta ordet, rita ut del av bild.
        } else {
            hangman.show(hangman.validParts[count]);
            count +=1;
            if (count == hangman.validParts.length) {
                parentLoseWin.innerHTML = '<h3>Game Over</h3>';
                let allLetters = document.querySelectorAll('.letter');

                for (const element of allLetters) {
                    element.style.pointerEvents = 'none';
                }
            }
        }
    }


    // skapar div element av bokstäverna och lägger till ett klickevent till dessa.
    for ( let i = 0; i < alphabet.length; i++) {
        let letterElement = document.createElement('div');

        letterElement.className = 'letter';
        letterElement.innerHTML = alphabet[i].toUpperCase();
        parentLetters.appendChild(letterElement);
        letterElement.addEventListener("click", makeGuess);
    }
})();
