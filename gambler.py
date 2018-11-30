
#importing random module to get random outputs
import random

#defining a class named Gambler
class Gambler():

	
	#constructor function called 
	def __init__(self, stake, goal,nmb):
		self.stake = stake
		self.goal = goal
		self.nmb = nmb
		self.fair = 1

	#defining a method to calculate outcome of the game
	def game(self):

		#iterating through the loop to get several outputs
		for i in range(self.nmb):
			game = random.randint(0, 1)

			
			#setting random output according to game 
			if (game == 0):
				print("you won this round ")
				self.stake = self.stake*2

				#break if our conditions are met
				if (self.stake >= self.goal):
					print("!! YOU ARE A WINNER !!")
					break
					


			else:
				print("you loose this round ")
				self.stake = self.stake/2

				
				if(self.stake <= 0):
					print(" YOU LOOSE")
					break
					
			

			
		print("you have {} rupees in your stakes :".format(self.stake))



#taking user input

target = input("Enter your goal : ")
play = input("How many times you wanna play : ")
amount = input("How much money you are offering to play : ")


#objectifying our class and calling its method
gmb = Gambler(amount, target, play)
result = gmb.game()
