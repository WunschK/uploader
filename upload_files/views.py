from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.staticfiles.utils import get_files
from os.path import isfile, join
from os import listdir
from .models import Image

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
        return redirect("/upload")
    return render(request, 'upload_files/upload.html', {'allfiles': allfiles})

def file(request):
    return HttpResponse("Starting point for files and details")


def dz_upload(request):
    if request.method == 'POST':
        my_file = request.FILES['file']
        Image.objects.create(image=my_file)
        return HttpResponse('')
    return JsonResponse({
        'post': 'false'
    })



