from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        DEVELOPER = 'developer', 'Developer'
        MANAGER = 'manager', 'Manager'
        VIEWER = 'viewer', 'Viewier'

    role = models.CharField(
        max_length=16,
        choices=Role.choices,
        default=Role.DEVELOPER,
    )

    def __str__(self):
        return f'(self.username) ({self.role})'
