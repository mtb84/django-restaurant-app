from django.urls import path
from .views import MenuListAPIView, AdminMenuListAPIView, MenuDetailAPIView

app_name = 'menu'

urlpatterns = [
    path('<int:pk>/', MenuDetailAPIView.as_view()),
    path('admin/', AdminMenuListAPIView.as_view()),
    path('', MenuListAPIView.as_view()),
]