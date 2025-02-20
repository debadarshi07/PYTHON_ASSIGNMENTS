import random
from dataclasses import dataclass

@dataclass
class Card:
    rank: str
    suit: str

class Deck:
    def __init__(self):
        self.cards = [ Card(rank, suit) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades'] for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] ]
        random.shuffle(self.cards)

    def deal(self, num_cards):
        hand = [self.cards.pop() for _ in range(num_cards)]
        return hand

    def remaining_cards(self):
        return len(self.cards)

def print_hand(hand):
    for card in hand:
        print(f"{card.rank} of {card.suit}")


deck = Deck()
player_hand = deck.deal(5)

print("Player's hand:")
print_hand(player_hand)

print(f"\nRemaining cards in the deck: {deck.remaining_cards()}")