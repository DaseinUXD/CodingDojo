let suits = ['hearts', 'clubs', 'diamonds', 'spades'];
let names = ['ace',
             'deuce',
             'trey',
             'four',
             'five',
             'six',
             'seven',
             'eight',
             'nine',
             'ten',
             'jack',
             'queen',
             'king'];
let ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];

class Card {
    constructor(name, suit, rank) {
        this.name = name;
        this.suit = suit;
        this.rank = rank;
        
    }
    
    show() {
        console.log(this.name + ' of ' + this.suit, this.rank);
    }
}

class Deck {
    constructor(name) {
        this.name = name;
        this.cards = [];
        
    }
    
    static build() {
        for (var s = 0; s < suits.length; s++) {
            for (var r = 0; r < ranks.length; r++) {
                const card = new Card(`${names[r]}`, `${suits[s]}`, `${ranks[r]}`);
                deck.cards.push(card);
            }
        }
        console.log('Success, this deck is named: ' + `${deck.name}`);
    }
    
    
    count() {
        console.log('There are currently ' + `${this.cards.length}` + ' cards in this deck.');
    }
    
    shuffle() {
        var c = this.cards.length;
        var t;
        var i;
        while (c) {
            i = Math.floor(Math.random() * c--);
            t = this.cards[c];
            this.cards[c] = this.cards[i];
            this.cards[i] = t;
        }
        // console.log(t);
    }
    
    
    static reset() {
        Deck.build()
        
    }
    
    deal() {
        var pop_card;
        var temp_deck = this.cards;
        var max = this.cards.length;
        var choice = Math.floor(Math.random() * Math.floor(max));
        // console.log(choice);
        pop_card = temp_deck.pop(choice);
        console.log('The ' +
                    `${pop_card.name}` +
                    ' of ' +
                    `${pop_card.suit}` +
                    ' was dealt. There are ' +
                    `${temp_deck.length}` +
                    ' remaining in the deck');
        this.cards = temp_deck;
        return pop_card;
        // console.log(max);
        // console.log(this.cards.length)
        
    }
}


class Player {
    constructor(name) {
        this.name = name;
        this.hand = [];
    }
    
    takeCard() {
        var card = deck.deal();
        console.log('I just drew the ' + `${card.name}` + ' of ' + `${card.suit}`);
        this.hand.push(card);
        console.log(this.hand);
    }
    
    discard(card) {
        console.log('I am discarding the ' + `${card.name}` + ' of ' + `${card.suit}`);
        this.hand.pop(card);
        console.log(this.hand);
    }
    
    
}



const deck = new Deck('hoyle_bicycle');
Deck.build();
console.log('+++++OUT OF THE BOX+++++');
for (var i = 0; i < deck.cards.length; i++) {
    deck.cards[i].show();
    
}
deck.count();
deck.deal();

deck.shuffle();
// deck.reset();
console.log('+++++SHUFFLED+++++');

for (var i = 0; i < deck.cards.length; i++) {
    
    deck.cards[i].show();
}

deck.deal();
deck.deal();
deck.deal();
deck.deal();

player = new Player('bill');
console.log('Hi, my name is ' + player.name);
player.takeCard();
player.takeCard();
player.takeCard();
player.takeCard();

player2 = new Player('john');
console.log('Hi, my name is ' + player2.name);
player2.takeCard();
player2.takeCard();
player2.takeCard();
player2.takeCard();

player2.discard(player2.hand[0]);
