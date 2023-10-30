from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'orders'

urlpatterns = [
    path('make_order/', views.MakeOrderView.as_view(), name='make_order'),
    path(
        'make_order/success/',
        TemplateView.as_view(template_name='orders/success_making_order.html'),
        name='success_making_order',
    ),
]
