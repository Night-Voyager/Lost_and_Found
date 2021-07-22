from django.db import models

# Create your models here.


class FindObject(models.Model):
    objectName = models.CharField(max_length=50, default="")
    objectImage = models.ImageField(upload_to="images/%Y/%m/", null=True, blank=True)
    ownerName = models.CharField(max_length=50, default="")
    ownerID = models.PositiveIntegerField(default="")
    ownerContactWay = models.CharField(max_length=3, default="")
    ownerContactNum = models.CharField(max_length=20, default="")
    remarks = models.CharField(max_length=200, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    publisher = models.PositiveIntegerField(default="")


class FindOwner(models.Model):
    objectName = models.CharField(max_length=50, default="")
    objectImage = models.ImageField(upload_to="images/%Y/%m/", null=True, blank=True)
    haveOwnerInfo = models.BooleanField(default=False)
    ownerName = models.CharField(max_length=50, null=True, blank=True)
    ownerID = models.PositiveIntegerField(null=True, blank=True)
    place = models.CharField(max_length=10, default="")
    pickerName = models.CharField(max_length=50, null=True, blank=True)
    pickerContactWay = models.CharField(max_length=3, null=True, blank=True)
    pickerContactNum = models.CharField(max_length=20, null=True, blank=True)
    remarks = models.CharField(max_length=200, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    publisher = models.PositiveIntegerField(default="")
