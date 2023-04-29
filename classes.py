from random import randint

##### Classes #####

class Card_deck:
    full_deck = [['A Hearts', 1], ['A Diamonds', 1], ['A Spades', 1], ['A Clubs', 1], ['2 Hearts', 2], ['2 Diamonds', 2], ['2 Spades', 2], ['2 Clubs', 2], ['3 Hearts', 3], ['3 Diamonds', 3], ['3 Spades', 3], ['3 Clubs', 3], ['4 Hearts', 4], ['4 Diamonds', 4], ['4 Spades', 4], ['4 Clubs', 4], ['5 Hearts', 5], ['5 Diamonds', 5], ['5 Spades', 5], ['5 Clubs', 5], ['6 Hearts', 6], ['6 Diamonds', 6], ['6 Spades', 6], ['6 Clubs', 6], ['7 Hearts', 7], ['7 Diamonds', 7], ['7 Spades', 7], ['7 Clubs', 7], ['8 Hearts', 8], ['8 Diamonds', 8], ['8 Spades', 8], ['8 Clubs', 8], ['9 Hearts', 9], ['9 Diamonds', 9], ['9 Spades', 9], ['9 Clubs', 9], ['10 Hearts', 10], ['10 Diamonds', 10], ['10 Spades', 10], ['10 Clubs', 10], ['J Hearts', 10], ['J Diamonds', 10], ['J Spades', 10], ['J Clubs', 10], ['Q Hearts', 10], ['Q Diamonds', 10], ['Q Spades', 10], ['Q Clubs', 10], ['K Hearts', 10], ['K Diamonds', 10], ['K Spades', 10], ['K Clubs', 10]]
    def __init__(self):
        self.card_delt = ''
        self.cards_out = []
    def deal (self):
        self.card_delt = self.full_deck[randint(0, len(self.full_deck)-1)]
        self.cards_out.append(self.card_delt)
        self.full_deck.remove(self.card_delt)
        return self.card_delt
    def reset_deck(self):
        self.cards_out = []
        self.card_delt = ''
        self.full_deck = [['A Hearts', 1], ['A Diamonds', 1], ['A Spades', 1], ['A Clubs', 1], ['2 Hearts', 2], ['2 Diamonds', 2], ['2 Spades', 2], ['2 Clubs', 2], ['3 Hearts', 3], ['3 Diamonds', 3], ['3 Spades', 3], ['3 Clubs', 3], ['4 Hearts', 4], ['4 Diamonds', 4], ['4 Spades', 4], ['4 Clubs', 4], ['5 Hearts', 5], ['5 Diamonds', 5], ['5 Spades', 5], ['5 Clubs', 5], ['6 Hearts', 6], ['6 Diamonds', 6], ['6 Spades', 6], ['6 Clubs', 6], ['7 Hearts', 7], ['7 Diamonds', 7], ['7 Spades', 7], ['7 Clubs', 7], ['8 Hearts', 8], ['8 Diamonds', 8], ['8 Spades', 8], ['8 Clubs', 8], ['9 Hearts', 9], ['9 Diamonds', 9], ['9 Spades', 9], ['9 Clubs', 9], ['10 Hearts', 10], ['10 Diamonds', 10], ['10 Spades', 10], ['10 Clubs', 10], ['J Hearts', 10], ['J Diamonds', 10], ['J Spades', 10], ['J Clubs', 10], ['Q Hearts', 10], ['Q Diamonds', 10], ['Q Spades', 10], ['Q Clubs', 10], ['K Hearts', 10], ['K Diamonds', 10], ['K Spades', 10], ['K Clubs', 10]]

        
class Player:
    def __init__(self, name = '', score = 100, hand = [], sum = 0):
        self.name = name
        self.score = score
        self.hand = hand
        self.sum = sum
    def get_score(self, score):
        self.score += score
    def get_card(self, card):
        self.hand.append(card)
        self.sum += int(card[1])
    def get_hand(self):
        print([i[0] for i in self.hand])
    def reset_hand(self):
        self.hand = []
        self.sum = 0
    
class Dealer:
    def __init__(self, name = 'Dealer', hand = [], sum = 0):
        self.name = name
        self.hand = hand
        self.sum = sum
    def get_card(self, card):
        self.hand.append(card)
        self.sum += int(card[1])
    def get_hand(self):
        print([i[0] for i in self.hand])
    def reset_hand(self):
        self.hand = []
        self.sum = 0