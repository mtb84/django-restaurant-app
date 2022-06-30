from rest_framework import generics
from .models import Menu
from .serializer import MenuSerializer

class MenuListAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer 


class AdminMenuListAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    

class MenuDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer