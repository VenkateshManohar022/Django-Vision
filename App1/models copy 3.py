from django.db import models
from django.contrib.auth.models import User
import cv2
import numpy as np
import os
from django.core.files.base import ContentFile
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
    # modified_image = models.ImageField(upload_to='model/modified/')

    description = models.CharField(max_length=100,null=True)

    def save(self, *args, **kwargs):
        convert_img = cv2.cvtColor(cv2.imread(self.image),cv2.COLOR_BGR2GRAY)
        self.image = (convert_img)

        # Call the save method of the parent class to save the model instance
        super().save(*args, **kwargs)
