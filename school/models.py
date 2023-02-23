from django.db import models
from validation.models import CustomUser
# from student.models import Student
# from sponsor.models import Sponsor


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
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'school'

    def __str__(self):
        return self.user.email


class School(models.Model):
    school_name = models.CharField(max_length=200)
    student = models.ForeignKey("student.Student", on_delete=models.DO_NOTHING)
    sponsor = models.ForeignKey("sponsor.Sponsor", on_delete=models.DO_NOTHING, related_name='sponsor_name')
    sponsorship_type = models.ForeignKey("sponsor.Sponsor", on_delete=models.DO_NOTHING, related_name="type_of_sponsorship")
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    school_address = models.CharField(max_length=250)
    academic_level = models.CharField(max_length=20, choices=ACADEMIC_LEVELS)
    expected_year_of_completion = models.DateField()

    def __str__(self):
        return self.user.email


class Reasons(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reasons_to_be_sponsored = models.TextField()
    recommendation_letter = models.FileField(upload_to='files')

    def __str__(self):
        return self.user.email


