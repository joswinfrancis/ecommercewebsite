from django.db import models

# Create your models here.
#model for themes
class Sitesetting(models.Model):
    banner=models.ImageField(upload_to='media/site/')
    caption=models.TextField()