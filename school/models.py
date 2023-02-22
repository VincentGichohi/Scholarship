from django.db import models
from validation.models import CustomUser
from student.models import Student

ACADEMIC_LEVELS = [
    ('Certificate', 'CERTIFICATE'),
    ('Diploma', 'DIPLOMA'),
    ('Bachelors Degree', 'Bachelors Degree'),
    ('Masters', 'Masters')
]


class School(models.Model):
    school_name = models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    school_address = models.CharField(max_length=250)
    academic_level = models.CharField(max_length=2, choices=ACADEMIC_LEVELS)
    expected_year_of_completion = models.DateField()

    def __str__(self):
        return self.user.email
