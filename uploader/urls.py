from django.contrib import admin
from django.urls import path, include
from .views import ImageUploadView, MyImagesView

urlpatterns = [
    path('upload/', ImageUploadView.as_view()),
    path('my-images/', MyImagesView.as_view()),
]