from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import FileUploadForm
from .api_test import get_date_from_file, read_dates, process_query
import os

def index(request):
    return render(request,'viewer/index.html')

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            # Store the uploaded file as a query.
            process_query(request.FILES['file'])
            # Redirect to query view or maybe do a javascript alert here instead of a redirect? 
            return HttpResponseRedirect('/gallery')
    else:
        form = FileUploadForm()
    return render(request, 'viewer/fileUpload.html', {'form': form})

def gallery(request):
    root = os.path.dirname(os.path.realpath(__file__))
    photodir = os.path.join(root,'photos')
    dirs = os.listdir(photodir)
    full_path = []
    for d in dirs:
        full_path.append(os.path.join(photodir, d,'frontLeft.jpg'))
    context = {'paths':full_path}
    return render(request, 'viewer/gallery.html',context)