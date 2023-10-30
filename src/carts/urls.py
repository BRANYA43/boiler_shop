from django.urls import path

from . import views

app_name = 'carts'

urlpatterns = [
    path('add/<slug>', views.cart_add, name='cart_add'),
    path('remove/<slug>', views.cart_remove, name='cart_remove'),
    path('clear', views.cart_clear, name='cart_clear'),
    path('set_quantity/<slug>', views.cart_set_quantity, name='cart_set_quantity'),
    path('', views.cart_view, name='cart'),
]
