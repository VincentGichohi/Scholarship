from django.db import models
from validation.models import CustomUser


class Student(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=255, null=False, blank=False)
    birth_cert_file = models.FileField(upload_to='files')
    national_id = models.FileField(upload_to='files')

    def __str__(self):
        return self.email


