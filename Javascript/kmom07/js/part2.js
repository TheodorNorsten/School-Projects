// modul för deltest 2

window.part2 = (function() {
    let score = 0;
    let maxScore = 3;
    let structureList = ['question', 'top', 'middle', 'bottom', 'under'];
    let testText = document.getElementsByClassName('quiz')[0];
    let content = document.getElementsByClassName('content')[0];
    let optionList = ['buzz', 'fizzBuzz', 'fizz'];
    let questionDivList = [];
    let nextButton = document.getElementById('next');


    function numbSequence() {
        let max = 2000;
        let serieRange = 5;
        let sequenceString = '';
        let randomStart = Math.floor(Math.random() * (max));
        let nextInt = randomStart + 5;

        sequenceString = 'Vilken sekvens fortsätter serien?\n';
        sequenceString += randomStart + ', ';

        for (let i = 1; i < serieRange; i++) {
            let nextNumb = randomStart + i;

            sequenceString += nextNumb + ', ';
        }
        sequenceString += '?';
        optionList.push(nextInt.toString());

        return sequenceString;
    }


    function fizzChoice() {
        let clickedElement = event.target;
        //console.log(clickedElement);
        let correctAnswer = '';
        let nextInt = parseInt(questionDivList[questionDivList.length - 1].innerHTML);

        // identiferar rätt svar.
        if (nextInt % 3 == 0 && nextInt % 5 == 0) {
            correctAnswer = 'fizzbuzz';
        } else if (nextInt % 3 == 0) {
            correctAnswer = 'fizz';
        } else if (nextInt % 5 == 0) {
            correctAnswer = 'buzz';
        } else {
            correctAnswer = nextInt.toString();
        }

        // kontrollerar användarens svar
        // om rätt svar.
        if (clickedElement.innerHTML == correctAnswer) {
            clickedElement.style.backgroundColor = 'green';
            score += 3;
            //window.totalScore += 3;
            for (const choice of questionDivList) {
                choice.style.pointerEvents = "none";
            }
        } else {
            clickedElement.style.backgroundColor = 'red';
            for (const choice of questionDivList) {
                choice.style.pointerEvents = "none";

                if (choice.innerHTML == correctAnswer) {
                    choice.style.backgroundColor = 'green';
                }
            }
        }

        // visa resultat för deltest.
        let continueBtn = document.createElement('div');

        continueBtn.className = 'innerBtn';
        continueBtn.innerHTML = 'klicka, för att avsluta testet';
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


    function init() {
        testText.innerHTML = '';
        let countTopPos = 0;
        //let nextInt = 0;

        for (let i = 0; i < structureList.length; i++) {
            let child = document.createElement('div');

            child.className = structureList[i];

            if (i == 0) {
                child.innerHTML = numbSequence();
                testText.appendChild(child);
            } else {
                child.innerHTML = optionList[i-1];
                testText.appendChild(child);
                child.style.height = `${child.offsetHeight - 20}px`;
                child.style.top = `${parseInt(window.getComputedStyle(child).top) - countTopPos}px`;
                countTopPos += 20;
            }
            questionDivList.push(child);
            child.addEventListener("click", fizzChoice);
        }
    }


    function getScore() {
        return score;
    }

    function reset() {
        score = 0;
        questionDivList = [];
        optionList = ['buzz', 'fizzBuzz', 'fizz'];
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
