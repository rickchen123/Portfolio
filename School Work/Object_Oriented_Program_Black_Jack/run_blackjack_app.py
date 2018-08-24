from BlackJack.Deck import Deck
from BlackJack.Game import Game
from BlackJack.Hand import Hand
from BlackJack.Player import Player

def main():
	"""This function runs the gamble app"""

	print("Welcome to the BlackJack game. Good Luck!")
	print(" ")
	user_name = input('Please enter your name: ')
	user_choice = None

	player = Player(user_name)
	player.hand = Hand()
	dealer = Player('Dealer')
	dealer.hand = Hand()
	deck = Deck()
	game = Game(player, dealer, deck)
	print("-------")
	print('Welcome', user_name,", Please choose what to do.")

	while user_choice != 4:
		print("1. Get chips")
		print("2. Start the game")
		print("3. Check balance")
		print("Press '4' to quit")

		try:
			user_choice = int(input('What would you like to do?\n'))
		except ValueError:
			print("-------")
			print("Please type in a value from 1 to 3")
			print("-------")
			print("")
			continue

		if user_choice == 1:
			try:
				print("-------")
				credit = int(input('How many chips would you like to have?\n'))
				if credit < 0:
					raise ValueError
				player.credit += credit
				print('Now you have',player.credit,'credits' )
				print("-------")
			except ValueError:
				print("-------")
				print("Please enter an positive integer")
				print("-------")
				print("")
				continue

		elif user_choice == 2:
			one_more = 1

			while one_more == 1:
				game.play()
				print("-------")
				try:
					one_more = int(input('One more game? (1 = Yes, 0 = No)\n'))
				except ValueError:
					print("-------")
					print("Please enter either '1' or '0' ")
					print("-------")
					continue

		elif user_choice == 3:
			print("-------")
			print('Your balance is now: ', player.credit)	
			print("-------")

		elif user_choice == 4:
			break

if __name__ == '__main__':
	main()


