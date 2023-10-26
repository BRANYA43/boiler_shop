from django.urls import path
from django.views.generic import TemplateView


app_name = 'orders'

urlpatterns = [
    path(
        'make_order_success_message/',
        TemplateView.as_view(template_name='orders/make_order_success_message.html'),
        name='make_order_success_message',
    ),
]
