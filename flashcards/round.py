class Round: 

    def __init__(self, deck):
        self.deck = deck
        self.turns = []

    def current_card(self):
        return self.deck.cards[0]
    
    def take_turn(self, guess):
       from flashcards import turn
       self.turns.append(turn.Turn( guess,self.current_card()))
       self.deck.cards.pop(0)
       return self.turns[-1]
    
    def number_correct(self):
        correct = 0
        for turn in self.turns:
            if turn.correct() == True:
                correct += 1
        return correct

    def number_correct_by_category(self,category):
        correct = 0
        for turn in self.turns:
            if turn.card.category == category and turn.correct() == True:
                correct += 1
        return correct
    
    def percent_correct(self):
        test = len(self.turns)
        return (self.number_correct() / float(test)) * 100
    
    def by_category(self,category):
        correct = 0
        for turn in self.turns:
            if turn.card.category == category:
                correct += 1
        return correct
    
    def percent_correct_by_category(self,category):
        test = self.by_category(category)
        return (self.number_correct_by_category(category)/ float(test)) * 100
    
        
    
    def current_card(self):
        return self.deck.cards[0]