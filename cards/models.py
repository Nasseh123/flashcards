from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile (models.Model):
    profile_pic=models.ImageField(upload_to='profile/',blank=True)
    bio=models.CharField(max_length=150,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
class Subjects(models.Model):
    subjects=models.CharField(max_length=50)
    
class cards(models.Model):
    title=models.CharField(max_length=50)
    body=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now_add=True)
    subject=models.ForeignKey(Subjects,on_delete=models.CASCADE)