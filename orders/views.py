from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from book.models import Book
from cart.models import Cart
from orders.models import Order, OrdersBooks


class OrderSuccessView(TemplateView):
    template_name = "order_success.html"


def order_detail(request):
    if request.method == 'GET':
        cart = Cart(request)

        if len(cart.books()) == 0:
            return redirect('cart:cart_detail')

        return render(request, 'order_detail.html', context={'cart': cart})

    if request.method == 'POST':
        cart = Cart(request)

        name = request.POST.get('name', None)
        address = request.POST.get('address', None)
        if name is None or address is None:
            return render(request, 'order_detail.html', context={'cart': cart, "failed": True})

        order = Order(
            real_name=name,
            user=request.user,
            address=address,
        )
        order.save()

        orders_books = []
        for book, quantity in cart.books().items():
            orders_books.append(OrdersBooks(
                book=book,
                order=order,
                quantity=quantity,
            ))

        OrdersBooks.objects.bulk_create(orders_books)

        cart.clear()

        return redirect('order_success')

    return None
