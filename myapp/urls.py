
from django.urls import path

from . import views

urlpatterns = [
   
    path('', views.GeneratePdf.as_view(), name = "pdf" ) ,
    path('download/', views.downloadPdf.as_view(), name = "download-pdf" )
]