from django.db import models

# Create your models here.
class School(models.Model):
      name = models.CharField(max_length=100)
      location = models.CharField(max_length=100)
      principal = models.CharField(max_length=100)

from django.contrib.auth.models import User

class Student(models.Model):
          name = models.CharField(max_length=100)
          age = models.IntegerField()
          place = models.CharField(max_length=100)
          school = models.ForeignKey(School, on_delete= models.CASCADE,related_name='students')
          User = models.OneToOneField(User,on_delete= models.CASCADE)

