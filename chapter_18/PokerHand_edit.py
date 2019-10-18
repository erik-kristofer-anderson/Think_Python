"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from card_sample import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False


    ### add method has_pair
    def has_pair(self):
        """ returns true if the hand contains at least one pair
        (pair is two or more cards with same rank)

        works correctly for hands with two or more cards
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    ### add method has_twopair
    def has_twopair(self):
        """ returns true if the hand contains at least two pairs
        (pair is two or more cards with same rank)

        works correctly for hands with two or more cards
        """
        self.rank_hist()
        count = 0
        for val in self.ranks.values():
            if val >= 2:
                count += 1
        if count >=2:
            return True
        return False

    ### add method has_three_of_a_kind
    def has_three_of_a_kind(self):
        """ returns true if the hand contains at least one instance of three of a kind
        (three of a kind is 3 or more cards of the same rank)
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    ### add method has_straight
    def has_straight(self):
        """ returns True if there are a set of five cards in order by rank
        (ace can be high or low) other wise returns False
        """
        self.rank_hist()
        self.ranks[14] = self.ranks.get(1, 0) # allows for ace is high
        counter = 0
        i = 1
        while i <= 14:
            val = self.ranks.get(i, 0)
            if val >= 1:
                counter += 1
            else:
                counter = 0
            if counter >= 5:
                return True
            i += 1



        return False

    def has_full_house(self): # to test # add method has_full_house
        """ returns True if any suit has two cards and any other
        suit has three cards
        """
        self.suit_hist()
        test_pair = False
        test_three = False
        count = 0
        for val in self.suits.values():
            if val == 2:
                test_pair = True
            if val == 3:
                test_three = True
        return test_pair and test_three

    def has_four_of_a_kind(self):
        """ returns true if the hand contains at least one instance of four of of a kind
        (four of a kind is 4 or more cards of the same rank)
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def has_straight_flush(self): #TODO
        """returns true if the hand has a straight flush
        (I'm not sure how to do this)
        """
        result = self.has_straight() and self.has_flush()
        return result

if __name__ == '__main__':
    # make a deck
    # deck = Deck()
    # deck.shuffle()
    #
    # hand = PokerHand()
    # hand = PokerHand()
    # deck.move_cards(hand, 5)
    # hand.sort()
    # hand.suit_hist()


    ### test straight flush
    test = False
    while test == False:
        deck = Deck()
        deck.shuffle()

        hand = PokerHand()
        hand = PokerHand()
        deck.move_cards(hand, 5)
        hand.sort()
        print(hand)
        test = hand.has_straight_flush()
        print(test)
        print('')


    # # deal the cards and classify the hands
    # for i in range(1):
    #     hand = PokerHand()
    #     deck.move_cards(hand, 5)
    #     #hand.sort()
    #     hand.sort_by_rank()
    #     print(hand)
    #     # print(hand.has_flush())
    #     # print('')
    #     print(hand.has_four_of_a_kind())
    #     print('')
    #
    #
    # test = False
    # test_count = 0
    # while test == False:
    #     print(test_count)
    # # make a deck
    #     deck = Deck()
    #     deck.shuffle()
    #
    # # deal the cards and classify the hands
    #     for i in range(1):
    #         hand = PokerHand()
    #         deck.move_cards(hand, 5)
    #         hand.sort()
    #         hand.sort_by_rank()
    #         print(hand)
    #         # print(hand.has_flush())
    #         # print('')
    #
    #         test = hand.has_four_of_a_kind()
    #         print(test)
    #         print('')
        # test_count += 1
