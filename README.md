# Mini Rummy Game

Welcome to Mini Rummy! This is a simple console-based implementation of the classic card game Rummy. The game is designed for two players, and the objective is to form sets of cards to win the game.

## Getting Started

### Prerequisites

- Computer obviously ;)
- Python

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/lafilledepondy/rummy.git
    ```

2. Navigate to the project directory:

    ```bash
    cd rummy
    ``` 

3. Run the game:

    ```bash
    py main.py
    ```

## How to Play

1. Each player is dealt a hand of 10 cards from a standard deck.
2. Players take turns drawing cards, either from the deck or the pile.
3. The goal is to form three sets of cards:
    - Two sets with three cards each
    - One set with four cards
4. A set can be either a "book" (cards of the same rank but different suits) or a "run" (a sequence of cards in the same suit).
5. After drawing a card, players must discard a card onto the pile.
6. The game continues until one player successfully forms all the required sets.

## Rules

- A player must have at least one valid "book" and one valid "run" to win.
- A "book" consists of cards of the same rank but different suits.
- A "run" is a sequence of cards in the same suit.
- During each turn, a player can choose a card from the pile or the deck to create sets.
- After selecting a card, the player must discard a card onto the pile.

## Actions

- **Move Cards (M):** Rearrange cards in your hand.
- **Pick from Pile (P):** Pick a card from the pile.
- **Take from Deck (T):** Draw a card from the deck.
- **Drop (D):** Discard a card onto the pile.
- **Sort (S):** Sort your hand in descending.
- **Close Game (C):** Attempt to close the game (win).

## Exiting the Game

- To exit the game, enter 'X' during your turn.
- Confirm your exit choice with 'Y' or 'N'.

## Author

- Gayathiri RAVENDIRANE aka lafilledepondy

## Acknowledgments

- Inspired by https://github.com/VinithaGadiraju/Rummy/blob/master/rummy_final.py