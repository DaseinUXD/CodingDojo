

let sides = ['blank', 1, 2, 3, 4, 5, 6];
let seats = [
    {'seat': 'north'},
    {'seat': 'south'},
    {'seat': 'east'},
    {'seat': 'west'},
];

class Domino {
    constructor(aSide, bSide) {
        this.aSide = aSide;
        this.bSide = bSide;
        
        if (this.aSide === this.bSide) {
            this.name = 'double-' + this.aSide.toString();
        }
        else {
            this.name =
                this.aSide.toString() + ':' + this.bSide.toString() + '/' + this.bSide.toString() + ':' + this.aSide.toString();
        }
    }
    
    show() {
        console.log(this.name)
    }
    
}

class Set {
    constructor() {
        this.type = 'Double-' + (sides.length - 1).toString();
        this.dominoes = [];
        
    }
    
    build() {
        //build doubles
        
        for (var a = 0; a < sides.length; a++) {
            for (var b = a; b < sides.length; b++) {
                const domino = new Domino(sides[a], sides[b], a);
                set.dominoes.push(domino);
            }
        }
        return this;
    }
    
    show() {
        for (var i = 0; i < set.dominoes.length; i++) {
            this.dominoes[i].show();
        }
    }
    
    shake() {
        var d = this.dominoes.length;
        var t;
        var i;
        while (d) {
            i = Math.floor(Math.random() * d--);
            t = this.dominoes[d];
            this.dominoes[d] = this.dominoes[i];
            this.dominoes[i] = t;
        }
    }
    
    pulled() {
        var popped_domino;
        var temp_set = this.dominoes;
        var max = this.dominoes.length;
        var choice = Math.floor(Math.random() * Math.floor(max));
        // console.log(choice);
        popped_domino = temp_set.pop(choice);
        // console.log(popped_domino);
        this.dominoes = temp_set;
        return popped_domino
        
    }
    
}


class Player {
    constructor(name) {
        this.name = name;
        this.hand = [];
        this.dealing = false;
        
    }
    
    pull() {
        console.log('pulling');
        for (var i = 0; i < 7; i++) {
            var domino = set.pulled();
            this.hand.push(domino);
        }
        console.log(this.hand);
    }
    
    play(domino) {
        console.log('playing');
        if (this.hand.length === 0) {
            console.log('You have no dominoes to play; pull dominoes to build a hand.')
        }
        var played_domino;
        var temp_set = this.hand;
        // var max = this.hand.length;
        var selection = domino;
        console.log(selection);
        played_domino = temp_set.splice(selection, 1);
        this.hand = temp_set;
        console.log(this);
        console.log('this is the played domino', played_domino);
        return this;
        
    }
    
}


class Game {
    constructor() {
        let set = new Set();
        this.players = [];
        this.tricks = [];
    }
    
    start(){
        this.set = set.build();
        console.log(this.set);
        // this.domino_set = set.build();
    }
    
    addPlayer(player){
        this.players.push(player);
        console.log(this.players)
    }
    
}


