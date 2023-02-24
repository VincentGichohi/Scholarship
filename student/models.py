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
    status = models.CharField(max_length=10, choices=SPONSORSHIP_STATUS)
    sponsorship_type = models.ForeignKey(Sponsor, on_delete=models.DO_NOTHING, related_name="sponsorship")
    birth_cert_file = models.FileField(upload_to='files')
    national_id = models.FileField(upload_to='files')

    def __str__(self):
        return self.email



