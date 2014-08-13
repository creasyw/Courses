var slaying = true;
var youHit = Math.floor(Math.random()*2);
var damageThisRound = Math.floor(Math.random()*5 + 1);
var totalDamage = 0;

while (slaying) {
    if (youHit === 1) {
        console.log("Congrts, you hit it!");
        totalDamage += damageThisRound;
        if (totalDamage>=4) {
            console.log("The dragon is dead...WWF will hunt you down!");
            slaying = false;
        }
        damageThisRound = Math.floor(Math.random()*5 + 1);
    } else {
        console.log("Ohhhh...");
    }
    youHit = Math.floor(Math.random()*2);
}
