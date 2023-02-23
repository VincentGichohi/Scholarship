from django.db import models
from validation.models import CustomUser


class Staff(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.email
