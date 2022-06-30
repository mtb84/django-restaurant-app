from decimal import Decimal
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal)
    category = models.CharField(max_length=255)

    def __str__ (self):
        return self.name
