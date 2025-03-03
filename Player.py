
import random #import the random module for generating random numers

class Player: # create the Player class
    def __init__(self):      #constructor for the player class
        self.score=0         #initialize the player score to 0
    
    def roll(self):       #create the roll() method
        return (random.randint(1,6))    #return a random number between 1 and 6 to simulate the roll of the dice