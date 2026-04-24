import random
logo = r"""
       .------.            _     _            _    _            _    
       |A_  _ |.          | |   | |          | |  (_)          | |   
       |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
       | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
       |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
       `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
             |  \/ K|                            _/ |                
             `------'                           |__/           
       """
def sum_total(hand):  #total the cards
    total = 0
    for n in hand:
        total += n
    return total

def rules(hand_both): #handle aces
    if 11 in hand_both:
        temp_v = hand_both.index(11)
        if sum_total(hand_both) > 21:
            hand_both[temp_v] = 1
    return hand_both

def blackjack(): #The main code
    player_hand= []
    dealer_hand = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for _ in range(2):
        card = random.choice(cards)
        player_hand.append(card)
    for _ in range(2):
            card1=random.choice(cards)
            dealer_hand.append(card1)
    print(f"Your cards: {player_hand}")
    print(f"Your current score is: {sum_total(hand=player_hand)}")
    print(f"Dealers card: [ #, {dealer_hand[1]}]")
    playing = True
    while playing:
        consent = input("Type 'y' to get another card, type 'n' to pass:\n").lower()
        if consent == "y":
            playing = True
            player_hand = rules(player_hand)
            dealer_hand = rules(dealer_hand)
            card = random.choice(cards)
            player_hand.append(card)
            print(f"Your hand is: {player_hand}")
            print(f"The dealers hand is: {dealer_hand}")
        elif consent == "n":
            while sum_total(dealer_hand) < 17:
                 dealer_hand.append(random.choice(cards))
                 player_hand = rules(player_hand)
                 dealer_hand = rules(dealer_hand)
            if sum_total(player_hand) <= 21 and sum_total(player_hand)>sum_total(dealer_hand):
                 print(f"The player wins: {sum_total(player_hand)}. The dealers hand was {dealer_hand}.")
                 playing = False
            elif sum_total(player_hand) == sum_total(dealer_hand):
                 print(f"It's a tie! The player's hand is {player_hand} and the total is {sum_total(player_hand)} and the the dealer's hand is {dealer_hand} and the total is {sum_total(dealer_hand)}")
                 playing = False
            else:
                 print(f"The dealer wins! Dealer's hand was:{dealer_hand} and total is {sum_total(dealer_hand)} and the player's hand was {player_hand}")
                 playing = False
        else:
            print("Invalid response")

def inputs():
    print(logo)
    consent = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n").lower()
    if consent == "y":
       blackjack()
    else:
        return

inputs()
