##### Functions #####   

def is_blackjack(hand):
    Alist = [['A Hearts', 1], ['A Diamonds', 1], ['A Spades', 1], ['A Clubs', 1]]
    for i in hand:
        if i in Alist and len(hand) == 2 and sum([i[1] for i in hand]) == 11:
            return True
        else:
            return False
def is_bet_available(available_score, bet):
    if available_score >= bet:
        return True
    else:
        print('You do not have enough points to bet that amount!')
        return False
def is_hit_cards(response):
    if response == 'h':
        return True
    elif response == 's':
        return False
    else:
        return None