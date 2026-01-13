from django.contrib import admin
from django.urls import path, include
from .views import ImageUploadView, MyImagesView, PublicImagesView

urlpatterns = [
    path('upload/', ImageUploadView.as_view()),
    path('my-images/', MyImagesView.as_view()),
    path('public-images/<str:firebase_uid>/', PublicImagesView.as_view())
]