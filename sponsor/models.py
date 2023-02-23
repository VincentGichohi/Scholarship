from django.db import models
from validation.models import CustomUser
from school.models import School
# from student.models import Student

SPONSORSHIP_TYPE = (
    ('Partial Sponsorship', 'Partial_Sponsorship'),
    ('Full Sponsorship', 'Full Sponsorship')
)


class Sponsor(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    school = models.ForeignKey("school.School", on_delete=models.DO_NOTHING, related_name="school")
    student = models.ForeignKey("student.Student", on_delete=models.DO_NOTHING)
    sponsorship_type = models.CharField(max_length=20, choices=SPONSORSHIP_TYPE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.email
