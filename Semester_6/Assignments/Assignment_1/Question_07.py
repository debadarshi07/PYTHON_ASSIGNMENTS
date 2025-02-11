import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self.cards)
        print("Deck shuffled!")

    def deal(self, num_players, cards_per_player):
        hands = {f"Player {i+1}": [] for i in range(num_players)}
        for i in range(cards_per_player):
            for player in hands:
                hands[player].append(self.cards.pop())
        return hands

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_cards(self, cards):
        self.hand.extend(cards)

    def show_hand(self):
        return f"{self.name}'s hand: {', '.join(str(card) for card in self.hand)}"

def main():
    deck = Deck()
    deck.shuffle()

    num_players = 4
    players = [Player(f"Player {i+1}") for i in range(num_players)]

    hands = deck.deal(num_players, 5)

    for i, player in enumerate(players):
        player.receive_cards(hands[f"Player {i+1}"])
        print(player.show_hand())

if __name__ == "__main__":
    main()