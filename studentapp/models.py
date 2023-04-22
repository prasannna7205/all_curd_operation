from django.db import models

# Create your models here.
class StudentData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
    course=models.CharField(max_length=100)
