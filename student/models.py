from django.db import models
from validation.models import CustomUser
from sponsor.models import Sponsor

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
    sponsorship_type = models.ForeignKey(Sponsor, on_delete=models.DO_NOTHING)
    email = models.EmailField(max_length=255, null=False, blank=False)
    birth_cert_file = models.FileField(upload_to='files')
    national_id = models.FileField(upload_to='files')

    def __str__(self):
        return self.email


class StudentProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    phone = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    email = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.email
