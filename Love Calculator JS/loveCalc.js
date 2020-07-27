// button listener 
var button = document.querySelector('button');

button.addEventListener('click', function(e){
var yourName = document.querySelector ("#yourName").value;
var crushName = document.querySelector ("#crushName").value;

var loveScore = Math.random();
loveScore = Math.floor(loveScore * 100) + 1 ;

// A place for % result to be printed out 
var resultNumber = document.querySelector("#resultNumber");
// A place for the following explanation to be printed out 
var explanation = document.querySelector("#explanation");
// Hiding form for result 
var hideForResult = document.querySelector('.hideForResult');
// Showing Try Again button
var tryAgain = document.querySelector('#tryAgain');
// Shortcut for result
var yourResultIs = yourName + " & " + crushName + ", your compatibility is " + loveScore + "%.";

    if (loveScore >= 70) {
        explanation.style.visibility = "visible";
        resultNumber.style.visibility = "visible";
        resultNumber.innerHTML = loveScore + "%";
        explanation.innerHTML = yourResultIs + "High change there 😏";
        hideForResult.style.display = "none";
        tryAgain.style.visibility = "visible";
    }
    else if (loveScore >= 40 && loveScore < 70) {
        explanation.style.visibility = "visible";
        resultNumber.style.visibility = "visible";
        resultNumber.innerHTML = loveScore + "%";
        explanation.innerHTML = yourResultIs + "That's not bad 🤔";
        hideForResult.style.display = "none";
        tryAgain.style.visibility = "visible";
    }
    else {
        explanation.style.visibility = "visible";
        resultNumber.style.visibility = "visible";
        resultNumber.innerHTML = loveScore + "%";
        explanation.innerHTML = yourResultIs + "ugh, as if! 🤧";
        hideForResult.style.display = "none";
        tryAgain.style.visibility = "visible";
    }
});


