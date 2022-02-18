
import random

ng = Cards(5,3)

while True:
    print("\n\n")
    print("на столе\n")
    for each in ng.drawPile: print(str.upper(each) + "🔴")
    choose = input("\nчто хотим сделать?\n 1 - sbros s ruki\n 2 - взять со стола\n 3 - взять с верха колоды\n 4 - сдать карты\n\n\n")
    
    if choose == "1":
        sbros_s_ruki = input("какие скинуть в сброс в формате wild,red")
        for each in sbros_s_ruki.split(","):
          ng.addToDiscard(each)
    if choose == "2":
        zabral_so_stola = input("какие карты взял в формате red,red")
        
        for each in zabral_so_stola.split(","):
          ng.pickFaceUpCard(each)
    if choose == "3":
        vzyat_iz_kolodi = input("сколько карт с верха взять")
        print(ng.dealCards(int(vzyat_iz_kolodi)))
    if choose == "4":
        print(ng.dealCards(5))
    print("\n\n####################\n")

   

class Cards():
    def __init__(self, sizeDrawPile, maxWilds):
        self.sizeDrawPile = sizeDrawPile
        self.possibleColors = ["red",   "orange", "yellow", 
                               "green", "blue",   "purple", 
                               "white", "black"
                               ]
        #add wilds                                             
        self.cards = ["wild" for x in range(14)] + \
                    [x for x in self.possibleColors for j in range(12)]

        self.maxWilds = maxWilds
                     
        self.shuffle(self.cards)
       
        #city1, city2, pointValue
       
        
        self.drawPile          = []
        self.discardPile       = []
        self.ticketDiscardPile = []

        self.addToDrawPile()
                
    def shuffle(self, cards):
        """shuffles cards in-place, nothing returned
        cards: list
        """
        random.shuffle(cards)
        
    def dealCard(self):
        """returns a single card"""
        if len(self.cards) == 0:
            self.restockCards()
        try:
            return self.cards.pop()
        except IndexError:
            print "\n There are no more cards in the deck! \n"
    
    def dealCards(self, numCards):
        """returns a list of (numCards) cards
        numCards: int
        """
        return [self.dealCard() for x in range(numCards)]
    
    
    def pickFaceUpCard(self, card):
        """returns one card from draw pile
        card: string
        """
        assert card in self.drawPile
        self.drawPile.remove(card)
        self.addToDrawPile()
        return card
        
    def pickFaceDown(self):
        """returns the next card in cards"""
        return self.dealCard()
    
    def addToDrawPile(self):
        """adds one more cards to draw pile"""
        nextCard = self.dealCard()
        if nextCard != None: #when the drawPile AND discardPile are empty
            self.drawPile.append(nextCard)
        
        if len(self.drawPile) < self.sizeDrawPile:
            self.restockDrawPile()
        
        #check to see if draw pile has reached maxWilds, 
        #if so, clear and create new drawPile
        if self.drawPile.count('wild') >= self.maxWilds:
            self.addToDiscard(self.drawPile)
            self.drawPile = []
            self.addToDrawPile()
            
            
    def getDrawPile(self):
        return self.drawPile
    
    def getDiscardPile(self):
        return self.discardPile
    
    def addToDiscard(self, cards):
        """adds one or more cards to the discard pile
        does not remove cards from source they came from
        """
        for card in cards:
            self.discardPile.append(card)
        if len(self.drawPile) < self.sizeDrawPile:
            self.restockDrawPile()
        
    def restockDrawPile(self):
        while len(self.drawPile) < self.sizeDrawPile:
            if len(self.cards) == 0 and len(self.discardPile) == 0:
                break
            elif len(self.cards) == 0:
                self.restockCards()
            nextCard = self.dealCard()
            if nextCard != None:
                self.drawPile.append(nextCard)    
    
    def cardsLeft(self):
        """returns the number of cards left in the cards pile"""
        return len(self.cards)
    
    def restockCards(self):
        """used when cards is empty, 
        restocks cards with discard pile and shuffles
        """
        assert len(self.cards) == 0
        self.cards = self.discardPile
        self.shuffle(self.cards)
        self.discardPile = []
    
        
    def isEmpty(self, pile):
        return len(pile) == 0
