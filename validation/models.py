from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
# from phonenumber_field.phonenumber import PhoneNumber
# from PIL import Image


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = email=self.normalize_email(email),
        
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a regular user with a given email and password
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
        

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = ((1, "Admin"), (2, "Staff"), (3, "Student"), (4, "Sponsor"))
    GENDER = (("M", "Male"), ("F", "Female"))
    ACTIVE_STATUS = (
        ('active', "Active"),
        ('inactive', 'Inactive')
    )

    email = models.EmailField(unique=True)
    user_type = models.CharField(default=1, choices=USER_TYPE, max_length=1)
    active = models.CharField(max_length=20, choices=ACTIVE_STATUS, default='inactive')
    gender = models.CharField(max_length=1, choices=GENDER)
    password2 = models.CharField(default='', max_length=100)
    profile_pic = models.ImageField()
    is_staff = models.BooleanField(default=False)
    is_sponsor = models.BooleanField(default=False)
    fcm_token = models.TextField(default="")  # For firebase notifications
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(default="", upload_to="profile_images")

    def __str__(self):
        return self.user.email

    # def save(self, *args, **kwargs):
    #     super().save()
    #
    #     img = Image.open(self.avatar.path)
    #
    #     if img.height > 100 or img.width > 100:
    #         new_img = (100, 100)
    #         img.thumbnail(new_img)
    #         img.save(self.avatar.path)
