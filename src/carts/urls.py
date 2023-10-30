from django.urls import path

from . import views

app_name = 'carts'

urlpatterns = [
    path('add/<slug>', views.cart_add, name='cart_add'),
    path('remove/<slug>', views.cart_remove, name='cart_remove'),
    path('', views.cart_view, name='cart'),
]
