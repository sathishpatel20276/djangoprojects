from django.shortcuts import render
from .models import vending_machine
from django.views.generic import ListView
# Create your views here.
class cooldrinks(ListView):
    model = vending_machine
    template_name = 'cooldrink_list.html'