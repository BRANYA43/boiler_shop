from django.urls import path
from django.views.generic import TemplateView

from . import views


app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('<str:slug>/', TemplateView.as_view(template_name='products/detail.html'), name='detail'),
]
