from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory

from book.models import Book
from cart.models import Cart


class CartTestCase(TestCase):
    def setUp(self):
        self.request = RequestFactory().post('/cart')
        self.request.session = self.client.session
        self.request.user = get_user_model()(username='test')
        self.cart = Cart(self.request)

        self.request.user.save()

    def tearDown(self):
        Book.objects.all().delete()
        get_user_model().objects.all().delete()
        self.cart.clear()

    def testAddBook(self):
        book1 = self._create_book("book1", 100)
        book2 = self._create_book("book2", 200)

        self.cart.add(book1, 1)
        self.cart.add(book2, 2)

        items = list(self.cart)

        self.assertEqual(items[0]['product'], book1)
        self.assertEqual(items[0]['price'], book1.price)
        self.assertEqual(items[0]['quantity'], 1)
        self.assertEqual(items[0]['total_price'], 1*book1.price)

        self.assertEqual(items[1]['product'], book2)
        self.assertEqual(items[1]['price'], book2.price)
        self.assertEqual(items[1]['quantity'], 2)
        self.assertEqual(items[1]['total_price'], 2*book2.price)

    def testClearCart(self):
        book1 = self._create_book("book1", 100)
        book2 = self._create_book("book2", 200)

        self.cart.add(book1, 1)
        self.cart.add(book2, 2)

        self.assertEqual(len(self.cart), 3)

        self.cart.clear()

        cart = Cart(self.request)
        self.assertEqual(len(cart), 0)

    def testRepresentCart(self):
        book1 = self._create_book("book1", 100)
        book2 = self._create_book("book2", 200)

        self.cart.add(book1, 1)
        self.cart.add(book2, 2)

        self.assertEqual(len(self.cart), 3)

        cart = Cart(self.request)
        self.assertEqual(len(cart), 3)

    def testGetTotalPrice(self):
        book1 = self._create_book("book1", 100)
        book2 = self._create_book("book2", 1000)

        self.cart.add(book1, 3)
        self.cart.add(book2, 1)

        self.assertEqual(self.cart.get_total_price(), book1.price*3 + book2.price)

    def testCartRemove(self):
        book1 = self._create_book("book1", 100)
        book2 = self._create_book("book2", 1000)

        self.cart.add(book1, 3)
        self.cart.add(book2, 1)

        self.assertEqual(len(self.cart), 4)

        self.cart.remove(book1)

        self.assertEqual(len(self.cart), 1)


    def _create_book(self, name, price):
        book = Book(
            title=name,
            price=price,
            user=self.request.user,
        )

        book.save()

        return book
