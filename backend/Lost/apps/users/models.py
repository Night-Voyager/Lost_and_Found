from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student', null=True)
    name = models.CharField(max_length=50, default="")
    studentID = models.PositiveIntegerField(default="")
    openID = models.CharField(max_length=50, default="")
    unionID = models.CharField(max_length=50, default="")
