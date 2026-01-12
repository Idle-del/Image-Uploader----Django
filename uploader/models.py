from django.db import models

# Create your models here.
class ImageUpload(models.Model):
    firebase_uid = models.CharField(max_length=128)
    image = models.ImageField(upload_to='profile_pics/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.firebase.uid
