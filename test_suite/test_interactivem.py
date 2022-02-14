import unittest
import interactive_model as im

class TestInteractives(unittest.TestCase):

    def setUp(self):
        self.Desk = im.ContainerModel(2, 2, 'Desk', 'someid', ' d ')

    def test_set_container(self):
        self.Desk.set_container('Sword', 1)
        self.assertIn('Sword', self.Desk.return_container())
