// Main-modulen
// Denna fil importerar innehåll från part1.js, part2.js samt part3.js.

window.Test = (function() {
    let allGames = [window.part1, window.part2, window.part3];
    let counter = -1;
    let totalScore = 0;
    let maximalScore = 30;
    let nextButton = document.getElementById('next');



    // Vid klick på knappen anropas init funktionen för aktuellt deltest.
    nextButton.addEventListener('click', function() {
        nextButton.style.display = 'none';
        if (counter != -1) {
            totalScore += allGames[counter].getScore();
        }
        if (counter == 1) {
            nextButton.remove();
        }
        counter += 1;
        let currentTest = allGames[counter];

        currentTest.init();
    });




    // Denna funktion. låter användaren starta om pågående deltest.
    function reset() {
        allGames[counter].reset();
        allGames[counter].init();
    }


    /**
     * @param function reset låter användaren börja om på aktuellt test.
     * @param number totalScore det totala poäng användaren fått från testerna.
     *@param number maximalScore det maximala antal poäng man kan få.
     * @returns reset, totalScore and maximalScore.
     */

    return {
        reset: reset,
        totalScore: () => totalScore,
        maximalScore: () => maximalScore,
    };
})();
