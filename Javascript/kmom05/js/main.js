(function () {
    'use strict';

    let browserHeight = window.innerHeight;
    let browserWidth = window.innerWidth;
    let box1 = document.getElementById('box1');

    // Initiate box attributevalue
    let boxHeight = box1.offsetHeight;
    let boxWidth = box1.offsetWidth;
    let boxPosY = parseInt(window.getComputedStyle(box1).top);
    let boxPosX = parseInt(window.getComputedStyle(box1).left);




    // uppgift 1.1
    function emptyGreenBox() {
        // function returns the browsers height and height, width,position(x,y) for the box1 object.
        console.log(` webbläsarens höjd är ${browserHeight}px`);
        console.log(` webbläsarens bredd är ${browserWidth}px`);
        console.log(`boxens höjd är ${boxHeight}px`);
        console.log(`boxens bredd är ${boxWidth}px`);
        console.log(`boxens vertikala position är ${boxPosY}px`);
        console.log(`boxens horisontella position är ${boxPosX}px`);
    }


    // uppgift 1.2
    function moveBox(box1) {
        browserHeight = window.innerHeight;
        browserWidth = window.innerWidth;
        boxHeight = box1.offsetHeight;
        boxWidth = box1.offsetWidth;

        box1.style.top = (browserHeight / 2) - (boxHeight / 2);
        box1.style.left = (browserWidth / 2) - (boxWidth / 2);
    }


    // uppgift 2.1-2.2
    function borderToggle() {
        event.target.classList.toggle('selected');
    }
    box1.addEventListener('click', borderToggle);


    // uppgift 2.3
    function getAllSelected() {
        return document.getElementsByClassName('selected');
    }

    function toggleCircle() {
        let allSelected = getAllSelected();

        for (let i = 0; i < allSelected.length; i++) {
            allSelected[i].classList.toggle('circle');
        }
    }


    // 2.4 Öka/minska storlek
    function changeSeize(key) {
        let allSelected = getAllSelected();

        //console.log(key);
        for (let i = 0; i < allSelected.length; i++) {
            let currentElement = allSelected[i];
            //let attributeStyle = window.getComputedStyle(currentElement);

            if (key == 'q') {
                currentElement.style.height = `${currentElement.offsetHeight + 10}px`;
                currentElement.style.width = `${currentElement.offsetWidth + 10}px`;
                moveBox(currentElement);
            } else {
                currentElement.style.height = `${currentElement.offsetHeight - 10}px`;
                currentElement.style.width = `${currentElement.offsetWidth - 10}px`;
                moveBox(currentElement);
            }
        }
    }

    //2.5 Byt Färg
    function changeColor() {
        let allSelected = getAllSelected();

        for (let i = 0; i < allSelected.length; i++) {
            let tempStyle = getComputedStyle(allSelected[i]);
            let currentColor = tempStyle.getPropertyValue('background-color');

            if (currentColor == 'rgb(0, 128, 0)') {
                allSelected[i].style.backgroundColor = 'yellow';
            } else if (currentColor == 'rgb(255, 0, 0)') {
                allSelected[i].style.backgroundColor = 'blue';
            } else if (currentColor == 'rgb(0, 0, 255)') {
                allSelected[i].style.backgroundColor = 'green';
            } else {
                allSelected[i].style.backgroundColor = 'red';
            }
        }
    }

    // random position till uppgift 3.1
    function randomPosition(clone) {
        browserHeight = window.innerHeight;
        browserWidth = window.innerWidth;
        boxHeight = clone.offsetHeight;
        boxWidth = clone.offsetWidth;

        clone.style.top = Math.floor(Math.random() * (browserHeight - boxHeight ) ) + 'px';
        clone.style.left = Math.floor(Math.random() * (browserWidth - boxWidth )) + 'px';
    }


    // förändrar z-index till uppgift 3.1
    function changeZ(clone, amount) {
        let styles = window.getComputedStyle(clone);
        let defaultZ = amount > 0 ? "1" : "-1";

        if (styles.zIndex == 'auto') {
            clone.style.zIndex = defaultZ;
        } else {
            clone.style.zIndex = (parseInt(styles.zIndex) + amount).toString();
        }
    }

    // uppgift 3.1
    function duplicateElement() {
        let allSelected = document.querySelectorAll('.selected');
        let body = document.getElementsByTagName('body')[0];
        //let color = ['green','yellow','red','blue'];
        //let shape = ['box','circle'];
        //console.log(color[Math.floor(Math.random() * color.length)]);

        for (let i = 0; i < allSelected.length; i++) {
            let clone = allSelected[i].cloneNode();

            clone.removeAttribute('id');
            body.appendChild(clone);

            //clone.style.backgroundColor = color[Math.floor(Math.random() * color.length)];
            //clone.classList.add(shape[Math.floor(Math.random() * shape.length)]);

            changeZ(clone, 1);
            randomPosition(clone);
            clone.addEventListener('click', borderToggle);

            console.log(getComputedStyle(clone).getPropertyValue('z-index'));
        }
        console.log(`${allSelected.length}element skapades `);
    }



    // 3.2 flytta elementet i z-led
    function changeZindex(key) {
        let allSelected = getAllSelected();

        for (let i = 0; i < allSelected.length; i++) {
            let styles = window.getComputedStyle(allSelected[i]);

            if (key == 'a') {
                allSelected[i].style.zIndex = parseInt(styles.zIndex) + 1;
            } else {
                allSelected[i].style.zIndex -= 1;
            }
            //console.log(allSelected[i].style.zIndex);
            allSelected[i].addEventListener('click', borderToggle);
        }
    }


    // 3.3 radera element
    function removeElement() {
        let allSelected = document.querySelectorAll('.selected');
        let body = document.body;

        for (let i = 0; i < allSelected.length; i++) {
            let child = allSelected[i];

            body.removeChild(child);
            child.addEventListener('click', borderToggle);
        }
    }


    // 3.4 Flytta element

    let selectedElements = getAllSelected();

    document.addEventListener('keydown', function(event) {
        let key = event.key;
        let step = 5;
        //console.log(`du tryckte på knappen ${key}`);

        for (let i = 0; i < selectedElements.length; i++) {
            let node = selectedElements[i];
            let styles = window.getComputedStyle(node);
            let left = parseInt(styles.left);
            let top = parseInt(styles.top);

            //console.log(`vänster pos ${left} top pos${top}`);
            switch (key) {
                case 'ArrowUp':
                    event.preventDefault();
                    //console.log(node.style.top);
                    if (top - step < 2) {
                        break;
                    } else {
                        node.style.top = (top - step) + 'px';
                    }
                    //console.log(node.style.top);
                    break;

                case 'ArrowDown':
                    event.preventDefault();
                    if (top + step > (browserHeight - boxHeight - 2)) {
                        break;
                    } else {
                        node.style.top = (top + step) + 'px';
                    }
                    //console.log(node.style.top);
                    break;

                case 'ArrowLeft':
                    event.preventDefault();
                    if (left -step < 2) {
                        break;
                    } else {
                        node.style.left = (left - step) + 'px';
                    }
                    //console.log(node.style.left);
                    break;

                case 'ArrowRight':
                    event.preventDefault();
                    if (left + step > browserWidth - boxWidth -2) {
                        break;
                    } else {
                        node.style.left = (left + step) + 'px';
                    }
                    //console.log(node.style.left);
                    break;
            }
        }
    });


    //3.5 Gör element icke valda
    function changeSelected() {
        let allSelected = document.querySelectorAll('.selected');

        for (let i = 0; i < allSelected.length; i++) {
            let node = allSelected[i];

            node.classList.remove('selected');
        }
    }



    //3.6 Gör samtliga element valda
    function makeSelected() {
        let boxClass = document.getElementsByClassName('box');

        for (let i = 0; i < boxClass.length; i++) {
            let node = boxClass[i];

            node.classList.add('selected');
        }
    }


    // 3.7 Skapa ett slumpmässigt element
    function createRandom() {
        let body = document.getElementsByTagName('body')[0];
        let color = ['green', 'yellow', 'red', 'blue'];
        let shape = ['box', 'circle'];
        let clone = box1.cloneNode();

        clone.removeAttribute('id');
        body.appendChild(clone);

        clone.style.backgroundColor = color[Math.floor(Math.random() * color.length)];
        clone.classList.add(shape[Math.floor(Math.random() * shape.length)]);
        randomPosition(clone);
        clone.addEventListener('click', borderToggle);
    }


    // 4.1
    function removeClicked() {
        // if sats för att kolla om elementet tillhör klassen box
        // om ja: lägg till i animated, tilldela style, width och ta bort.

        let body = document.body;
        let box = document.getElementsByClassName('box')[0];
        let element = event.target;

        if (box.contains(element)) {
            //console.log('klassen box');
            element.classList.add('animateSize');
            element.style.height = '2px';
            element.style.width = '2px';

            window.setTimeout(function() {
                let removedChild = body.removeChild(element);

                console.log(removedChild);
            }, 2000);
        }
    }
    document.addEventListener('dblclick', removeClicked);




    // 5.0 Egen händelse
    // klickar man på bokstaven b - väljs alla element och görs om till färgen svart.

    function makeBlack() {
        let boxClass = document.getElementsByClassName('box');

        for (let i = 0; i < boxClass.length; i++) {
            let node = boxClass[i];

            node.classList.add('selected');
            node.style.backgroundColor = 'black';
        }
    }





    // keydown event
    document.addEventListener('keydown', function(event) {
        let key = event.key;

        switch (key) {
            case 'e':
                toggleCircle();
                break;
            case 'q':
                changeSeize(key);
                break;
            case 'w':
                changeSeize(key);
                break;
            case 'r':
                changeColor();
                break;
            case 't':
                duplicateElement();
                break;
            case 'a':
                changeZindex(key);
                break;
            case 's':
                changeZindex(key);
                break;
            case 'y':
                removeElement();
                break;
            case 'u':
                changeSelected();
                break;
            case 'i':
                makeSelected();
                break;
            case 'p':
                createRandom();
                break;
            case 'b':
                makeBlack();
                break;
        }
    });
    window.addEventListener('resize', moveBox(box1));
    moveBox(box1);
    emptyGreenBox();
})();
