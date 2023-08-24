from django.db import models

# Create your models here.
class Imaze(models.Model):
    photo = models.ImageField(upload_to='myimaze')
    date = models.DateTimeField(auto_now_add=True)
    