from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=250)
  created_at = models.DateTimeField()
  
class News(models.Model):
  title = models.CharField(max_length=250)
  text = models.TextField()
  created_at = models.DateTimeField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
