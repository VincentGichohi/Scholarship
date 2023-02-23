from django.db import models
from validation.models import CustomUser


SPONSORSHIP_STATUS = [
    ('Pending', 'PENDING'),
    ('Approved', 'APPROVED'),
    ('Rejected', 'REJECTED')
]


class Student(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=SPONSORSHIP_STATUS)
    phone = models.IntegerField(blank=False, null=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    birth_cert_file = models.FileField(upload_to='files')
    national_id = models.FileField(upload_to='files')

    def __str__(self):
        return self.email


