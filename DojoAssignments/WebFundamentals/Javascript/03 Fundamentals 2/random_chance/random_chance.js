function randomChance(quarters) {
    while (quarters > 0)
    {
        var win = 1;
        var chance = (Math.floor(Math.random()*100));
        // console.log(chance === win);
        var winnings = Math.floor((Math.random()*100)/2);
        if (win === chance) {
            quarters = quarters + winnings;
            console.log(quarters);

        }

        quarters--;
    }


}
randomChance(1000);