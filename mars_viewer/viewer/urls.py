from django.urls import path

from . import views

urlpatterns = [
    path('', views.upload_file, name='upload'),
    path('upload/', views.upload_file, name='upload'),
    path('gallery/',views.gallery, name='gallery'),
]