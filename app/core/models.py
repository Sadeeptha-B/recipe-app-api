from django.db import models

# The Base user manager provides the helper functions for creating a user/superuser.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,\
     PermissionsMixin


# Extend base user manager and override functions
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        user = self.model(email=email, **extra_fields)
        user.set_password(password) # encrypt and set password
        user.save(using=self._db) # self._db is good practice (support multiple db)

        return user



class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'


# After changing the model, we must make migrations. The command will create a migrations file. It's the instructions for django to create the model in the database. We don't need to worry about this file too much. 
# The command -
#   docker-compose run app sh -c "python manage.py makemigrations core" 
# specify the appname at the end - core

