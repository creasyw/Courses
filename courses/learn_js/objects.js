var friends = new Object();

// construct using "literal notation"
friends.bill = {
    firstName: "Bill",
    lastName:"Gates",
    number:"(206) 555-5555",
    address: ['Microsoft Sucks Way','Redmond','WA','98052']
};

friends.steve = {
    firstName: "Steve",
    lastName: "Jobs",
    number:"(734) 546-8903",
    address:["Much Better Than Windows", "Palo Alto", "CA", "94301"]
};

var list = function(obj) {
    for (var key in obj) {
        console.log(key);
    }
}

var search = function(name) {
    for (var key in friends) {
        if (friends[key].firstName === name) {
            console.log(friends[key]);
            return friends[key];
        }
    }
}

// another way to construct object -- General Constructor
var susan2 = new Object();
// two ways to set/access properties:
// 1. dot notation; 2.bracket notation
susan2["name"] = "Susan Jordan";
susan2.age = 24;

// -----------------
// another way of constructing object is "customized constructor"
// 3 lines required to make harry_potter
var harry_potter = new Object();
harry_potter.pages = 350;
harry_potter.author = "J.K. Rowling";

// A custom constructor for book
function Book (pages, author) {
    this.pages = pages;
    this.author = author;
}

// Use our new constructor to make the_hobbit in one line
var the_hobbit = new Book(320, "J.R.R. Tolkien");

// -----------------
// There are two approaches declearing methods of object

// 1. within the literal notation
function Circle (radius) {
    this.radius = radius;
    this.area = function () {
        return Math.PI * this.radius * this.radius;

    };
    // define a perimeter method here
    this.perimeter = function () {
        return Math.PI * this.radius * 2;
    }
};

// 2. declear general function working for objects
// here we define our method using "this", before we even introduce bob
var setAge = function (newAge) {
  this.age = newAge;
};
// now we make bob
var bob = new Object();
bob.age = 30;
// and down here we just use the method we already made
bob.setAge = setAge;
// change bob's age to 50 here
bob.setAge(50);
