var friends = new Object();

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
