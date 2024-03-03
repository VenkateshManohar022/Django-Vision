from django.db import models
from django.contrib.auth.models import User
import cv2
import numpy as np
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from pathlib import Path
from .utils import selectionChoices
from django.urls import reverse
import requests


# Create your models here.

ACTION_CHOICES = (('GRAY','GrayScale'),
                  ('HSV','Colorized HSV'),
                  ('BLUR','Blurred'),
                  ('EDGE','Edge Detection'),
                  ('FACE','Face Detection'))


class ImageModel(models.Model):
    image = models.ImageField(upload_to='model/original/')
    modified_image = models.ImageField(upload_to='model/modified/',null=True,blank=True)

    choice = models.CharField(max_length=100,null=True,choices=ACTION_CHOICES)
    created = models.DateTimeField(auto_now_add = True)
    
    def save(self, *args, **kwargs):
      pather = Path(self.image.path)
      if self.image:
        # Read the image data as bytes
        image_bytes = self.image.read()

        # Decode the image data into an OpenCV image object
        image_np = np.frombuffer(image_bytes, np.uint8)
        image_cv2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
   
        # Convert the image according to the choices
        convert_img = selectionChoices(image_cv2,self.choice)

        # Convert the grayscale image back to bytes
        retval, buffer = cv2.imencode('.jpg', convert_img)
        image_bytes = buffer.tobytes()

        # Create a new InMemoryUploadedFile object with the converted image data
        self.modified_image = InMemoryUploadedFile(BytesIO(image_bytes), None, f'{pather.name}', f'image/{pather.suffix}', len(image_bytes), None)

        # Call the save method of the parent class to save the model instance
      super().save(*args, **kwargs)


