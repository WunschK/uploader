from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.staticfiles.utils import get_files
from os.path import isfile, join
from os import listdir

# Create your views here.
def index(request):
    return render(request, "upload_files/index.html")

def upload_file(request):
    '''displays upload form with a list of already uploaded files.'''
    mypath = 'media'
    allfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    if request.method == 'POST' and request.FILES['upload']:
        '''handles file uploads and redirects to upload'''
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
#        file_url = fss.url(file)
#        mypath = 'media'
        return redirect("/upload")
    return render(request, 'upload_files/upload.html', {'allfiles': allfiles})

def file(request):
    return HttpResponse("Starting point for files and details")