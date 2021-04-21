// modul för deltest 1

window.part1 = (function() {
    // initiering av variabler.
    let score = 0;
    let maxScore = 15;
    let structureList = ['question', 'top', 'middle', 'bottom'];
    let questionDivList = [];
    let countCorrect = 0;
    let countQuestions = 0;
    let countAnswers = 0;
    let countNextButton = 1;
    let testText = document.getElementsByClassName('quiz')[0];
    let content = document.getElementsByClassName('content')[0];
    let nextButton = document.getElementById('next');


    let allQuestions = ['Vad heter skolan Harry potter går på?',
        'Hur många är dvärgarna i snövit?',
        'Vad heter Zlatan i efternamn?', 'Vem är luke skywalkers far?',
        'Vem var Amerikas 44:e president?'];

    let optionList = [['Trollskolan', 'Wizardschool', 'Hogwarts'], ['5', '6', '7'],
        ['Ibrahimovic´', 'Andersson', 'svensson'],
        ['Obi Wan Kenobi', 'Darth Vader', 'Yoda'],
        ['Donald Trump', 'Barack Obama', 'Joe Biden']];

    let correctAnswers = ['Hogwarts', '7', 'Ibrahimovic´', 'Darth Vader', 'Barack Obama'];




    /*Funktion för att köra hela deltestet. Funktionen är kopplat till en eventlyssnare.
    Vid klick på någon av svarsalternativen kontrolleras om svaret var rätt eller ej,
    samt skriver ut ny fråga. */

    function makeChoice() {
        let clickedElement = event.target;

        // rätt svar addera 3poäng, tilldela bakgrundfärgen grön samt ta bort pointerEvents.
        if (clickedElement.innerHTML == correctAnswers[countCorrect]) {
            clickedElement.style.backgroundColor = 'green';
            score += 3;
            for (const choice of questionDivList) {
                choice.style.pointerEvents = "none";
            }
        } else {
            clickedElement.style.backgroundColor = 'red';

            for (const choice of questionDivList) {
                choice.style.pointerEvents = "none";

                if (choice.innerHTML == correctAnswers[countCorrect]) {
                    choice.style.backgroundColor = 'green';
                }
            }
        }


        countCorrect += 1;
        countAnswers += 1;

        // definerar inre knapp, som låter användaren stega mellan varje fråga inom resp deltest.
        if (countNextButton < 5) {
            let continueBtn = document.createElement('div');

            continueBtn.className = 'innerBtn';
            continueBtn.innerHTML = 'klicka här, för nästa fråga';
            content.appendChild(continueBtn);

            continueBtn.addEventListener("click", function() {
                // tilldela ny fråga och nya svarsalternativ
                for (let i = 0; i < questionDivList.length; i++) {
                    if (i == 0) {
                        questionDivList[i].innerHTML = allQuestions[countQuestions];
                        countQuestions += 1;
                    } else {
                        questionDivList[i].innerHTML = optionList[countAnswers][i-1];
                        questionDivList[i].style.backgroundColor = '';
                        questionDivList[i].style.pointerEvents = 'auto';
                        questionDivList[i].style.cursor = 'pointer';
                    }
                }

                continueBtn.remove();
                countNextButton += 1;
            });
        } else {
            let continueBtn = document.createElement('div');

            continueBtn.className = 'innerBtn';
            continueBtn.innerHTML = 'Avsluta testet';
            content.appendChild(continueBtn);

            continueBtn.addEventListener("click", function() {
                for (const div of questionDivList) {
                    div.remove();
                }
                let string = `Poäng: ${score.toString()} av maximalt ${maxScore.toString()} poäng`;

                testText.innerHTML = string;
                nextButton.style.display = 'block';
                continueBtn.remove();
            });
        }
    }


    /* Funktionen skapar strukturen för frågorna och svarsalternativ.
    lägger på ett klickevent på resp svarsalternativ och lägger till dessa i en lista.*/
    function init() {
        testText.innerHTML = '';
        for (let i = 0; i < structureList.length; i++) {
            let child = document.createElement('div');

            child.className = structureList[i];

            if (i == 0) {
                child.innerHTML = allQuestions[countQuestions];
                countQuestions += 1;
            } else {
                child.innerHTML = optionList[countAnswers][i-1];
            }

            testText.appendChild(child);
            questionDivList.push(child);
            child.addEventListener("click", makeChoice);
        }
    }


    function getScore() {
        return score;
    }


    function reset() {
        countCorrect = 0;
        countQuestions = 0;
        countAnswers = 0;
        score = 0;
        countNextButton = 1;
        questionDivList = [];
        let btn = document.getElementsByClassName('innerBtn')[0];

        if (typeof(btn) != 'undefined') {
            btn.remove();
        }
    }


    return {
        init: init,
        getScore: getScore, //() => score,
        reset: reset,
    };
})();
