from rest_framework import generics
from .models import Menu
from .serializer import MenuSerializer
from .models import Menu

# Create your views here.


class MenuListAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
