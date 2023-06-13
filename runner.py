from flashcards import card 
from flashcards import deck
from flashcards import turn
from flashcards import round
 

card_1 = card.Card("Question: What is 5 + 5?", "10", "STEM")
card_2 = card.Card("Question: What is the color of grass?", "Green", "Color")
card_3 = card.Card("Question: What is Wade's middle name?", "Collin", "Person")
card_4 = card.Card("Question: What is my favorite pet?", "Dog", "Person")

cards = [card_1, card_2, card_3, card_4]

deck_1 = deck.Deck(cards)

round_1 = round.Round(deck_1)

print("Welcome! You're playing with 4 cards.")
print("_" * 30)
print("This is card 1 out of 4")


guess1 = int(input(round_1.deck.cards[0].question))
string1 = str(guess1)
turn1 = round_1.take_turn(string1)
print(turn1.feedback())

print("This is card 2 out of 4")
guess2 = input(round_1.deck.cards[0].question)
turn2 = round_1.take_turn(guess2)

print(turn2.feedback())


print("This is card 3 out of 4")
guess3 = input(round_1.deck.cards[0].question)
turn3 = round_1.take_turn(guess3)
print(turn3.feedback())

print("This is card 4 out of 4")
guess4 = input(round_1.deck.cards[0].question)
turn4 = round_1.take_turn(guess4)
print(turn4.feedback())

print("****** Game Over! ******")
print("You had " + str(round_1.number_correct()) + " correct guesses out of 4 for a total score of " + str(round_1.percent_correct()))
print("Person - " + str(round_1.percent_correct_by_category("Person")) + " percent correct")
print("STEM - " + str(round_1.percent_correct_by_category("STEM")) + " percent correct")
print("Color - " + str(round_1.percent_correct_by_category("Color")) + " percent correct")







