### Deck of Cards Exercise ###

# Your goal in this exercise is to implement two classes,
# 'Card' and 'Deck'

# Specifications:


# 'Card'
# 1. Each instance of Card should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades")
# 2. Each instance of Card should have a value ("A", "2", "3", "4'"..."K")
# 3. Card's __repr__ method should retun the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)

from random import shuffle

class Card:
    
    def __init__(self, value, suit): 
        self.value = value
        self.suit = suit
        
    
    def __repr__(self):
        # return the card's value and suit
        return f"You got a {self.value} {self.suit}"


# 'Deck'
# 1. Each instance of Deck should have a cards attribute with all 52 possible instances of Card
# 2. Deck should have an instance method called count which returns a count of how many cards remain in
# the deck
# 3. Deck's __repr__ method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", 
#  "Deck of 12 cards", etc.)
# 4. Deck should have an instance method called _deal which acepts a number and removes at most that many cards
# from the end of the deck (it may need to remove fewer if there fewer remaining cards in the deck). If there are
# no cards left it should return a ValueError with the message "All cards have been dealt"
# 5. Deck should have an instance method called shuffle which will shuffle a full deck of cards.
# If there are cards missing from the deck, this method should raise a ValueError with the message "Only
#  full decks can be shuffled". Shuffle should return the shuffled deck.


class Deck:
    
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]
        print(self.cards)
                
    def __repr__(self):
        return f"Deck of {self.count()} cards"
        
    def count(self):
        return len(self.cards)
    
    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
    
    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self, hand_size):
        return self._deal(hand_size)
    
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self

d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(5)
print(hand)

d2 = Deck()
d2.shuffle()
card2 = d2.deal_hand(10)
print(d2.count()) # 42
