import random

class Card:
    def __init__(self, sym, val):
        self.symbol = sym
        self.value = val

    def show(self):
        print(f'{self.value} of {self.symbol}')


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ['Hearts', 'Diamonds', 'Spades', 'Clubs']:
            for v in range(1, 14):
                if v == 1:
                    v = "Ace"
                elif v == 11:
                    v = "Jack"
                elif v == 12:
                    v = "Queen"
                elif v == 13:
                    v = "King"
                else:
                    v = v
                self.cards.append(Card(sym=s, val=v))

    def show_built_deck(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def say_hello(self):
        print(f"Hi!! My name is {self.name}.")
        return self

    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                return False
        return True

    def initial_deal(self, deck, num=13):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                return False
        return True


    def show_hand(self):
        print(f'Player {self.name} has')
        for i in self.hand:
            i.show()
        return self

    def discard(self):
        return self.hand.pop()


deck = Deck()
deck.build()
deck.shuffle()
havala = Player("Havala")
chandu = Player("Chandu")
chandu.say_hello()
havala.say_hello()
chandu.initial_deal(deck)
havala.initial_deal(deck)
chandu.show_hand()
havala.show_hand()