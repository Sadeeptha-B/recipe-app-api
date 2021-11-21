from django.db import models

# The Base user manager provides the helper functions for creating a user/super
# user.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,\
     PermissionsMixin


# Extend base user manager and override functions
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # encrypt and set password
        user.set_password(password)
        # self._db is good practice (support multiple db)
        user.save(using=self._db)
        return user

    # Create superuser is used by the django cli when creating new
    # users using the cmd. No need to worry about extra fields since used
    # primarily with the cmd.
    def create_superuser(self, email, password):
        """Creates and savea a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True

        # User must be saved again after the change
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'


# After changing the model, we must make migrations. The command will create a
# migrations file. It's the instructions for django to create the model in the
#  database. We don't need to worry about this file too much.
# The command -
#   docker-compose run app sh -c "python manage.py makemigrations core"
# specify the appname at the end - core
