from functions import is_hit_cards, is_bet_available, is_blackjack
from classes import Card_deck, Player, Dealer

##### Playing the game #####

player_turn = False
dealer_turn = False
quit = False
playing = True
first_dealt = True

response = input(' What is your name? ')

dealer = Dealer()
player = Player()
player.name = response
cards = Card_deck()

while quit == False:
    if player.score <= 0:
        print('You are out of points! Game over!')
        quit = True
        break
    bet = 0
    while bet == 0:
        try:
            bet = int(input(f'You have {player.score} points. How many points would you like to bet? ')) #add error handling for non-int inputs
            break
        except ValueError:
            print("Oops! Enter valid number. Try again...")
     
    if is_bet_available(player.score, bet) == False:
        playing = False
    else:
        playing = True
        print(f'You bet {bet} points! Good luck!')
        statement = True

    while playing:
        while first_dealt:
            print('Great! Lets get started!')
            player.get_card(cards.deal())
            player.get_card(cards.deal())
            print(f'You have')
            player.get_hand()
            dealer.get_card(cards.deal())
            dealer.get_card(cards.deal())
            print(f"Dealer got: {dealer.hand[0][0]}")
            
            player_blackjack = is_blackjack(player.hand)
            dealer_blackjack = is_blackjack(dealer.hand)
 
            if player_blackjack and not dealer_blackjack:
                player.score += bet * 1.5 # win 1.5x bet when you get blackjack
                playing = player_turn = dealer_turn = statement = False
                print('Black Jack! You win!')
                break
            elif dealer_blackjack and not player_blackjack:
                player.score -= bet
                playing = dealer_turn = player_turn = statement = False
                print('Dealer has Black Jack! Dealer wins!')
                break
            elif dealer_blackjack and player_blackjack:
                playing = dealer_turn = player_turn = statement = False
                print('You both have Black Jack! Tie!')
                break
            elif dealer.sum <17:
                dealer_turn = True   
            first_dealt = False
            
            while True:
                response = input('Would you like to hit or stay? (h/s) ').lower()
                if is_hit_cards(response) == True:
                    player_turn = True
                    break
                elif is_hit_cards(response) == False:
                    player_turn = False
                    break
                else:
                    print('Invalid input! Try again...')
                    continue
            
            
        while playing and player_turn and player.sum <= 21:
            player.get_card(cards.deal())
            print(f"You got: {player.hand[-1][0]}")
            print(f"Your hand is now:")
            player.get_hand()
            if player.sum > 21:
                print('Bust! You lose!')
                player.score -= bet
                player_turn = playing = dealer_turn = False
                break
            else:
                while True:
                    response = input('Would you like to hit or stay? (h/s) ').lower()
                    if is_hit_cards(response) == True:
                        player_turn = True
                        break
                    elif is_hit_cards(response) == False:
                        player_turn = False
                        print(f"Dealer's hand is: ")
                        dealer.get_hand()
                        break
                    else:
                        print('Invalid input! Try again...')
                        continue
                    
            
        while dealer.sum < 17 and dealer_turn == True:
            dealer.get_card(cards.deal())
            print(f"Dealer got: {dealer.hand[-1][0]}")
            if dealer.sum > 21:
                print('Dealer hand is now:')
                dealer.get_hand()
                print('Dealer bust! You win!')
                playing = False
                player.score += bet
                break
        
        if statement == True:
            if player.sum > dealer.sum and player.sum <= 21:
                print('Dealer hand is now:')
                dealer.get_hand()
                print('Congrats! You win!')
                player.score += bet
            elif dealer.sum > player.sum and dealer.sum <= 21:
                print('Dealer hand is now:')
                dealer.get_hand()
                print('Dealer wins!')
                player.score -= bet
            elif dealer.sum == player.sum:
                print('Tie!')
            
        playing = False
        

    while True:
        response = input('Would you like to play again? (y/n) ').lower()
        if response == 'y':
            first_dealt = playing = True
            dealer.reset_hand()
            player.reset_hand()
            cards.reset_deck()
            break
        elif response == 'n':
            quit = True
            print(f'You ended with {player.score} points!')
            break
        else:
            print('Invalid input! Try again...')
            continue
