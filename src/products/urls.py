from django.urls import path

from . import views


app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('<str:slug>/', views.ProductDetailView.as_view(), name='detail'),
]
