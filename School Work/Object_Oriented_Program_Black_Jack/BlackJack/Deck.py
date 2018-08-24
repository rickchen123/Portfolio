import random
class Deck(object):
	"""This class suffles the deck and draws one card from deck and put cards back"""
	def __init__(self):				# set up the deck
		self.card_values = {'A':1,'2':2,'3':3,'4':4, '5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'K':10,'Q':10}
		self.cards = list(self.card_values.keys())
		self.cards *= 16
		# self.card_values = list(self.card_values.values())
		# self.card_values *= 4

	# Shuffles the deck to get random card
	def shuffle(self):
		random.shuffle(self.cards)


	# self.card_values.remove(self.card_values[self.cards[0]])
	def next_card(self):
		if (len(self.cards) < 1):
			self.cards = list(self.card_values.keys())
			self.cards *= 4
		card = self.cards.pop(0)
		return (card, self.card_values.get(card)) 
		
