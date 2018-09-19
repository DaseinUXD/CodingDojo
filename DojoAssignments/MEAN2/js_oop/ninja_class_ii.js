function Ninja(name) {
    this.name = name;
    this.health = 100;
    var speed = 3;
    var strength = 3;
    this.sayName = function () {
        console.log(this.name);
        return this;
    };
    this.showStats = function () {
        console.log(this.name, strength, speed, this.health);
        return this;
    };
    this.drinkSake = function () {
        this.health += 10;
        console.log(this.health);
        return this;
    };
    this.punch = function (punchedNinja) {
        if (punchedNinja instanceof Ninja) {
            if (punchedNinja !== this) {
                punchedNinja.health -= 5;
                return this;
            }
        }
        return this;
        
    };
    this.kick = function (kickedNinja) {
        if (kickedNinja instanceof Ninja) {
            if (kickedNinja !== this) {
                s = this.strength;
                k_d = 6 * 15;
                kickedNinja.health -= k_d;
                return this;
            }
        }
        return this;
        
    };
}

var ninja_01 = new Ninja('Chow Yun Fat');
var ninja_02 = new Ninja('Jet Li');
ninja_01.sayName();
ninja_01.showStats();
ninja_01.drinkSake();
ninja_02.sayName();
ninja_01.punch(ninja_02);
ninja_02.showStats();
ninja_02.drinkSake();
ninja_02.showStats();
ninja_01.kick(ninja_02);
ninja_02.showStats();
