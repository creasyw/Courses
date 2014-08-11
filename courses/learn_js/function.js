// Define quarter here.
var quarter = function(number){
    return number/4;
};

if (quarter(12) % 3 === 0 ) {
  console.log("The statement is true");
} else {
  console.log("The statement is false");
}

var nameString = function (name) {
    return "Hi, I am" + " " + name;
};

console.log(nameString("Maldini"));

var sleepCheck = function(numHours) {
    if (numHours >= 8) {
        return "You're getting plenty of sleep! Maybe even too much!";
    } else {
        return "Get some more shut eye!";
    }
};

sleepCheck(5);
sleepCheck(10);
sleepCheck(8);
