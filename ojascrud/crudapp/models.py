from django.db import models
# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.title
class Student(models.Model):
    fullname = models.CharField(max_length = 30)
    roll_no = models.CharField(max_length = 40)
    mobile = models.CharField(max_length = 100)
    course = models.ForeignKey(Course,on_delete = models.CASCADE)