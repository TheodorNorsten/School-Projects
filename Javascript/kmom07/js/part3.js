// modul för deltest 3

window.part3 = (function() {
    let score = 0;
    let indexIntelligence = 0.5;
    let testText = document.getElementsByClassName('quiz')[0];
    let content = document.getElementsByClassName('content')[0];

    // dic med div-element för varje flagga.
    const availableFlags = {
        armenia: {
            html: `<div class="flag armenia">
                  <div class="top"></div
                  ><div class="middle"></div>
                  <div class="bottom"></div>
                  </div>`,
            name: 'Armenia',
        },
        bolivia: {
            html: `<div class="flag bolivia">
                  <div class="top"></div>
                  <div class="middle"></div>
                  <div class="bottom"></div>
                  </div>`,
            name: 'Bolivia',
        },
        sweden: {
            html: `<div class="flag sweden">
                  <div class="vertical"></div>
                  <div class="horizontal">
                  </div>`,
            name: 'Sweden',
        },
        norway: {
            html: `<div class="flag norway">
                  <div class="verticalinner"></div>
                  <div class="verticaloutter"></div>
                  <div class="horizontalinner"></div>
                  <div class="horizontaloutter"></div>
                  </div>`,
            name: 'Norway',
        },
        bulgaria: {
            html: `<div class="flag bulgaria">
                  <div class="top"></div>
                  <div class="middle"></div>
                  <div class="bottom"></div>
                  </div>`,
            name: 'Bulgaria',
        },
        gabon: {
            html: `<div class="flag gabon">
                  <div class="top"></div>
                  <div class="middle"></div>
                  <div class="bottom"></div>
                  </div>`,
            name: 'Gabon',
        },
        lithuania: {
            html: `<div class="flag lithuania">
                  <div class="top"></div>
                  <div class="middle"></div>
                  <div class="bottom"></div>
                  </div>`,
            name: 'Lithuania',
        },
        russia: {
            html: `<div class="flag russia">
                  <div class="top"></div>
                  <div class="middle"></div>
                  <div class="bottom"></div>
                  </div>`,
            name: 'Russia',
        },
        austria: {
            html: `<div class="flag austria">
                  <div class="top"></div>
                  <div class="middle"></div>
                  <div class="bottom"></div>
                  </div>`,
            name: 'Austria',
        },

    };

    const quizFlags = [
        availableFlags.armenia,
        availableFlags.bolivia,
        availableFlags.sweden,
        availableFlags.norway,
        availableFlags.bulgaria,
        availableFlags.gabon,
        availableFlags.lithuania,
        availableFlags.russia,
        availableFlags.austria,
    ];

    /* funktionen skriver ut flaggorna, vänder dessa samt skapar ett klickevent till de.
    funktionen är kopplat till ett klickevent.*/
    function hideFlags(event) {
        event.target.remove();
        testText.innerHTML = '';
        for (const flag of quizFlags) {
            testText.innerHTML += flag.html;
        }
        // slumpar fram ordningen för den ordnade listan av flaggor.
        const randomizedFlags = quizFlags.slice(0);

        for (let i = randomizedFlags.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));

            [randomizedFlags[i], randomizedFlags[j]] = [randomizedFlags[j], randomizedFlags[i]];
        }


        // efter 5 sekunder ska varje flagga flippas.
        setTimeout(() => {
            const list = content.appendChild(document.createElement('ol'));

            list.classList.add('flag-list');
            for (const flag of randomizedFlags) {
                list.appendChild(document.createElement('li')).innerText = flag.name;
            }
            for (let i = 0; i < quizFlags.length; i++) {
                const flagElement = testText.children[i];

                flagElement.classList.add('substitute');
            }
        }, 5000);

        let countFLag = 0;
        let correctAnswer = 0;
        let nameList = document.getElementsByTagName('li');

        for (let i = 0; i < quizFlags.length; i++) {
            const flagElement = testText.children[i];

            flagElement.addEventListener('click', function() {      //event =>
                flagElement.classList.remove('substitute');
                let flagName = flagElement.className.split(' ')[1];

                // rätt svar.
                if (flagName == randomizedFlags[countFLag].name.toLowerCase()) {
                    nameList[countFLag].style.backgroundColor = 'green';
                    countFLag += 1;
                    correctAnswer += 1;
                    score += 1;

                    if (correctAnswer == quizFlags.length) {
                        // visa resultat för deltest.
                        let continueBtn = document.createElement('div');
                        let stringTwo = `Alla Rätt! klicka här,
                        för att  avlsuta testet och se slutresultat`;

                        continueBtn.className = 'innerBtn';
                        continueBtn.innerHTML = stringTwo;
                        content.appendChild(continueBtn);
                        continueBtn.addEventListener("click", function() {
                            continueBtn.remove();
                            testText.innerHTML = '';
                            // beräknar och skriver ut intelligensen.
                            let sumScore = window.Test.totalScore() + score;
                            let ratioMax = sumScore / window.Test.maximalScore();
                            let diff = (ratioMax - indexIntelligence) * 100;
                            let intelligence = Math.round((100 + diff) * 100) / 100;
                            let string = `Tack för medverkan!\n
                            Slutgiltigt resultat: Din intelligens är ${intelligence}
                            av maximalt 150
                            Välkommen åter.`;

                            testText.innerHTML = string;
                            let temp = document.getElementsByClassName('flag-list')[0];

                            temp.remove();
                        });
                    }
                } else {
                    nameList[countFLag].style.backgroundColor = 'red';
                    for (let i = 0; i < quizFlags.length; i++) {
                        const flagElement = testText.children[i];

                        flagElement.style.pointerEvents = 'none';
                    }
                    // visa resultat för deltest.
                    let continueBtn = document.createElement('div');

                    continueBtn.className = 'innerBtn';
                    continueBtn.innerHTML = 'Fel, klicka för att Avsluta testet och se resultat.';
                    content.appendChild(continueBtn);

                    continueBtn.addEventListener("click", function() {
                        continueBtn.remove();
                        testText.innerHTML = '';
                        // beräknar och skriver ut intelligensen.
                        let sumScore = window.Test.totalScore() + score;
                        let ratioMax = sumScore / window.Test.maximalScore();
                        let diff = (ratioMax - indexIntelligence) * 100;
                        let intelligence = Math.round((100 + diff) * 100) / 100;
                        let string = `Tack för medverkan!\n
                        Slutgiltigt resultat: Din intelligens är ${intelligence} av maximalt 150\n
                        Välkommen åter.`;

                        testText.innerHTML = string;
                        let temp = document.getElementsByClassName('flag-list')[0];

                        temp.remove();
                    });
                }
            });
        }
    }


    /*init funktionen. skriver ut en förklarande text.
    skapar ett klickevent för att visa flaggorna.*/
    function init() {
        let string = `9 Flaggor kommer visas i 5 sekunder\n, kom ihåg dess position
        och välj flaggorna i rätt ordning enligt listan till höger.`;

        testText.innerHTML = string;
        let continueBtn = document.createElement('div');

        continueBtn.className = 'innerBtn';
        continueBtn.innerHTML = 'klicka här, för att starta testet';
        content.appendChild(continueBtn);
        continueBtn.addEventListener("click", hideFlags);
    }

    function getScore() {
        return score;
    }

    function reset() {
        score = 0;
        let btn = document.getElementsByClassName('innerBtn')[0];

        if (typeof(btn) != 'undefined') {
            btn.remove();
        }
        let temp = document.getElementsByClassName('flag-list')[0];

        if (typeof(temp) != 'undefined') {
            temp.remove();
        }
    }

    return {
        init: init,
        getScore: getScore, //() => score,
        reset: reset,
    };
})();
