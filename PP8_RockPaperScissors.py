def rock_paper_scissors():
	while True:
		try:
			player1 = str(input("Player 1 - Choose Rock, Paper or Scissors: "))
			if player1.lower() == "rock":
				break
			elif player1.lower() == "paper":
				break
			elif player1.lower() == "scissors":
				break
			else:
				print ("You must enter either Rock, Paper or Scissors")
				continue
		except ValueError:
			print ("You must enter either Rock, Paper or Scissors")
		else:
			break
	
	while True:
		try:
			player2 = str(input("Player 2 - Choose Rock, Paper or Scissors: "))
			if player2.lower() == "rock":
				break
			elif player2.lower() == "paper":
				break
			elif player2.lower() == "scissors":
				break
			else:
				print ("You must enter either Rock, Paper or Scissors")
				continue
		except ValueError:
			print ("You must enter either Rock, Paper or Scissors")
		else:
			break

	if player1.lower() == "rock":
		if player2.lower() == "paper":
			print ("\nPlayer 1 has chosen " + player1.capitalize() + " and Player 2 has chosen " + player2.capitalize() + ". Player 2 wins, congratulations!\n")
		elif player2.lower() == "rock":
			print ("\nPlayer 1 has chosen " + player1.capitalize() + " and Player 2 has chosen " + player2.capitalize() + ". The game is a draw.\n")
		else:
			print ("\nPlayer 1 has chosen " + player1.capitalize() + " and Player 2 has chosen " + player2.capitalize() + ". Player 1 wins, congratulations!\n")
	elif player1.lower() == "paper":
		if player2.lower() == "scissors":
			print ("\nPlayer 1 has chosen " + player1.capitalize() + " and Player 2 has chosen " + player2.capitalize() + ". Player 2 wins, congratulations!\n")
		elif player2.lower() == "paper":
			print ("\nPlayer 1 has chosen " + player1.capitalize() + " and Player 2 has chosen " + player2.capitalize() + ". The game is a draw.\n")
		else:
			print ("\nPlayer 1 has chosen " + player1.capitalize() + " and Player 2 has chosen " + player2.capitalize() + ". Player 1 wins, congratulations!\n")
	elif player1.lower() == "scissors":
		if player2.lower() == "rock":
			print ("\nPlayer 1 has chosen " + player1.capitalize() + " and Player 2 has chosen " + player2.capitalize() + ". Player 2 wins, congratulations!\n")
		elif player2.lower() == "scissors":
			print ("\nPlayer 1 has chosen " + player1.capitalize() + " and Player 2 has chosen " + player2.capitalize() + ". The game is a draw.\n")
		else:
			print ("\nPlayer 1 has chosen " + player1.capitalize() + " and Player 2 has chosen " + player2.capitalize() + ". Player 1 wins, congratulations!\n")
	
	play_again()


def play_again():
	while True:
		try:
			play_again = str(input("Type Y to play again and N to end: "))
			if play_again.lower() == "y":
				rock_paper_scissors()
			elif play_again.lower() == "n":
				print ("Thank you for playing")
				break
			else: 
				print ("You need to enter Y to play again or N to exit: ")
				continue
		except ValueError:
			print ("You need to enter Y to play again or N to exit: ")
		else:
			break


if __name__ == "__main__":
	rock_paper_scissors()
