// domino_set
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
    return this;
  }
  
  show() {
    console.log(this.name)
  }
  
}

class Set {
  constructor() {
    this.type = 'double-' + (sides.length - 1).toString();
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
    console.log('new set built');
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
    // console.log('playing a domino');
    if (this.hand.length === 0) {
      console.log('You have no dominoes to play; pull dominoes to build a hand.')
    }
    var played_domino;
    var temp_set = this.hand;
    // var max = this.hand.length;
    // console.log(selection);
    played_domino = temp_set.splice(domino, 1);
    this.hand = temp_set;
    // console.log(this);
    console.log(this.name,  'played the ', played_domino[0]['name']);
    return this;
    
  }
  
}


set = new Set();
console.log('Set type: ' + set.type);
set.build();
console.log('++++++++ out of the box ++++++++');
set.show();
set.shake();
console.log('++++++++ SHAKEN not SHUFFLED ++++++++');
set.show();
//
//
console.log('+++++++++ starting pile of bones to pull from ++++++++++');
console.log(set.dominoes);
// console.log('++++ and now the players ++++++');
// player_01 = new Player('bob');
// console.log();
// console.log(player_01.name);
// player_01.pull();
// //
// // console.log();
// // console.log('++++++++ remaining pile of bones ++++++++++');
// // console.log(set.dominoes);
//
// player_02 = new Player('mary');
// console.log();
// console.log(player_02.name);
// player_02.pull();
// // console.log();
// //
// // console.log('++++++++ remaining pile of bones ++++++++++');
// // console.log(set.dominoes);
// player_03 = new Player('john');
// console.log();
// console.log(player_03.name);
// player_03.pull();
// // console.log();
// //
// // console.log('++++++++ remaining pile of bones ++++++++++');
// // console.log(set.dominoes);
// player_04 = new Player('jane');
// console.log();
// console.log(player_04.name);
// player_04.pull();
// console.log();
// //
// // console.log('++++++++ remaining pile of bones ++++++++++');
// // console.log(set.dominoes);
// //
// console.log('++++++++ playing round one ++++++++++');
// player_01.play(0);
// player_02.play(0);
// player_03.play(0);
// player_04.play(0);
// console.log();
//
// console.log('++++++++ playing round two ++++++++++');
// player_01.play(0);
// player_02.play(0);
// player_03.play(0);
// player_04.play(0);
// console.log();
//
// console.log('++++++++ looking at player_01\'s remaining hand  ++++++++++');
// console.log(player_01.hand);
// console.log('++++++++ number of dominoes remaining in player_01\'s hand  ++++++++++');
// console.log(player_01.hand.length);
//
// //
// // game = new Game();
// // game.start();
// // game.addPlayer(player_01);
// // game.addPlayer(player_02);
// // game.addPlayer(player_03);
// // game.addPlayer(player_04);
//
