from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.files import uploadedfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
from django.contrib import messages
from users.models import Profile, CustomUser
from .forms import UploadFileForm
from .models import Files


from django_searchbar.mixins import SearchBarViewMixin  # Search Bar

# Create your views here.

# File Upload View.

def UploadFile(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            form.instance.owner = request.user
            instance.save()
            messages.success(request, 'File Uploaded Successfully!!')
            return redirect('zash-dashboard')
    else:
        form = UploadFileForm()
    context = {
        'form': form,
        'title': 'Upload',
    }
    return render(request, "dashboard/upload_file.html", context)

    # def form_valid(self, form):
    #     form.instance.owner = self.request.user
    #     return super().form_valid(form)


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
    ordering = ['-uploaded_at']

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        return context
<<<<<<< HEAD
=======

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
>>>>>>> bd0737e0fdce215a068daf25099c766a038972b9
