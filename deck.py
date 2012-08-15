import random

from card import card
from hand import hand

class deck(list):
    def __init__(self):
        cards = []
        for i in range(2, 15):
            for j in range(1, 5):
                cards.append(card(i, j))
        self.extend(cards)

    def shuffle(self, num=1):
        for i in range(num):
            random.shuffle(self)

    def cut(self, place=None):
        if place == None:
            place = random.randint(1, 53)
        dtmp = self[place:]
        dtmp.extend(self[:place])
        self[:] = dtmp

    def deal(self):
        h1 = self[0::4]
        h2 = self[1::4]
        h3 = self[2::4]
        h4 = self[3::4]
        return hand(h1), hand(h2), hand(h3), hand(h4)

    def __eq__(self, other):
        """equal if cards in same order"""
        for i in range(52):
            if self[i] != other[i]:
                return False
        return True
        
    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True
    
