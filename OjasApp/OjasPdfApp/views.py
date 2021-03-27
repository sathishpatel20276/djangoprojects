from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from OjasPdfApp.forms import OjasProfileForm
from .models import OjasPdfData

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'
def pdf_list(request):
    pdf = OjasPdfData.objects.all()
    return render(request, 'pdf_list.html',{'pdf':pdf})
def upload_pdf(request):
    if request.method == "POST":
        form = OjasProfileForm(request.POST, request.FILES)
        if form.is_valied():
            form.save()
            return redirect('pdf_list')
    else:
        form = OjasPdfData()
    return render(request, 'upload_pdf.html',{'form':form})
def delete_pdf(request, pk):
    if request.method == 'POST':
        pdf = OjasPdfData.objects.get(pk=pk)
        pdf.delete()
    return redirect('pdf_list')
