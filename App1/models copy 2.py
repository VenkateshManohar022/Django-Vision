from django.db import models
from django.contrib.auth.models import User
import cv2
import numpy as np
import os
from django.core.files.base import ContentFile
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from pathlib import Path


# Create your models here.


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)


class Task(models.Model):
    user = models.ForeignKey(User,
                             on_delete = models.RESTRICT)
    title = models.CharField(max_length = 200)
    description = models.TextField(null=True)
    complete = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)



class ImageModel(models.Model):
    image = models.ImageField(upload_to='model/original/')
    modified_image = models.ImageField(upload_to='model/modified/',null=True)

    description = models.CharField(max_length=100,null=True)
    
    def save(self, *args, **kwargs):
      pather = Path(self.image.path)
      if self.image:
        # Read the image data as bytes
        image_bytes = self.image.read()

        # Decode the image data into an OpenCV image object
        image_np = np.frombuffer(image_bytes, np.uint8)
        image_cv2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

        # Convert the image to grayscale
        convert_img = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2GRAY)

        # Convert the grayscale image back to bytes
        retval, buffer = cv2.imencode('.jpg', convert_img)
        image_bytes = buffer.tobytes()

        # Create a new InMemoryUploadedFile object with the converted image data
        self.modified_image = InMemoryUploadedFile(BytesIO(image_bytes), None, f'{pather.name}', f'image/{pather.suffix}', len(image_bytes), None)

        # Call the save method of the parent class to save the model instance
      super().save(*args, **kwargs)


