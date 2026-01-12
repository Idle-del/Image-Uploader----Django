from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from .models import ImageUpload
from .utils import verify_firebase_token

# Create your views here.

class ImageUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request):
        try:
            user_uid = verify_firebase_token(request)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        
        image = request.FILES.get('image')
        if not image:
            return Response({"error" : "No image provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        image_upload = ImageUpload.objects.create(
            firebase_uid=user_uid,
            image=image,
        )
        return Response({"message": "Image uploaded successfully", "image_url": image_upload.image.url}, status=status.HTTP_201_CREATED)
    
class MyImagesView(APIView):
    def get(self, request):
        try:
            user_uid = verify_firebase_token(request)
            print("User UID:", user_uid)
        except Exception as e:
            # return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
            print("Authentication error:", str(e))
            return Response({"error": "Authentication failed"}, status=status.HTTP_401_UNAUTHORIZED)
        
        img = ImageUpload.objects.filter(firebase_uid=user_uid).order_by('-created_at').first()
        
        if not img:
            return Response({"error": "No images found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"image_url": img.image.url}, status=status.HTTP_200_OK)
