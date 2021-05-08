import random

# simple function to rewrite some of the rank values
def rank2int(rank):
    try: 
        converter = {'Ace': 1, 'Jack' : 11, 'Queen' : 12, 'King' : 13}
        return converter[rank]
    except:
        return int(rank)

class Card:
    """
    Card class represents an individual card in the deck and
    has useful attributes of the cards themselves
    """

    def __init__(self, rank, color):
        self.rank = rank
        self.color = color

        # also add a numerical value as rank
        self.numrank = rank2int(self.rank)

        # also add the name of corresponding png
        if self.rank == '10':
            self.filename = self.rank + self.color[0] + '.png'
        else:
            self.filename = self.rank[0] + self.color[0] + '.png'

class Deck:
    """
    The Deck class initializes a full deck of 52 playing cards 
    and has methods to alter the deck in useful ways
    """

    # Create two class variables that can be called upon with self.ranks and self.colors
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    colors = ['Diamond', 'Club', 'Heart', 'Spade']

    def __init__(self):
        
        # create a list of all possible unique Card objects (52 total)
        deck_list = []
        for rank in self.ranks:
            for color in self.colors:
                deck_list.append(Card(rank, color))

        self.deck_list = deck_list

    # remove a specific card from the deck
    def remove(self, rank, color):
        print('REMOVE CHECK')
        for i, card in enumerate(self.deck_list):
            if card.rank == rank and card.color == color:
                self.deck_list.pop(i)
                break
    
    # pick a random card from the deck
    def random_pick(self):
        random_card = random.choice(self.deck_list)
        return random_card
        
    # counts how much of each rank is left in deck
    def counts(self):
        
        # create empty dict with all ranks
        count_dict = dict(zip(self.ranks, [0]*len(self.ranks)))
        
        # count instances of that rank still in deck
        for card in self.deck_list:
            count_dict[card.rank] += 1
        
        return count_dict
    
    # gives the total number of cards in the deck
    def total(self):
        tot = sum(self.counts().values())
        return tot
    
class Game:
    """
    The Game class initializes a game of Fuck the Dealer with
    a full deck of cards. The methods can be used to progress
    in the game or plot the game state
    """
    def __init__(self):
        print('init')
        self.cards = Deck()

    # Plays the first round of FTD
    def first_round(self, first_guess):
        picked = self.cards.random_pick()

        # 1st round
        if first_guess == picked.rank:
            
            self.cards.remove(picked.rank, picked.color)
            return picked, True

        else:
            if rank2int(first_guess) > picked.numrank:
                return picked, 'lower'
                
            elif rank2int(first_guess) < picked.numrank:
                return picked, 'higher'

    # Plays the second round of FTD
    def second_round(self, second_guess, picked):
        # 2nd round
        if second_guess == picked.rank:
            
            self.cards.remove(picked.rank, picked.color)
            return picked, True

        else:
            self.cards.remove(picked.rank, picked.color)
            return picked, False
        
    def plot_counts(self):
        """
        Makes a barplot of the number of counts of each rank
        """
        return