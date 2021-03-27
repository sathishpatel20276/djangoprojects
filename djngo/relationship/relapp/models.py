from django.db import models

# Create your models here.
'''
#one to one
class person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    contact = models.IntegerField()

    def __str__(self):
        return self.name
class voter(models.Model):
    voter_id = models.IntegerField()
    person = models.OneToOneField('person',on_delete = models.CASCADE)

#many to one
class employee(models.Model):
    emp_name = models.CharField(max_length=30)
    emp_number  = models.IntegerField()
    emp_address = models.TextField()

    def __str__(self):
        return self.emp_name
class bankaccount(models.Model):
    bank_number = models.IntegerField()
    bank_name = models.CharField(max_length=50)
    employee = models.ForeignKey('employee',on_delete = models.CASCADE)

    def __str__(self):
        return self.bank_name
'''
#many to many

class movie(models.Model):
    m_name = models.CharField(max_length=50)
    m_theatre = models.CharField(max_length=100)
    ticket_price = models.IntegerField()

    def __str__(self):
        return self.m_name
class actor(models.Model):
    actor_name = models.CharField(max_length=100)
    actor_rating = models.DecimalField(max_digits=20,decimal_places=2)
    movie = models.ManyToManyField('movie')

    def __str__(self):
        return self.actor_name

