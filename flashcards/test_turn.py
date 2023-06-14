import unittest
import deck
import card
import turn


class TestTurn(unittest.TestCase):

    def test_turn_creation(self):
         card1 = card.Card("Question: What is the color of grass?", "Green", "Color")
         guess1 = "Green"
         turn1 = turn.Turn(guess1,card1)
         self.assertIsInstance(turn1, turn.Turn)

    def test_correct(self):
        card1 = card.Card("Question: What is the color of grass?", "Green", "Color")
        card2 = card.Card("Question: What is the color of grass?", "Blue", "Color")
        guess1 = "Green"
        guess2 = "Green"
        turn1 = turn.Turn(guess1,card1)
        turn2 = turn.Turn(guess2, card2 )
        result = turn1.correct()
        result2 = turn2.correct()
        self.assertEqual(result, True)
        self.assertEqual(result2, False)

    def test_feedback(self):
        card1 = card.Card("Question: What is the color of grass?", "Green", "Color")
        card2 = card.Card("Question: What is the color of grass?", "Blue", "Color")
        guess1 = "Green"
        guess2 = "Green"
        turn1 = turn.Turn(guess1,card1)
        turn2 = turn.Turn(guess2, card2 )
        result = turn1.feedback()
        result2 = turn2.feedback()
        self.assertEqual(result, "Correct!")
        self.assertEqual(result2, "Incorrect!")

if __name__ == '__main__':
    unittest.main()