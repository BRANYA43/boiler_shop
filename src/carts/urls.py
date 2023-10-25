from django.urls import path

from . import views

app_name = 'carts'

urlpatterns = [
    path('add/<slug>', views.cart_add, name='cart_add'),
]
