from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a user with the given email and password
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff with the given email and password
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a user with the given email and password
        """
        user = self.create_user(
            
        )
class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email_address',
        max_length = 255,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) #A admin user; a non-superuser
    admin = models.BooleanField(default=False) # a superuser


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #Emails and passwords are required by default

    def get_full_name(self):
        #The user is identified by their email address.
        return self.email

    def get_short_name(self):
        #The user is identified by their email address
        return self.email

    def _str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission"
        #Simplest answer: Yes always
        return True

    def has_module_perm(self, app_label):
        "Does the user have permissions to view the app?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff"
        return self.staff

    @property
    def is_admin(self):
        "Is the user an admin member"
        return self.admin