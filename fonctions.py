# fonctions.py

import random
from shutil import move
import sys


deck_of_cards = {'1 ♤': 1, '2 ♤': 2, '3 ♤': 3,  '4 ♤': 4, '5 ♤': 5, 
                 '6 ♤': 6, '7 ♤': 7, '8 ♤': 8, '9 ♤': 9, '10 ♤': 10, 
                 '11 ♤': 11, '12 ♤': 12, '13 ♤': 13, 

                 '1 ◆': 1, '2 ◆': 2, '3 ◆': 3,  '4 ◆': 4, '5 ◆': 5, 
                 '6 ◆': 6, '7 ◆': 7, '8 ◆': 8, '9 ◆': 9, '10 ◆': 10, 
                 '11 ◆': 11, '12 ◆': 12, '13 ◆': 13, 

                 '1 ❤': 1, '2 ❤': 2, '3 ❤': 3,  '4 ❤': 4, '5 ❤': 5, 
                 '6 ❤': 6, '7 ❤': 7, '8 ❤': 8, '9 ❤': 9, '10 ❤': 10, 
                 '11 ❤': 11, '12 ❤': 12, '13 ❤': 13, 

                 '1 ♧': 1, '2 ♧': 2, '3 ♧': 3,  '4 ♧': 4, '5 ♧': 5, 
                 '6 ♧': 6, '7 ♧': 7, '8 ♧': 8, '9 ♧': 9, '10 ♧': 10, 
                 '11 ♧': 11, '12 ♧': 12, '13 ♧': 13} 

suit_mapping = {
    '❤': 'h',
    '◆': 'd',
    '♤': 's',
    '♧': 'c'
}

deck = []

pile = []

players_hands = []

MAX_CARDS_PER_PLAYER = 11


def shuffled(cards):
    cards_list = list(cards.keys())
    random.shuffle(cards_list) 
    return {card: deck_of_cards[card] for card in cards_list}

def sort_cards(cards):
    return sorted(cards, key=lambda card: deck_of_cards[card])

def draw_card(cards):
    if not cards:
        raise ValueError("The deck is empty.")
    drawn_card = cards.pop()
    print(f"Drawn card: {drawn_card}")
    return drawn_card

def find_seq_of_3(hand_card):
    sequences = []

    for i in range(len(hand_card) - 2):
        card1 = hand_card[i].split()
        card2 = hand_card[i + 1].split()
        card3 = hand_card[i + 2].split()

        rank1 = int(card1[0])
        rank2 = int(card2[0])
        rank3 = int(card3[0])

        if (rank2 == rank1 + 1
            and rank3 == rank2 + 1
            and card1[1] == card2[1] == card3[1]
        ):
            sequences.append([hand_card[i], hand_card[i + 1], hand_card[i + 2]])

    return sequences

def find_seq_of_4(hand_card):
    sequences = []

    for i in range(len(hand_card) - 3):
        card1 = hand_card[i].split()
        card2 = hand_card[i + 1].split()
        card3 = hand_card[i + 2].split()
        card4 = hand_card[i + 3].split()

        rank1 = int(card1[0])
        rank2 = int(card2[0])
        rank3 = int(card3[0])
        rank4 = int(card4[0])

        if (rank2 == rank1 + 1
            and rank3 == rank2 + 1 and rank4 == rank3 + 1
            and card1[1] == card2[1] == card3[1] == card4[1]
        ):
            sequences.append([hand_card[i], hand_card[i + 1], hand_card[i + 2], hand_card[i + 3]])

    return sequences

def find_book_of_3(hand_card):
    rank = []

    for i in range(len(hand_card) - 2):
        card1 = hand_card[i].split()
        card2 = hand_card[i + 1].split()
        card3 = hand_card[i + 2].split()

        rank1 = int(card1[0])
        rank2 = int(card2[0])
        rank3 = int(card3[0])

        if (rank2 == rank3 == rank1
            and card1[1] != card2[1] != card3[1]
        ):
            temp = [hand_card[i], hand_card[i + 1], hand_card[i + 2]]
            if (temp not in rank):
                rank.append(temp)

    return rank

def find_book_of_4(hand_card):
    rank = []

    for i in range(len(hand_card) - 3):
        card1 = hand_card[i].split()
        card2 = hand_card[i + 1].split()
        card3 = hand_card[i + 2].split()
        card4 = hand_card[i + 3].split()

        rank1 = int(card1[0])
        rank2 = int(card2[0])
        rank3 = int(card3[0])
        rank4 = int(card4[0])


        if (rank2 == rank3 == rank1 == rank4
            and card1[1] != card2[1] != card3[1] != card4[1]
        ):
            temp = [hand_card[i], hand_card[i + 1], hand_card[i + 2], hand_card[i + 3]]
            if (temp not in rank):
                rank.append(temp)

    return rank

def distribute_cards(cards_per_player, cards):
    cards_list = list(cards.keys())
    
    local_players_hands = [[] for _ in range(2)]

    for _ in range(cards_per_player):
        for i in range(2):
            card = draw_card(cards_list)
            local_players_hands[i].append(card)

    players_hands[:] = local_players_hands
    deck.extend(cards_list)

