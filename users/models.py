# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from polls.models import Team

class CustomUser(AbstractUser):
    # First/last name is not a global-friendly pattern
    name = models.CharField(blank=True, max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.email