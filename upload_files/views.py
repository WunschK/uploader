from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, "upload_files/index.html")

def upload_file(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'upload_files/upload.html', {'file_url': file_url})
    return render(request, 'upload_files/upload.html')

def file(request):
    return HttpResponse("Starting point for files and details")