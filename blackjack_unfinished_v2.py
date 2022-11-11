from enum import Enum
from random import shuffle

class BlackJackCard:

    def __init__(self,value,suit):
 
      #  self.rank = CardValue.ranks
        self.value = value
        self.suit = suit

    # @property
    # def value(self):
    #     return self[0]

    # @property
    # def suit(self):
    #     return self[1]

    def __str__(self):
        return "{} {}".format(self.value[0], self.suit)  # """AttributeError: 'Deck' object has no attribute 'value'"""

    # def __setattr__(self, *ignored):
    #     raise NotImplementedError

    # def __delattr__(self, *ignored):
    #     raise NotImplementedError

class Hand(): 

    def __init__ (self, dealer_card: BlackJackCard, *cards: BlackJackCard) -> None: 

        self.dealer_card = dealer_card 
        self._cards = list(cards) 
        #self.hand_value = [sum(card.value[1]) for card in self._cards]

    def __str__(self) -> str: 
        ", ".join(map(str, self._cards)) 
 

    def __repr__(self) -> str: 
        return (
        f"{self.__class__.__name__}" 
        f"({self.dealer_card!r}, " 
        f"{', '.join(map(repr, self._cards))}") 


# class Hand_Lazy(Hand):

#     @property 
#     def total(self) -> int: 
#         delta_soft = max(c.soft - c.hard for c in self._cards) 
#         hard_total = sum(c.hard for c in self._cards) 
#         if hard_total + delta_soft <= 21: 
#             return hard_total + delta_soft 
#         return hard_total 
 
#     @property
#     def card(self) -> list[BlackJackCard]: 
#         return self._cards 

#     @card.setter 
#     def card(self, aCard: BlackJackCard) -> None: 
#         self._cards.append(aCard) 


#     @card.deleter 
#     def card(self) -> None: 
#         self._cards.pop(-1) 


class Suit(dict,Enum):

    suits = {"Spade" :"♠", "Heart" :"♥", "Diamond" :"♦", "Club" :"♣"}
    

class CardValue():    
    ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

    values = {"Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" :7
    , "Eight" : 8, "Nine" : 9, "Ten" : 10, "Jack" : 10, "Queen" : 10, "King" : 10, "Ace" : 11}

   
        
class Deck():

    def __init__(self):

        self._cards = [
            BlackJackCard(value, suit) for value in CardValue.values.items() for suit in Suit.suits.values()
        ]

    def __str__(self):
        string_cards = ""
        for self.card in self._cards:
            string_cards += (str(self.card.value[0]), self.card.suit)
        return string_cards

        #return f"{[self.card.value[0], self.card.suit for self.card  in self._cards]}"

    def shuffle_deck(self):
        shuffle(self._cards)


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
d.shuffle_deck()


#print(f"printing d._cards -> {list(d._cards)}")
for x in d._cards:
    print(x.value[0], x.suit)
print(d._cards.__len__())
d._cards.pop()
print(d._cards.__len__())

new_deck = Deck()
print(new_deck._cards.__len__())
new_deck._cards.clear()
print(new_deck._cards.__len__())

new_deck._cards.append(d._cards.pop())
new_deck._cards.append(d._cards.pop())

print(d._cards.__len__())
print(new_deck._cards.__len__())


for card in new_deck._cards:
    print(card.value[0], card.suit)


bjc = BlackJackCard(('Ace', 11), "♠")

print(f"Printing bjc object {bjc}")

print("printing hand ----------------------------------------------")
# hand_obj = Hand(bjc, new_deck)
# print(hand_obj)

print(f"printing deck ------------------{d}")
print(len(d._cards))

# while True:
#     sum = 0
#     for card in new_deck._cards:
#         sum += card.value[1]
#         print(card, card.value[1])
#     print(f"Sum = {sum}")


#     if sum==21:
#         print("Black Jack")
#         break
#     elif sum>21:
#         print("You Lose")
#         break
#     elif 17 < sum <=20:
#         print("Hold")
#         break
#     elif sum<17:
#         print("Need another card")
#         new_deck._cards.append(d._cards.pop())
#         continue




# h = Hand_Lazy(d._cards.pop(), d._cards.pop(), d._cards.pop())  
# print(h.total)

# hand = Hand()

# print(hand.dealer_card)
