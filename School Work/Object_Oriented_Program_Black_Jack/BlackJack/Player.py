class Player(object):
	"""This class clairfys the player class which saves the names of player and the dealer(computer)
	"""
	credit = 0
	hand = ''
	# set up player status 
	def __init__(self,name,credit = 0):            
		self.credit = credit        
		self.owner = name
	
	# Shows the card value in hand: returns an int
	def show_hand(self, dealer_turn):            
		print(self.owner + ' current hand: ' + str(self.hand.current_hand(cards)) + ' for a total of: ' + str(self.hand.get_total()))
		if self.owner == "Dealer" and dealer_turn==0:
			print('Dealer shows: ' + self.cards[0] + ' and <card face down>') #don't show the card in the hole

	# Determine to hit or stand: returns a str
	def hit_or_stand(self):    
		while True:
			try:
				choice = int(input("Press '1' to hit, '0' to stand\n"))
				if choice == 1 or choice == 0:
					if choice == 1:
						return 1
					elif choice == 0:
						return 0
				else:
					raise  ValueError
			except ValueError:
				print("-------")
				print('Now you have', self.hand.current_hand()[:])
				continue

	# Display current card in hand: returns a str
	def current_cards(self):        
		return self.hand.current_hand()

	# return the sum of cards in player's hand 
	def current_value(self):
		return self.hand.get_total()

	# change the current credit 
	def change_credits(self, amount):
		self.credit += amount