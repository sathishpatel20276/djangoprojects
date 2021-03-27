from django.db import models

# Create your models here.
class college(models.Model):
    college_name = models.CharField(max_length=100)
    college_location = models.CharField(max_length=200)
    college_contact = models.IntegerField()

    class meta:
        abstaract = True
class student(college):
    student_name = models.CharField(max_length=100)

class staff(college):
    staff_name = models.CharField(max_length=100)