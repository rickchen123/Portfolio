class Hand(object):
	"""This class defines drwaing the cards from the deck and put them back"""
	def __init__(self): 			# empty list of cards
		self.cards = []
		self.values = []
		self.total = self.get_total()

	# draws card from the deck: list
	def draw_from(self,deck): 		
		new_card = Deck.new_card()
		self.cards.append(new_card)
		self.values.append(Deck.card_values[new_card])

	# put the card back to the deck after one round: list
	def return_to(self,deck):		
		Deck.cards.append(self.cards)

	# returns the total value of the palyer's cards
	def get_total(self):
		return sum(i for i in self.values)	

	# show the cards in the current hand
	def current_hand(self):
		return self.cards

	# reset the hand to be empty
	def empty_hand(self):
		self.cards = []
		self.values = []
		self.total = self.get_total()

	# store a card which was being drawn
	def add_card(self, card):
		self.cards.append(card)

	# stores the value of the card being drawn
	def add_value(self, value):
		self.values.append(value)

	#returns the card and corresponding value which was being drawn
	def draw_card(self, deck):
		card, value = deck.next_card()
		self.add_card(card)
		self.add_value(value)

	
