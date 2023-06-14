import unittest
import deck
import card


class TestDeck(unittest.TestCase):

    def test_deck_creation(self):
        card1 = card.Card("Question: What is the color of grass?", "Green", "Color")
        card2 = card.Card("Question: What is the color of grass?", "Green", "Color")
        cards_array = [card1, card2]
        deck1 = deck.Deck(cards_array)
        self.assertIsInstance(deck1, deck.Deck)

    def test_card_count(self):
        card1 = card.Card("Question: What is the color of grass?", "Green", "Color")
        card2 = card.Card("Question: What is the color of grass?", "Green", "Color")
        cards_array = [card1, card2]
        self.assertEqual(len(cards_array), 2)

    def test_cards_in_category(self):
        card1 = card.Card("Question: What is the color of grass?", "Green", "Color")
        card2 = card.Card("Question: What is the color of grass?", "Green", "Person")
        cards_array = [card1, card2]
        deck1 = deck.Deck(cards_array)

        result = deck1.cards_in_category("Color")
        self.assertEqual(len(result), 1)



if __name__ == '__main__':
    unittest.main()