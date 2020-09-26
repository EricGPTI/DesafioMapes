from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('send', views.send, name='send'),
    path('report', views.report, name='report'),
    path('process_file', views.file, name='file'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
