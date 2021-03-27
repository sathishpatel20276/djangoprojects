from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    #context = "hi welcome to my home page"
    return render(request,'index.html')

def contact(request):
    context = "hi welcome to my contact page"
    return HttpResponse(context)

def service(request):
    context = "hi welcome to my service page"
    return HttpResponse(context)

def product(request):
    context = "hi welcome to my product page"
    return HttpResponse(context)

