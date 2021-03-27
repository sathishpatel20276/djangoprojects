from django.db import models

# Create your models here.
class FakeData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    job = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    city = models.CharField(max_length=100)
    dob = models.DateField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name