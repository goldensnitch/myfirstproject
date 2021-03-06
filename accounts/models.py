from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.
class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    display_name = models.CharField(max_length=30, blank=True)


