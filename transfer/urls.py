from django.urls import path
from . import views

urlpatterns = [path("filereceive", views.FileReceiveView.as_view(), name="filereceive")]
