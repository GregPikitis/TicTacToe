#Emelia Blankenship 
#12-30-15
#This final version has input validity checking, and displays the stats of winnings of all games at the end by reading and writing to a file.

# Importing things and creating variables
import os
import colorama
from colorama import Fore, Back, Style
import sys
spacer = "-----------"
board = [1,2,3,4,5,6,7,8,9]
winner = False
file = open("stats",'r')
#reading from file for stats at end
things = file.readline()
file.close()

#Obvi im printing the current gameboard here
def printboard():
	print()
	print("",board[0],'|',board[1],'|',board[2])
	#Spacer is just the --- between the lines
	print(spacer)
	print("",board[3],'|',board[4],'|',board[5])
	print(spacer)
	print("",board[6],'|',board[7],'|',board[8])
	print()
	
#Obvi checking to see if anyone has won
def checkwinner():
	#Just all the ways it can win, if they are equal then it gives the character that holds that spot.
	if board[0] == board[1] == board[2]:
		return board[0]
	elif board[3] == board[4] == board[5]:
		return board[3]
	elif board[6] == board[7] == board[8]:
		return board[6]
	elif board[0] == board[3] == board[6]:
		return board[0]
	elif board[1] == board[4] == board[7]:
		return board[1]
	elif board[2] == board[5] == board[8]:
		return board[2]
	elif board[0] == board[4] == board[8]:
		return board[0]
	elif board[2] == board[4] == board[6]:
		return board[2]
	else:
		#If none are equal then returns false because no winner obvi.
		return False
	
#Checking if the gameboard is full
def fullcheck():
	#If the item is a number then all the spots havent been taken, board isn't full.
	for spot in board:
		if type(spot) == int:
			return False
	return True


def main():
	#Clearing the terminal
	os.system('cls' if os.name == 'nt' else 'clear')
	
	#Entry stuff
	print(Fore.YELLOW+"Welcome to Tic-Tac-Toe!"+Style.RESET_ALL)
	print(Fore.RED+"Press q at any prompting to quit"+Style.RESET_ALL)
	
	#While the board has spaces and no one has won...
	while fullcheck() == False and checkwinner() == False:
		printboard()
		
		#For the X players move..
		while fullcheck() == False and checkwinner() == False:
			#Taking the X players input
			choicex = input(Fore.YELLOW+"Player X please choose your position. (ex. 1 or 3)\n"+Style.RESET_ALL)
			os.system('cls' if os.name == 'nt' else 'clear')
			#Little header thing and space for looks
			print(Fore.YELLOW+"Tic-Tac-Toe"+Style.RESET_ALL)
			print()
			
			#Checking if user wanted to quit
			if choicex.lower() == 'q':
				print(Fore.BLUE+"Bye!"+Style.RESET_ALL)
				sys.exit()
				
			#Making sure the given input is valid
			if choicex.isdigit() == True:
				#Making the valid input an int
				choicex = int(choicex)
				#The board list index is one less so subtracting one
				boardnum = choicex - 1
			else:
				#Valid input
				input(Fore.RED+"That's not a valid input."+Style.RESET_ALL)
				printboard()
				continue
				
			#Checking for valid input differently here
			if choicex < 1 or choicex > 9:
				input(Fore.RED+"That's not a valid input. Please choose a new spot. (Should be a number)"+Style.RESET_ALL)
				printboard()
				continue
			#Putting the X in the space the user intended
			elif type(board[boardnum]) == int:
				board[boardnum] = 'X'
				if checkwinner() != False:
					#Making Winner == True so the loops no longer run
					winner = True
					continue
				printboard()
				break
			#If the above don't run then it must be already filled.
			else:
				input(Fore.RED+"That spot is already taken. Please choose again."+Style.RESET_ALL)
				printboard()
				continue
				
		#Doing the O now...
		while fullcheck() == False and checkwinner() == False:
			#Taking the input
			choiceo = (input(Fore.YELLOW+"Player O please choose your position. (ex. 1 or 3)\n"+Style.RESET_ALL))
			os.system('cls' if os.name == 'nt' else 'clear')
			print(Fore.YELLOW+"Tic-Tac-Toe"+Style.RESET_ALL)
			print()
			
			#Checking if user is quitting
			if choiceo.lower() == 'q':
				print(Fore.BLUE+"Bye!"+Style.RESET_ALL)
				sys.exit()
			
			#Making sure everything checks out with the input
			if choiceo.isdigit() == True:
				#Checks out so making it an int and subtracting one for index purposes
				choiceo = int(choiceo)
				boardnum = choiceo - 1
			else:
				#Whoops bad input
				input(Fore.RED+"That's not a valid input."+Style.RESET_ALL)
				printboard()
				continue
				
				
			if choiceo < 1 or choiceo > 9:
				#Checking in input is out of range
				input(Fore.RED+"That's not a valid input. Please choose a new spot. (Should be a number)"+Style.RESET_ALL)
				printboard()
				continue
			
			#Making sure its an integer and putting the O in the spot on the board
			elif type(board[boardnum]) == int:
				board[boardnum] = 'O'
				#If theres a winner, it't setting the winner variable to True so loops don't run anymore.
				if checkwinner() != False:
					winner = True
					continue
				break
				
			else:
				#If the spot is already used.
				input(Fore.RED+"That spot is already taken. Please choose again."+Style.RESET_ALL)
				printboard()
				continue
				
	#When the loops stop, checks if its full and theres no winner for a tie	
	if fullcheck() == True and checkwinner() == False:
		print()
		print(Fore.GREEN+"There's a tie!!"+Style.RESET_ALL)
		print()
		
	else:
		#If its not a tie then someone won. So tell em.
		printboard()
		print()
		print(Fore.GREEN+checkwinner(),"is the winner!"+Style.RESET_ALL)
		
		#Printing and obtaining stats for the end
		winner = checkwinner()
		newfile = things+winner
		#Writing to the file for next game
		file = open("stats",'w')
		file.write(newfile)
		file.close()
		
		numo = newfile.count('O')
		
		#this is a float (this was for me)
		statso = (numo / len(newfile))*100
		#Making it round to the second decimal place
		statso = "{0:.2f}".format(statso)
		
		#Doing the same thing for X
		numx = newfile.count('X')
		statsx = (numx / len(newfile))*100
		statsx = "{0:.2f}".format(statsx)
		
		#Printing the stats and making it pretty
		print()
		print(Fore.BLUE+"O wins: "+Fore.MAGENTA+statso+"%"+Fore.BLUE+" of the time."+Style.RESET_ALL)
		print(Fore.BLUE+"X wins: "+Fore.MAGENTA+statsx+"%"+Fore.BLUE+" of the time."+Style.RESET_ALL)
		print()
			

#Calling the main function.
if __name__ == "__main__":
    main()
	
	
	
	
	
	
	
	
	
	