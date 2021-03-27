from django.db import models

# Create your models here.

class OjasPdfData(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to = 'books/pdf')
    cover = models.ImageField(upload_to = 'books/images', bloank =True, null = True)
