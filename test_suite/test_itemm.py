import unittest
import item_model as im


class DummyItem:
    def __init__(self, name):
        self.name = name


class TestItems(unittest.TestCase):

    def setUp(self):
        self.DummyGold = DummyItem('Gold')
        self.DummySwrd = DummyItem('Sword')


if __name__ == "__main__":
    unittest.main()


"""

Obsolete Code - No Longer in Use

self.TestBag = im.LootBag(3, 3, ' & ', 'rndvalue')

    def test_set_contents(self):
        self.TestBag.set_contents(self.DummyGold.name, 12)
        check_this = self.TestBag.return_contents()
        against_that = {'Gold': 12}
        self.assertEqual(check_this, against_that)

"""