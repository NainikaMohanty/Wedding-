from django.db import models
class Registerer(models.Model):
    Name=models.CharField(max_length=30)
    Mobile_Number=models.IntegerField()
    Email=models.EmailField()
    Username=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)
    Confirm_password=models.CharField(max_length=30)

