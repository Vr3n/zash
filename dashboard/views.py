from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.files import uploadedfile
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib import messages
from .forms import UploadFileForm
from .models import *

from django_searchbar.mixins import SearchBarViewMixin  # Search Bar

# Create your views here.

# File Upload View.
def UploadFile(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File Uploaded Successfully!!')
            return redirect('zash-dashboard')
    else:
        form = UploadFileForm()
    context = {
        'form': form,
        'title': 'Upload',
    }
    return render(request, 'dashboard/upload_file.html', context)

# Function to Delete File.
def delete_file(request, pk):
    if request.method == "POST":
        file = Files.objects.get(pk=pk)
        file.delete()
        messages.success(request, 'File Deleted Successfully!!')
    return redirect('zash-dashboard')

# Viewing the files in list.
class FileListView(ListView):
    model = Files
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'Files'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        return context

""" For Viewing the default Name of uploaded File.

file_default_name = Files.objects.create(attachment=file)
file_default_name.filename 

# file name as a string is returned.

"""
# Search Bar
class FilterView(SearchBarViewMixin, ListView):
    model = Files
    method = "GET"
    search_fields = ['name']    # Search in "name" field of model

# class FilterView(SearchBarViewMixin, ListView):
# #def FilterView(request, ListView):
#     model = Files
#     search_fields = ['name']    # Search in "name" field of model
#     # search_str = "" # Initiaize to Blank

#     # if "dashboard_search" in request.GET:
#     #     search_str = request.GET['search']

#     # queryset = Files.objects.filter(name__icontains = search_str)