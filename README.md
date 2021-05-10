# Fuck-the-Dealer
The drinking game "Fuck the Dealer" wrapped in a PyQt GUI. You can play against the computer (or yourself when enough alcohol has been consumed). It has features that keep track of the picked cards and the amount of cards left with handy visuals. Hints on which is the best card to pick can be toggled on or off. A button to simulate an autonomous game is also added.

## Game rules
At the start of a round the dealer (computer in this case) picks a random card from the deck. The player makes a first guess at what rank this card can be (Ace, 1, 2, ... etc.). The color of the card does not matter. If the player chose the right rank the computer has to take **two** sips of beer. If the player was wrong, the computer tells him if the picked card has either a higher or a lower rank than their first guess. The player then has to take another guess at the rank of the picked card. If the second guess is right the computer has to take **one** sip of beer. If the second guess is wrong the player has to take **one** sip of beer.

https://drankspellen.fandom.com/nl/wiki/Fuck_the_Dealer

## Remarks
Originally the game is played such that on two wrong guesses the player has to drink the difference in rank between the picked card and their second guess (so for example 5 sips if the second guess was an Ace, but the picked card was a 6). However, when playing on your own against a dealer this rule is really unfair and can lead to extreme alcohol consumption (_the maker of this program is not responsible for any damages caused due to the misuse of alcohol from playing this game_). For this reason this rule is not implemented. 

While the game is originally called "fuck the dealer", and if playing with more people to share the player allocated beer sips this would definitely be true, this single player version is not so much that. After finishing the program and doing various testruns (where alcohol may or may not have been consumed), it proved to be quite difficult to beat the computer in this game and a win ratio of about 50% was achieved (Monte Carlo simulations are still in progress). 

My time is done, but now I challenge **you** to beat the bot and to become a true _"dealer fucker"_.

## Instructions
Start the game by running `python fuckTheDealer.py` with Python 3.x. 

## Requirements
- pyqt5
- pyqtgraph
- numpy
- wquantiles
