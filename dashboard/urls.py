from django.urls import path, include
from dashboard import views as d_view
from .views import FileListView
from .models import *

# Write your URL patterns Here
urlpatterns = [
    path('dashboard/', FileListView.as_view(model=Files), name='zash-dashboard'),
    path('dashboard/upload', d_view.UploadFile, name='upload-file'),
    path('dashboard/<int:pk>', d_view.delete_file, name='delete-file'),
]
