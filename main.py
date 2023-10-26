from fonctions import *

def main():    

    game()


    # hand1 = {
    #     '2 ♤': 2,
    #     '2 ❤': 2,
    #     '2 ♧': 2,
    #     '6 ❤': 6,
    #     '7 ❤': 7,
    #     '8 ❤': 8,
    #     '9 ❤': 9,
    #     '3 ◆': 3,
    #     '4 ◆': 4,
    #     '5 ◆': 5, 
    # }

    # hand1_sorted = sort_cards(shuffled(hand1))

    # draw_card(hand1_sorted)
    # draw_card(hand1_sorted)
    # draw_card(hand1_sorted)

    # print("Sequences of 3 cards with the same suit: ")
    # for card in find_seq_of_3(hand1_sorted):
    #     print(card)

    # print("Sequences of 4 cards with the same suit: ")
    # for card in find_seq_of_4(hand1_sorted):
    #     print(card)

    # print("Book of 3 cards:")
    # for i in find_book_of_3(hand1_sorted):
    #     print(i)

    # print("Book of 4 cards:")
    # for i in find_book_of_4(hand1_sorted):
    #     print(i)

    # print("Distributing cards to two players: ")
    # players_hands = distribute_cards(10, shuffled(deck_of_cards))
    # display_players_hands()

    # print("\n Let's simulate dropping a card") 
    # player_name = 1
    # try:
    #     dropped_card = drop_card(players_hands, player_name)
    # except ValueError as e:
    #     print(e)

    # print("\nUpdated hands: ")
    # display_players_hands()

    # print("Win_game: ", win_game(hand1_sorted))

    # distribute_cards(10, shuffled(deck_of_cards))
    # add_pile(draw_deck())
    
    # single_turn()  

    return 

if __name__ == "__main__":
    main()
