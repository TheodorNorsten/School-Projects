(function () {
    'use strict';

    let myContent = document.getElementById('content');
    let mydate = new Date();

    myContent.innerHTML = '<h3>This is a template!</h3>';
    myContent.innerHTML+= mydate.toDateString();

    window.console.log('Sandbox is ready!');
    window.console.log(mydate.toDateString());
})();
