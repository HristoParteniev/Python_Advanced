from enum import Enum
from random import shuffle

class BlackJackCard:

    def __init__(self,value,suit):
 
        self.value = value
        self.suit = suit

    @property
    def soft(self):
        if self.value[1] != 11:
            return self.value[1]
        else:
            return 1

    @property
    def hard(self):
        if self.value[1] != 11:
            return self.value[1]
        else:
            return 11

    def __str__(self):
        return "{} {}".format(self.value[0], self.suit)

class Hand(): 

    def __init__ (self, dealer_card: BlackJackCard, *cards: BlackJackCard) -> None: 

        self.dealer_card = dealer_card 
        self._cards = list(cards) 
        

    def __str__(self) -> str: 
        ", ".join(map(str, self._cards)) 
 

    def __repr__(self) -> str: 
        return (
        f"{self.__class__.__name__}" 
        f"({self.dealer_card!r}, " 
        f"{', '.join(map(repr, self._cards))}") 


class Hand_Lazy(Hand):

    @property 
    def total(self) -> int: 
        delta_soft = max(c.soft - c.hard for c in self._cards) 
        hard_total = sum(c.hard for c in self._cards) 
        if hard_total + delta_soft <= 21: 
            return hard_total + delta_soft 
        return hard_total 
 
    @property
    def card(self) -> list[BlackJackCard]:
        return self._cards 

    @card.setter 
    def card(self, aCard: BlackJackCard) -> None: 
        self._cards.append(aCard) 


    @card.deleter 
    def card(self) -> None: 
        self._cards.pop(-1) 


class Suit(dict,Enum):

    suits = {"Spade" :"♠", "Heart" :"♥", "Diamond" :"♦", "Club" :"♣"}
    

class CardValue():    
    
    values = {"Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" :7
    , "Eight" : 8, "Nine" : 9, "Ten" : 10, "Jack" : 10, "Queen" : 10, "King" : 10, "Ace" : 11}

   
        
class Deck():

    def __init__(self):

        self._cards = [
            BlackJackCard(value, suit) for value in CardValue.values.items() for suit in Suit.suits.values()
        ]

        shuffle(self._cards)

    def __str__(self):        
        return ', '.join(map(str, self._cards))
        


card1 = BlackJackCard(list(CardValue.values.items())[0], Suit.suits['Club'])
card2 = BlackJackCard(list(CardValue.values.items())[9], Suit.suits['Spade'])
card3 = BlackJackCard(list(CardValue.values.items())[4], Suit.suits['Diamond'])
card4 = BlackJackCard(list(CardValue.values.items())[8], Suit.suits['Heart'])
card5 = BlackJackCard(list(CardValue.values.items())[10], Suit.suits['Heart'])

print(f"printing card1 .... {card1}")
print(card2)
print(card3)
print(card4)
print(card5)
d = Deck()
bjc = BlackJackCard(('Ace', 11), "♠")

print("print deck")
print(d)
h = Hand_Lazy(d._cards.pop(), d._cards.pop(), d._cards.pop())  
print(h.total)

