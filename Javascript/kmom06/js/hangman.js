/**
 * Showing off how to display/hide parts of a SVG-image.
 */
window.Hangman = (function () {
    "use strict";
    let secret ='';
    let wordsList = ['julnisse', 'tomte', 'snögubbe', 'lejon', 'iphone', 'saffran'];

    let hangman = {
        wordlist: function() {
            console.log(wordsList);
        },

        randomIze: function() {
            let randomIndex = Math.floor(Math.random() * (wordsList.length - 1));

            //return wordsList[randomIndex];
            secret = wordsList[randomIndex];
            return secret;
        },
        peek: function() {
            return secret;
        },
        // Get all elements as their id
        partAsElement: {
            "hill": document.getElementById('hang_hill'),
            "gallow": document.getElementById('hang_construction'),
            "body": document.getElementById('hang_body'),
            "rightarm": document.getElementById('hang_rightarm'),
            "leftarm": document.getElementById('hang_leftarm'),
            "rightleg": document.getElementById('hang_rightleg'),
            "leftleg": document.getElementById('hang_leftleg'),
            "rope": document.getElementById('hang_rope'),
            "head": document.getElementById('hang_head')
        },

        // Create an array with all valid parts
        validParts: [
            "hill",
            "gallow",
            "body",
            "rightarm",
            "leftarm",
            "rightleg",
            "leftleg",
            "rope",
            "head"
        ],


        /**
         * Check if part a valid part, writes error message to console if the part is invalid.
         *
         * @param string part Name of the part to check.
         *
         * @returns boolean true if valid part, else false.
         */
        isValid: function (part) {
            if (this.validParts.indexOf(part) === -1) {
                //window.console.log("The part is not valid: " + part);
                return false;
            }
            //window.console.log("The part is valid: " + part);
            return true;
        },


        /**
         * Hide a part.
         *
         * @param string part Name of the part to hide.
         *
         * @returns void.
         */
        hide: function (part) {
            if (this.isValid(part)) {
                this.partAsElement[part].style.display = "none";
            }
        },


        /**
         * Show a part.
         *
         * @param string part Name of the part to show.
         *
         * @returns void.
         */
        show: function (part) {
            if (this.isValid(part)) {
                this.partAsElement[part].style.display = "inline";
            }
        }
    };

    // Return the object to make it visible.
    return hangman;
})();
