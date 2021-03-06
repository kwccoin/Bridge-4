
import unittest

import Card
import Deck
import Hand

class TestHand(unittest.TestCase):
    def setUp(self):
        super(TestHand, self).setUp()
        d1 = Deck.Deck()
        self.h1, self.h2, self.h3, self.h4 = d1.deal()
        vals = ((4,1), (4,2), (4,3), (4,4),
                (5,1), (5,2), (5,3), (5,4),
                (6,1), (6,2), (6,3), (6,4),
                (7,1))
        self.cards = [Card.Card(*v) for v in vals]
        self.hnd = Hand.Hand(self.cards)

    def test_longest(self):
        """longest should do as expected"""
        self.assertEqual(self.h1.longest, [('spades', 13)])
        self.assertEqual(self.h2.longest, [('hearts', 13)])
        self.assertEqual(self.h3.longest, [('diamonds', 13)])
        self.assertEqual(self.h4.longest, [('clubs', 13)])

    def test_strongest(self):
        """sringest has known output"""
        self.assertEqual(self.h1.strongest, [('spades', 10)])
        self.assertEqual(self.h2.strongest, [('hearts', 10)])
        self.assertEqual(self.h3.strongest, [('diamonds', 10)])
        self.assertEqual(self.h4.strongest, [('clubs', 10)])

    def test_init(self):
        """test input checking"""
        self.assertTrue(hasattr(self.h1, "n_cards"))
        self.assertTrue(hasattr(self.h1, "distro"))
        self.assertTrue(hasattr(self.h1, "balanced"))
        self.assertRaises(ValueError, Hand.Hand, self.cards[1:])

    def test_str(self):
        self.assertTrue(isinstance(self.h1.__str__(), str))

    def test_get_hc(self):
        self.assertEqual(self.h1.hc, 10)
        self.assertEqual(self.h2.hc, 10)
        self.assertEqual(self.h3.hc, 10)
        self.assertEqual(self.h4.hc, 10)
        self.assertEqual(self.hnd.hc, 0)

    def test_is_balanced(self):
        self.assertFalse(self.h1.balanced)
        self.assertFalse(self.h2.balanced)
        self.assertFalse(self.h3.balanced)
        self.assertFalse(self.h4.balanced)
        self.assertTrue(self.hnd.balanced)

    # TODO add test_pps!!


if __name__ == '__main__':
    unittest.main()