def drop_card(player_name):
    print("\nEnter the card you want to remove\n(in the format: ('2 ◆' <=> '2 d'; '2 ❤ ' <=> '2 h'; '2 ♧' <=> '2 c'; '2 ♤' <=> '2 s'): ")
    card_to_remove = input(">>> ")
    
    rcard = card_to_remove.split()
    for shorthand, full_suit in suit_mapping.items():
        for i in range(len(rcard)):
            rcard[i] = rcard[i].replace(full_suit, shorthand)
    card_to_remove = ' '.join(rcard)

    for hand in players_hands[player_name]:
        if card_to_remove in hand:
            players_hands[player_name].remove(card_to_remove)
            add_pile(card_to_remove)
            print(f"\nDropped {card_to_remove}.")    
            return card_to_remove

def display_player_hand(player_name, real_name):
    hand_str = ' ; '.join(players_hands[player_name])
    print(f"\nPlayer {real_name}'s cards are: ", hand_str)

def display_players_hands():
    for player, hand in enumerate(players_hands):
        print(f"\nPlayer {player + 1}'s Hand:")
        hand_str = ' ; '.join(hand)
        print(hand_str)

def win_game(player_name):
    hand_cards = players_hands[player_name]  
    set_counter = 0
    book_counter = 0
    
    book4 = find_book_of_4(hand_cards)
    if len(book4) != 0:
        for card in book4[0]:
            if card in hand_cards:
                hand_cards.remove(card)
        book_counter += 1
    
    seq4 = find_seq_of_4(hand_cards)
    if len(seq4) != 0:
        for card in seq4[0]:
            if card in hand_cards:
                hand_cards.remove(card)
        set_counter += 1

    book3 = find_book_of_3(hand_cards)
    if len(book3) != 0:
        for card in book3[0]:
            if card in hand_cards:
                hand_cards.remove(card)
        book_counter += 1

    seq3 = find_seq_of_3(hand_cards)
    if len(seq3) != 0:
        for card in seq3[0]:
            if card in hand_cards:
                hand_cards.remove(card)
        set_counter += 1
    
    if set_counter + book_counter == 3:
        return True

    return False

def display_pile():
    if len(pile) == 0:
        print("\nEmpty pile.")
    else:
        print("\nThe card at the top of the pile:", pile[0])

def add_pile(card):
    pile.insert(0, card)

def draw_pile():
    if len(pile) != 0:
        return pile.pop(0)
    else:
        return None

def display_deck():
    if len(deck) == 0:
        print("\nEmpty deck.")
    else:
        print("\nThe card at the top of the deck:", deck[0])

def add_deck(card):
    deck.intert(0, card)

def draw_deck():
    if len(deck) != 0:
        return deck.pop(0)
    else:
        return None

def sort_player_hand(player_name):
    players_hands[player_name] = sort_cards(players_hands[player_name])

