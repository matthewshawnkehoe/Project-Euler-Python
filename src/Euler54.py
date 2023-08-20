'''
Project Euler : Problem 54
@author: Matthew Kehoe
'''

import time
from collections import namedtuple

start = time.time()

Card = namedtuple('Card', ['rank', 'suit'])

Ace = 14
King = 13
Queen = 12
Jack = 11
Ten = 10


def map_rank(rank_to_map):
    if rank_to_map == 'A':
        return Ace
    if rank_to_map == 'K':
        return King
    if rank_to_map == 'Q':
        return Queen
    if rank_to_map == 'J':
        return Jack
    if rank_to_map == 'T':
        return Ten
    return int(rank_to_map)


def map_suit(suit_to_map):
    if suit_to_map == 'H':
        return 1
    if suit_to_map == 'D':
        return 2
    if suit_to_map == 'C':
        return 3
    # S = Spades
    return 4


def map_card(card_to_map):
    return Card(rank=map_rank(card_to_map[0]), suit=map_suit(card_to_map[1]))


class Hand(object):

    def __init__(self, *args):
        self.cards = sorted(args, key=lambda c: -c.rank)
        self.duplicates = {}
        for card in self.cards:
            if card.rank in self.duplicates:
                continue
            _duplicates = 0
            for card2 in self.cards:
                if card.rank == card2.rank:
                    _duplicates += 1
            self.duplicates[card.rank] = _duplicates

    def __cmp__(self, other):
        for rule in self.rules():
            #print(rule + ' ')
            rule = getattr(self, rule)
            val = rule(other)
            #print(val)
            if val:
                return val

    def rules(self):
        return []

    def _straight(self):
        last_card_rank = False
        for card in self.cards:
            if last_card_rank and last_card_rank != card.rank + 1:
                return False
            last_card_rank = card.rank
        return True

    def _flush(self):
        last_card_suit = False
        for card in self.cards:
            if last_card_suit and last_card_suit == card.suit:
                return False
        return True

    def _duplicate_count(self, c):
        for rank, value in self.duplicates.items():
            if value == c:
                yield rank


class PokerHand(Hand):
    def rules(self):
        rules = super(PokerHand, self).rules()
        rules.append('royal_flush')
        rules.append('straight_flush')
        rules.append('four_of_a_kind')
        rules.append('full_house')
        rules.append('flush')
        rules.append('straight')
        rules.append('three_of_a_kind')
        rules.append('two_pair')
        rules.append('highest_card')
        return rules

    def royal_flush(self, other):
        h1 = self.cards[0].rank == Ace and self._flush() and self._straight()
        h2 = other.cards[0].rank == Ace and other._flush() and other._straight()
        if h1 and not h2:
            return 1
        if h2 and not h1:
            return -1
        if h1 and h2:
            return 0

    def straight_flush(self, other):
        h1 = self._flush() and self._straight()
        h2 = other._flush() and other._straight()
        if h1 and not h2:
            return 1
        if h2 and not h1:
            return -1
        if h1 and h2:
            return self.highest_card(other)

    def four_of_a_kind(self, other):
        return self._of_a_kind(other, 4)

    def three_of_a_kind(self, other):
        return self._of_a_kind(other, 3)

    def _of_a_kind(self, other, value):
        h1 = [r for r in self._duplicate_count(value)]
        h2 = [r for r in other._duplicate_count(value)]
        if len(h1) > len(h2):
            return 1
        if len(h2) > len(h1):
            return -1
        for h1_c, h2_c in list(zip(h1, h2)):
            if h1_c > h2_c:
                return 1
            if h2_c > h1_c:
                return -1

    def two_pair(self, other):
        return self._of_a_kind(other, 2)

    def full_house(self, other):
        h1_3 = [r for r in self._duplicate_count(3)]
        h2_3 = [r for r in other._duplicate_count(3)]
        h1_2 = [r for r in self._duplicate_count(2)]
        h2_2 = [r for r in other._duplicate_count(2)]
        if h1_3 and h1_2 and not (h2_3 and h2_2):
            return 1
        if h2_3 and h2_2 and not (h1_3 and h1_2):
            return -1
        if h1_3 and h1_2 and h2_3 and h2_2:
            for h1_c, h2_c in list(zip(h1_3, h2_3)):
                if h1_c > h2_c:
                    return 1
                if h2_c > h1_c:
                    return -1
            for h1_c, h2_c in list(zip(h1_2, h2_2)):
                if h1_c > h2_c:
                    return 1
                if h2_c > h1_c:
                    return -1

    def flush(self, other):
        h1 = self._flush
        h2 = other._flush
        if h1 and not h2:
            return 1
        if h2 and not h1:
            return -1

    def straight(self, other):
        h1 = self._straight
        h2 = other._straight
        if h1 and not h2:
            return 1
        if h2 and not h1:
            return -1

    def highest_card(self, other):
        list1 = list(zip(self.cards, other.cards))
        for c1, c2 in list1:
            if c1.rank != c2.rank:
                return 1 if c1.rank > c2.rank else -1
        raise Exception("tie in highest_card")


def gen_hands(s):
    cards = [map_card(c) for c in s.split(' ')]
    return PokerHand(*cards[0:5]), PokerHand(*cards[5:])


p1_wins = 0
with open('poker.txt') as f:
    for line in f:
        h1, h2 = gen_hands(line.strip())
        if h1.__cmp__(h2) > 0:
            p1_wins += 1

val = p1_wins

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))

