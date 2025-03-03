from Game import Game
import random

class Application: #Create the Application method
    def __init__(self): #constructor for the Application class
        self.game = Game() #Create an instance of the game class
    
    def run(self):#Create the run method
        for round_num in range(1,6): #loop through 5 rounds
            print(round_num) #Display the round number
            self.game.start() #Start the round by generating a guess
            self.game.match() #Compare player rolls with the guess
            
        self.declare_winner() #Declare the winner after 5 rounds
        
    def declare_winner(self):
        scores=[player.score for player in self.game.players] #Collect player scores
        max_score=max(scores) #Find the highest score
        winners =[] #initalize a list to store the winners
        player_number=1 #Track player numbers
        
        for score in scores:
            if score==max_score:
                winners.append(player_number) #Add player number if they have the highest score
            player_number +=1
            
        print("Final Scores:  ") #Display final score
        player_number = 1
        for score in scores:
            print("Player",player_number,":",score,"points")
            player_number +=1
        
        if len(winners) >1:
            print("Its a tie") #Display tie message
        else:
            print("Player",winners[0],"wins the game!") #Display the winner

