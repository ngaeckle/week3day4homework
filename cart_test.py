from cart import Shop,Item,Cart
import unittest

class CartTest(unittest.TestCase):
    def test_Item(self):
        apple = Item("apple", 1, 1)
        self.assertEqual(apple.name, 'apple')


    def test_Cart(self):
        test_cart = Cart()
        test_cart.add("Anything", 3, 3)
        self.assertEqual(len(test_cart.items), 1)
        test_cart.delete[0]
        self.assertEqual(len(test_cart.items), 0)