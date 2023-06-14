import unittest
import card 

class TestCard(unittest.TestCase):
    def test_card_creation(self):
        card1 = card.Card("Question: What is the color of grass?", "Green", "Color")
        self.assertIsInstance(card1, card.Card)

if __name__ == '__main__':
    unittest.main()