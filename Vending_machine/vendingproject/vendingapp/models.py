from django.db import models


# Create your models here.
class vending_machine(models.Model):
    cooldrink_name = models.CharField(max_length=25)
    price = models.DecimalField(default=False,max_digits=10,decimal_places=2)

    def __str__(self):
       return self.cooldrink_name
