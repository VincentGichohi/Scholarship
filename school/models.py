from django.db import models
from validation.models import CustomUser
from student.models import Student
from sponsor.models import Sponsor


ACADEMIC_LEVELS = [
    ('Certificate', 'CERTIFICATE'),
    ('Diploma', 'DIPLOMA'),
    ('Bachelors Degree', 'Bachelors Degree'),
    ('Masters', 'Masters')
]


class Course(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


class School(models.Model):
    school_name = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.DO_NOTHING)
    sponsorship_type = models.ForeignKey(Sponsor, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    school_address = models.CharField(max_length=250)
    academic_level = models.CharField(max_length=2, choices=ACADEMIC_LEVELS)
    expected_year_of_completion = models.DateField()

    def __str__(self):
        return self.user.email


class Reasons(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reasons_to_be_sponsored = models.TextField()
    recommendation_letter = models.FileField(upload_to='files')

    def __str__(self):
        return self.user.email


