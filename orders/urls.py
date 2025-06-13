from django.urls import path
from django.views.generic import TemplateView

from orders.views import order_detail, OrderSuccessView

urlpatterns = [
    path('', order_detail, name='order_detail'),
    path('success/', OrderSuccessView.as_view(), name='order_success'),
]