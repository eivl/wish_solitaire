from textwrap import wrap
from itertools import islice
import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit', 'icon'])


class Deck:
    ranks = [str(n) for n in range(7, 11)] + list('JQKA')
    suits = [('spades', u'\u2660'),
             ('diamonds', u'\u2666'),
             ('clubs', u'\u2663',),
             ('hearts', u'\u2665')]

    def __init__(self, shuffle=True):
        self._cards = [Card(rank, suit, icon) for suit, icon in self.suits
                       for rank in self.ranks]
        if shuffle:
            self.shuffle()

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        return self._cards.pop()

import textwrap
sentence = '♢10'
width = 6


print('┌─' + '─' * width + '─┐')
for line in wrap(sentence, width):
    print(f'│ {line:^{width}} │')
print('└─' + '─'* width + '─┘')

deck = iter(Deck())
pile_setup = [4]*8
piles = [list(islice(deck, n))
         for n in pile_setup]

board = [pile.pop() for pile in piles]


class Board:
    pass

from pprint import pprint
lines = [
    ['╔═════════╗'],
    ['║░░░░░░░░░║'],
    ['║░░░░░░░░░║'],
    ['║░░░░░░░░░║'],
    ['║░░░░░░░░░║'],
    ['║░░░░░░░░░║'],
    ['║░░░░░░░░░║'],
    ['║░░░░░░░░░║'],
    ['╚═════════╝']
]

class Card(object):

    card_values = {
        'Ace': 11,  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }

    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.card_values[rank]

def ascii_version_of_card(*cards, return_string=True):
    """
    Instead of a boring text version of the card we render an ASCII image of the card.
    :param cards: One or more card objects
    :param return_string: By default we return the string version of the card, but the dealer hide the 1st card and we
    keep it as a list so that the dealer can add a hidden card in front of the list
    """
    # we will use this to prints the appropriate icons for each card
    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    suits_symbols = ['♠', '♦', '♥', '♣']

    # create an empty list of list, each sublist is a line
    lines = [[] for i in range(9)]

    for index, card in enumerate(cards):
        # "King" should be "K" and "10" should still be "10"
        if card.rank == '10':  # ten is the only one who's rank is 2 char long
            rank = card.rank
            space = ''  # if we write "10" on the card that line will be 1 char to long
        else:
            rank = card.rank[0]  # some have a rank of 'King' this changes that to a simple 'K' ("King" doesn't fit)
            space = ' '  # no "10", we use a blank space to will the void
        # get the cards suit in two steps
        suit = suits_name.index(card.suit)
        suit = suits_symbols[suit]

        # add the individual card on a line by line basis
        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, rank))
        lines[8].append('└─────────┘')

    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))

    # hidden cards do not use string
    if return_string:
        return '\n'.join(result)
    else:
        return result


def ascii_version_of_hidden_card(*cards):
    """
    Essentially the dealers method of print ascii cards. This method hides the first card, shows it flipped over
    :param cards: A list of card objects, the first will be hidden
    :return: A string, the nice ascii version of cards
    """
    # a flipper over card. # This is a list of lists instead of a list of string becuase appending to a list is better then adding a string
    lines = [['┌─────────┐'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['└─────────┘']]

    # store the non-flipped over card after the one that is flipped over
    cards_except_first = ascii_version_of_card(*cards[1:], return_string=False)
    for index, line in enumerate(cards_except_first):
        lines[index].append(line)

    # make each line into a single list
    for index, line in enumerate(lines):
        lines[index] = ''.join(line)

    # convert the list into a single string
    return '\n'.join(lines)


# TEST CASES
test_card_1 = Card('Diamonds', '4')
test_card_2 = Card('Clubs', 'Ace')
test_card_3 = Card('Spades', 'Jack')
test_card_4 = Card('Hearts', '10')

print(ascii_version_of_card(test_card_1, test_card_2, test_card_3, test_card_4))
print(ascii_version_of_hidden_card(test_card_1, test_card_2, test_card_3, test_card_4))
# print(ascii_version_of_hidden_card(test_card_1, test_card_2))


CARD = f"""\
┌─────────┐
│{rank: <2}       │
│         │
│         │
│    {suit: <2}   │
│         │
│         │
│       {rank: >2}│
└─────────┘
"""

HIDDEN_CARD = """\
┌─────────┐
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
└─────────┘
"""

def join_lines(strings):
    """
    Stack strings horizontally.
    This doesn't keep lines aligned unless the preceding lines have the same length.
    :param strings: Strings to stack
    :return: String consisting of the horizontally stacked input
    """
    liness = [string.splitlines() for string in strings]
    return '\n'.join(''.join(lines) for lines in zip(*liness))

def ascii_version_of_card(*cards):
    """
    Instead of a boring text version of the card we render an ASCII image of the card.
    :param cards: One or more card objects
    :return: A string, the nice ascii version of cards
    """

    # we will use this to prints the appropriate icons for each card
    name_to_symbol = {
        'Spades':   '♠',
        'Diamonds': '♦',
        'Hearts':   '♥',
        'Clubs':    '♣',
    }

    def card_to_string(card):
        # 10 is the only card with a 2-char rank abbreviation
        rank = card.rank if card.rank == '10' else card.rank[0]

        # add the individual card on a line by line basis
        return CARD.format(rank=rank, suit=name_to_symbol[card.suit])


    return join_lines(map(card_to_string, cards))


def ascii_version_of_hidden_card(*cards):
    """
    Essentially the dealers method of print ascii cards. This method hides the first card, shows it flipped over
    :param cards: A list of card objects, the first will be hidden
    :return: A string, the nice ascii version of cards
    """

    return join_lines((HIDDEN_CARD, ascii_version_of_card(*cards[1:])))


'┌─────────┐'
'│Q        │'
'│         │'
'│         │'
'│    ♦    │'
'│         │'
'│         │'
'│        Q│'
'└─────────┘'