def single_turn(player_name, real_name):
    move = None

    while True:
        display_player_hand(player_name, real_name)
        
        if move == None or move.lower() != 'p':
            display_pile()

        act = input("\n>>> Choose an action:\n"
                        "(M or m)ove Cards\n"
                        "(P or p)ick from pile\n"
                        "(T or t)ake from deck\n"
                        "(D or d)rop\n"
                        "(S or s)ort\n"
                        "(C or c)lose Game\n"
                        "(X or x)exit\n"
                        "Enter your choice: ")
        
        move = act

        # Deck = 0
        if len(deck) == 0:
            print("\nIt's a draw! No winner this time. 😔")
            input("\n>>> Press some key ")
            sys.exit()  

        #           MOVE
        elif act.lower() == 'm':
            print("\nCard to move? (e.g. '2 ◆' <=> '2 d'; '2 ❤' <=> '2 h'; '2 ♧' <=> '2 s'; '2 ♤' <=> '2 c')")
            card_to_move = input(">>> ")

            rcard = card_to_move.split()
            for shorthand, full_suit in suit_mapping.items():
                for i in range(len(rcard)):
                    rcard[i] = rcard[i].replace(full_suit, shorthand)
                card_to_move = ' '.join(rcard)

            if not card_to_move in players_hands[player_name]:
                input(f"\n>>> ERROR: {card_to_move} is not in your hand. Enter to continue ▶ ")
                continue

            print("\nWhere? before which card? (e.g. '2 ◆' <=> '2 d'; '2 ❤' <=> '2 h'; '2 ♧' <=> '2 s'; '2 ♤' <=> '2 c') ")
            move_where = input(">>> ")

            if move_where:
                rmove_where = move_where.split()
                for shorthand, full_suit in suit_mapping.items():
                    for i in range(len(rmove_where)):
                        rmove_where[i] = rmove_where[i].replace(full_suit, shorthand)
                move_where = ' '.join(rmove_where)

                if move_where not in players_hands[player_name]:
                    input(f"\n>>> {move_where} is not in your hand. Enter to continue ▶ ")
                    continue

                location = players_hands[player_name].index(move_where)
                players_hands[player_name].remove(card_to_move)
                players_hands[player_name].insert(location, card_to_move)
                print(f"\n{card_to_move} has been moved in your hand.")
                input("\n>>> Enter to continue ▶ ")
            else:
                players_hands[player_name].remove(card_to_move)
                players_hands[player_name].append(card_to_move)
                print(f"\n{card_to_move} has been moved in your hand.")
                input("\n>>> Enter to continue ▶ ")
             
        #           PICK
        elif act.lower() == 'p':
            if len(players_hands[player_name]) < MAX_CARDS_PER_PLAYER:
                c = draw_pile()
                players_hands[player_name].append(c)
                print(f"\nYou picked {c} from the pile.")
                input("\n>>> Enter to continue ▶ ")
            else:
                input("\n>>> ERROR: Cannot pick anymore. Enter to continue ▶ ")

        #           TAKE FROM DECK
        elif act.lower() == 't':
            if len(players_hands[player_name]) < MAX_CARDS_PER_PLAYER:
                c = draw_deck()
                players_hands[player_name].append(c)
                print("\nYou drew from deck:", c)
                input("\n>>> Enter to continue ▶ ")
            else:
                input("\n>>> ERROR: Cannot take anymore. Enter to continue ▶ ")

        #           DROP
        elif act.lower() == 'd':
            if len(players_hands[player_name]) == MAX_CARDS_PER_PLAYER:
                dropped_card = drop_card(player_name)  
                if dropped_card:
                    add_pile(dropped_card)
                    return False
                else: 
                    input("\n>>> The card is not found in the player's hand. Enter to continue ▶ ")
            else:
                input("\n>>> ERROR: Cannot drop a card. Player must have 11 cards total. Enter to continue ▶ ")


        #           SORT
        elif act.lower() == 's':
            sort_player_hand(player_name)
            print("\nYour hand has been sorted.")  
            input("\n>>> Enter to continue ▶ ")          

        #           CLOSE GAME
        elif act.lower() == 'c':
            if len(players_hands[player_name]) == MAX_CARDS_PER_PLAYER:
                dropped_card = drop_card(player_name)  
                if dropped_card:
                    if win_game(player_name):
                        display_player_hand(player_name)
                        return True
                    else:
                        input("\n>>> ERROR: The game is not over. Enter to continue ▶ ")
                        deck.insert(random.randint(0, len(players_hands[player_name])), dropped_card)
            else:
                input("ERROR: You do not have enough cards to close the game. Enter to continue ▶ ")
        
        elif act.lower() == 'x':
                    exit_choice = input("\n>>> Are you sure you want to exit the game? (Y(y) or N(n)): ")
                    if exit_choice.lower() == 'y':
                        print("\nIt's a draw! No winner this time. 😔")
                        input("\n>>> Press some key ")                        
                        sys.exit()  
                    else:
                        continue  

        else:
            print("Invalid action. Please choose a valid action.")
            input("\n>>> Enter to continue ▶ ")

def next_player(current_player):
    return (current_player + 1) % 2

def game(num_players=2):
    print("\n" * 100)
    print(
    """
    \033[1m\033[32mWelcome to mini Rummy\033[0m
    
    Please review the rules carefully before starting the game.

    \033[1m\033[31mRules:\033[0m
    - The game is played by 2 players.
    - Each player will receive 10 cards.
    - You must create 3 sets of cards, 2 sets with 3 cards, and 1 set with 4 cards.
    - At least one valid "book" and one valid "run" are required.
    - A book means same value but from different suits.
    - A run means sequence of number from same suit.
    - During each turn, the player should choose a card either from the pile or from the deck to create sets.
    - After selecting a card, the player must discard a card onto the pile.
    - A player wins when they have successfully formed all the required sets of cards. 
        (which include 2 sets of 3 cards each and 1 set of 4 cards, 
        and have also met the conditions of having at least one valid book and one valid run.)
    """
    )

    player1_name = input("\nEnter Player 1's name: ")
    while not player1_name.strip(): 
        print("Name cannot be empty. Please enter a valid name.")
        player1_name = input("Enter Player 1's name: ")

    player2_name = input("\nEnter Player 2's name: ")
    while not player2_name.strip():
        print("Name cannot be empty. Please enter a valid name.")
        player2_name = input("Enter Player 2's name: ")

    current_player = 0

    print("\nLET'S START THE GAME! 😎")
    input("\n>>> Enter to continue ▶ ")

    distribute_cards(10, shuffled(deck_of_cards))
    add_pile(draw_deck())

    while True:
        print("\n" * 100)
        if single_turn(current_player, player1_name if current_player==0 else player2_name):
            print("\n👾 GAME OVER !!! 👾")
            print("\n🏆🏆🏆 " + player1_name if current_player==0 else player2_name + " won the game 🏆🏆🏆")
            break
        
        current_player = next_player(current_player)
        print("\n")
        print(player1_name if current_player==0 else player2_name + " to play now.")
        input("\n>>> Enter to continue ▶ ... ")
