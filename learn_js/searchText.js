/*jshint multistr:true */

var text = "Robin McLaurin Williams was an American actor and \
    stand-up comedian. Rising to fame with his role as the alien \
    Mork in the TV series Mork & Mindy, Williams went on to \
    establish a successful career in both stand-up comedy and \
    feature film acting.";

var myName = "Williams";

var hits = [];

for (var i=0; i<text.length; i++) {
    if (text[i] === myName[0]) {
        for (var j=i; j<i+myName.length; j++) {
            hits.push(text[j]);
        }
    }
}

if (hits.length === 0) {
    console.log("Your name wasn't found!");
} else {
    console.log(hits);
}
