from django.shortcuts import render
from .models import Company
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.
class CompanyListView(ListView):
    model = Company
    template_name = 'company_list.html'

class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company_details.html'

class CompanyCreateView(CreateView):
    model = Company
    fields = ('name','location','ceo')
    template_name = 'company_form.html'

class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('name','ceo')
    template_name = 'company_form.html'

class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('companies')
    template_name = 'company_confirm_delete.html'
