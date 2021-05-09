import random
import numpy as np
import weighted

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
        self.cards = Deck()

    # Plays the first round of FTD
    def first_round(self, first_guess):
        picked = self.cards.random_pick()

        # 1st round
        if rank2int(first_guess) == picked.numrank:
            
            return picked, True

        else:
            if rank2int(first_guess) > picked.numrank:
                return picked, 'lower'
                
            elif rank2int(first_guess) < picked.numrank:
                return picked, 'higher'

    # Plays the second round of FTD
    def second_round(self, second_guess, picked):
        # 2nd round
        if rank2int(second_guess) == picked.numrank:
            
            #self.cards.remove(picked.rank, picked.color)
            return picked, True

        else:
            #self.cards.remove(picked.rank, picked.color)
            return picked, False
    

    def best_firstguess(self, cards):
        """
        Calculates the best guesses from the current
        card state
        """
        ranks = np.arange(1, 14)
        count_array = np.array(list(cards.counts().values()))

        # getting the weighted median
        wmedian = weighted.median(ranks, count_array)

        # getting the best first guess based on minimum difference
        # between medium and mode
        nearest_ranks = np.argsort(np.abs(wmedian - ranks))
        i = 0
        
        if not all(v == 0 for v in count_array):
            while True:
                best_pick = ranks[nearest_ranks][i]
                best_counts = count_array[nearest_ranks][i]
                if best_counts != 0:
                    return best_pick, best_counts
                i += 1

        return 0, 0

    def best_secondguess(self, cards, first_guess, picked):
        """
        The best second guess are all the modes that 
        are in the leftover part of the board
        """
        ranks = np.arange(1, 14)
        count_array = np.array(list(cards.counts().values()))
        
        # creating leftover arrays
        if rank2int(first_guess) > rank2int(picked.rank):
            leftover_ranks = ranks[ranks < rank2int(first_guess)]
            leftover_counts = count_array[leftover_ranks - 1]
        elif rank2int(first_guess) < rank2int(picked.rank):
            leftover_ranks = ranks[ranks > rank2int(first_guess)]
            leftover_counts = count_array[leftover_ranks - 1]
        
        # getting the ranks with the highest count in leftover array
        N = np.count_nonzero(leftover_counts == np.max(leftover_counts))
        idx = np.argpartition(leftover_counts, -N)[-N:]
        mode_indices = idx[np.argsort((-leftover_counts)[idx])]
        
        # calculating the best picks and best counts
        best_picks = leftover_ranks[mode_indices]
        best_counts = leftover_counts[mode_indices]
        
        return best_picks, best_counts