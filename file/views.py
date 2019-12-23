from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import fileForm
from django.views.generic import TemplateView, ListView, CreateView
from .models import file

# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        form = fileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = fileForm()
    return render(request, 'file/upload_book.html', {
        'form': form
    })

class UploadFileView(CreateView):
    model = file
    form_class = fileForm
    success_url = reverse_lazy('file:file_list')
    template_name = 'file/upload_book.html'

def file_list(request):
    files = file.objects.all()
    return render(request, 'file/file_list.html', {
        'files': files
    })

def delete_file(request, pk):
    if request.method == 'POST':
        sfile = file.objects.get(pk=pk)
        sfile.delete()
    return redirect('file/')