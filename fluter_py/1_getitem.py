import collections
from random import choice

# namedtuple 给赋予一个具有少数属性,但是没有方法的对象
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    ranks = [i for i in range(2, 11)] + list("JQWE")
    suits = "speads diamods".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamods')
print(beer_card)

deck = FrenchDeck()
print(choice(deck))


# 向量加减

