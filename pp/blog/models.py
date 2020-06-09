from django.db import models

# Create your models here.
class AllBlog(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='blog/images')
    description = models.CharField(max_length=50)
    date = models.DateField(max_length=10)
