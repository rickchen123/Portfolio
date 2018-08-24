class Game(object):
    """"""
    def __init__(self,player,dealer,deck):  #set up the initial
        self.player = player
        self.dealer = dealer
        self.deck = deck

    def play(self): 
        '''
        Run the game once
        '''
        self.deck.shuffle()
        self.player.hand.empty_hand()
        self.dealer.hand.empty_hand()

        hit = None 
        bet = 0
        ifreload = -1

        ##player turn##
        while bet < 1 or bet > self.player.credit:
            try:
                print("-------")
                bet = int(input('How much would you like to bet? You have ' + str(self.player.credit) + ' credits. \n'))
                if bet == -1:
                    break
                if bet < 1:
                    print('Please bet at least 1 credit')
                    print('If you want to quit the game, put -1\n')

                while bet > self.player.credit:
                    print("-------")
                    print('You do not have sufficient credits to make this bet. You have ' + str(self.player.credit) + ' credits left.')
                    try:
                        ifreload = int(input('Would you like to get more chips? (1= Yes, 0 = No)\n'))
                        if (ifreload != 1 and ifreload != 0):
                            raise ValueError
                        if ifreload == 1:
                            try:
                                reload_credit = int(input('How much more chips would you like to get?\n'))
                                self.player.credit += reload_credit
                            except ValueError:
                                print("-------")
                                print('That was an invalid number. Please enter an positive integer value')
                                print("-------")
                        elif ifreload == 0:
                             break
                    except ValueError:
                        print("-------")
                        print('Please Enter 1 or 0')
                        print("-------") 
                if ifreload == 0:
                    break
            except ValueError:
                print("-------")
                print('That was an invalid number. Please enter a value >= 1')  
                print("-------")
        
        if bet == -1 or ifreload == 0:
            return

        print('You bet ' + str(bet))
        print("-------")
        self.player.change_credits(-bet)

        # draw the first two cards
        for i in range(2):
            self.player.hand.draw_card(self.deck)
            self.dealer.hand.draw_card(self.deck)

        while True:
            try:
                easy_mode = int(input('Would you like us to calculate the total value for you? (1 = Yes, 0 = No) \n'))
                print("-------")
                if (easy_mode != 0 and easy_mode != 1):
                    raise ValueError
                break
            except ValueError:
                print("Please enter either 1 or 0")
                print("-------")
                continue

        print('Now you have',self.player.current_cards()[:])
        if easy_mode:
            print('Your total is', self.player.current_value())
        print('One of the card that dealer has: ', self.dealer.current_cards()[:1])
        print("-------")

        #give the palyer a chance to hit.
        if self.player.hand.get_total() <  21:
            hit = self.player.hit_or_stand()
        if len(self.player.current_cards())==5:
            hit = 0
        if self.player.hand.get_total() == 21:
            print('Player Blackjack!')
            self.player.change_credits(bet*2.5) #3:2 returns for blackjack
            return

        while self.player.hand.get_total() < 21 and hit == 1:
            self.player.hand.draw_card(self.deck)
            print("-------")
            print('Now you have', self.player.current_cards()[:])
            if easy_mode:
                print('Your total is', self.player.current_value())
            print('One of the card that dealer has: ', self.dealer.current_cards()[:1])
            print("-------")
            
            if self.player.hand.get_total() > 21:
                print('Player bust!')
                break
            hit = self.player.hit_or_stand()
        
        #player stands
        if hit == 0: 
            dealer_hit = 1
            print("-------")
            print('Player stands. Dealer turn')
            while dealer_hit != 0:
                if self.dealer.hand.get_total() < 17:
                    self.dealer.hand.draw_card(self.deck)
                elif len(self.player.current_cards())>=5:
                    dealer_hit = 0
                else:
                    dealer_hit = 0  
            print('Now Dealer has: ', self.dealer.current_cards())
            
                
            if self.dealer.hand.get_total() == 21 and self.player.hand.get_total() < 21 and len(self.dealer.current_cards()) == 2:
                print('Dealer Blackjack!')
                self.player.change_credits(int(-bet * 0.5))
            elif self.dealer.hand.get_total() == 21 and self.player.hand.get_total() == 21:
                print('Push! You have tied. You will get back your initial bet.')
                self.player.change_credits(int(bet))  
            
            elif self.dealer.hand.get_total() > 21:
                print('Dealer busted. You win!')
                self.player.change_credits(2*int(bet))
            
            elif self.dealer.hand.get_total() > self.player.hand.get_total(): 
                print('Dealer wins!')

            elif self.dealer.hand.get_total() == self.player.hand.get_total():
                print('Push! You have tied. You will get back your initial wager.')
                self.player.change_credits(int(bet))

            elif self.dealer.hand.get_total() < self.player.hand.get_total():
                print('You win!') 
                self.player.change_credits(2*int(bet))
            
        print('Your current credit is: ' + str(self.player.credit))