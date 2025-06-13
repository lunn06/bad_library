from django.contrib.auth import get_user_model
from django.db import models

from book.models import Book


class Order(models.Model):
    real_name = models.CharField(max_length=100)
    user = models.ForeignKey(get_user_model(), models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=256)

    class Meta:
        db_table = 'orders'


class OrdersBooks(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'orders_books'
