from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Cart
from book.models import Book


def cart(request):
    return {'cart': Cart(request)}


@require_POST
def cart_add(request, product_id, quantity):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)

    cart.add(
        product=product,
        quantity=quantity,
        update_quantity=False,
    )

    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 10)]


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        required=True,
        initial=1,
        widget=forms.HiddenInput(),
    )
    update = forms.BooleanField(
        required=False, initial=False,
        widget=forms.HiddenInput
    )
