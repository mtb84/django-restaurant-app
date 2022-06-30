from django.urls import path
from .views import OrderListAPIView, OrderDetailAPIView

app_name = 'orders'

urlpatterns = [
    path('<int:pk>/', OrderDetailAPIView.as_view()),
    path('', OrderListAPIView.as_view()),
]