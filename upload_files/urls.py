from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name='upload'),
    path('upload/dz_upload/', views.dz_upload, name='dz_upload'),
] + static(settings.MEDIA_URL)

