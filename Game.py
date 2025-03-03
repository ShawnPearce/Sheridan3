import random
from Player import Player

class Game: #creat the Game class
    def __init__(self): #Constructor for the game class
        self.players=[Player() for x in range(3)] #set the number of players to 3
        self.guess = None #initialize the guess attribute
    
    def start(self): #create the start() method
        self.guess = random.randint(1,6) #generate a random number as the games roll
        print("The game rolled:  ",self.guess) #Display the games roll
    
    def match(self): #create the match method
        player_number=1 #initalize the player_number variable to track whos turn it is
        for player in self.players: #initialize the loop for each player
            roll_result=player.roll()#Each player rolls a number
            print("Player:",player_number,"rolled: ",roll_result)#display the roll result for each player
            if roll_result==self.guess:#increment the score if the roll matches the guess
                player.score+=1
                print("Player",player_number,"SCORES!")
            player_number += 1 #moves to the next player