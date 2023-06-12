from django.db import models

# Create your models here.
class RegModels(models.Model):
    FName=models.CharField(max_length=20)
    LName=models.CharField(max_length=20)
    UserName=models.CharField(max_length=20)
    Password=models.CharField(max_length=10)
    CPassword=models.CharField(max_length=10)
    Emailid=models.EmailField()
    MobileNo=models.CharField(max_length=13)