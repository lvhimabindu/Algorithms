import sys
from random import randint

'''

This file implements the simulation of the famous monty-hall problem. 

https://en.wikipedia.org/wiki/Monty_Hall_problem. 

Input: Number of iterations to run the simulation.
Output: Probability of a switching win (explained below)

Monty Hall Problem: 

Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. 
You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. 
He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

Answer to Monty Hall Problem:

It is interesting to note that the answer to the question posed is that there is an advantage to switching your choice. More precisely, the probability of a stay win (no switching) is 1/3 
while the probability of a switch win is 2/3. 

Simulation Algorithm:

1. Randomly assign goats and car behind one of the doors numbered 1 through 3. 
2. Simulate the player on the game and randomly choose one of the doors. 
3. If the chosen door has a car, then record it as a staying win since the player wins if he does not switch in this case.
4. If the chosen door has a goat, then record it as a switching win since the player wins if he changes the choice he made at first. 

Error Handling: This implementation checks if the input (number of iterations) is indeed an integer. 

Note: 
1. Input the number of iterations to be in the order of atleast tens of thousands. Setting this value to a very small number does not guaranteee convergence. 
2. This code is generic enough to handle the problem setting with varying number of doors. 

'''

def assign_goats_car(num_doors):
	''' This function basically assigns the initial configuration as to which door has goats and car behind them. '''
	
	config_arr = [0] * num_doors
	car_door = randint(0,num_doors-1) 
	config_arr[car_door] = 1
	return config_arr


def player_chooses(num_doors):
	''' This function simulates the process of the player choosing a door '''

	door_chosen = randint(0,num_doors-1)
	return door_chosen


def run_simulation(iters,num_doors):
	''' This function computes the probability of stay and switch wins from the simulation '''
	''' Note: p(stay_win) = 1 - p(switch_win) given the way the process is constructed. 
	Instead of using this though, we compute stay_win and switch_win separately (as a sanity check).'''

	stay_win = 0
	switch_win = 0
	for i in range(iters):
		config_arr = assign_goats_car(num_doors)
		door_chosen = player_chooses(num_doors)
		if config_arr[door_chosen] == 1:
			stay_win += 1
		else:
			switch_win += 1
	print "The probability of a staying win: %f" % (stay_win/(iters+0.0))
	print "The probability of a switching win: %f" % (switch_win/(iters+0.0))


if __name__ == '__main__':
	''' This is the main function which takes the number of iterations as the input, checks it appropriately and then call the run_simulation function '''

	try:
		iters = input("Enter the number of iterations: ")
		iters = int(iters)
	except Exception:
		print "Number of iterations should be an integer!"
		sys.exit(-1)

	run_simulation(iters,3)		# Setting the number of doors to 3
