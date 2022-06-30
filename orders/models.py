from django.db import models

class Order(models.Model):
    order = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.data)