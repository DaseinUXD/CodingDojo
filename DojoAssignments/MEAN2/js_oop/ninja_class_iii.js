class Ninja {
    constructor(name) {
        this.name = name;
        this.health = 100;
        this.speed = 3;
        this.strength = 3;
    }
    
    sayName() {
        console.log(this.name);
    }
    
    showStats() {
        console.log(this.name, this.health, this.strength, this.speed);
    }
    
    drinkSake() {
        this.health += 10;
        console.log(this.health);
    }
}

class Sensei extends Ninja {
    constructor(name) {
        super(name);
        this.health = 200;
        this.speed = 10;
        this.strength = 10;
    }
    speakWisdom() {
        this.drinkSake();
        console.log('some cute little quip');
        return this;
    }
    
    
}



const ninja_01 = new Ninja('jet li');
const ninja_02 = new Ninja('chow yun fat');
const superSensi = new Sensei('bruce lee');
superSensi.speakWisdom();
superSensi.showStats();

ninja_01.sayName();
ninja_02.sayName();
ninja_01.showStats();
ninja_02.showStats();
ninja_01.drinkSake();
ninja_02.drinkSake();
ninja_01.showStats();
ninja_02.showStats();
// function Ninja(name) {
//     this.name = name;
//     this.health = 100;
//     var speed = 3;
//     var strength = 3;
//     this.sayName = function () {
//         console.log(this.name);
//         return this;
//     };
//     this.showStats = function () {
//         console.log(this.name, strength, speed, this.health);
//         return this;
//     };
//     this.drinkSake = function () {
//         this.health += 10;
//         console.log(this.health);
//         return this;
//     };
//     this.punch = function (punchedNinja) {
//         if (punchedNinja instanceof Ninja) {
//             if (punchedNinja !== this) {
//                 punchedNinja.health -= 5;
//                 return this;
//             }
//         }
//         return this;
//
//     };
//     this.kick = function (kickedNinja) {
//         if (kickedNinja instanceof Ninja) {
//             if (kickedNinja !== this) {
//                 s = this.strength;
//                 k_d = 6 * 15;
//                 kickedNinja.health -= k_d;
//                 return this;
//             }
//         }
//         return this;
//
//     };
// }
//
