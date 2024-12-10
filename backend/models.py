from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta
import uuid

class User(AbstractUser):
    study_duration = models.DurationField(default=timedelta)
    currently_studying = models.BooleanField(default=False)
    last_started_studying = models.DateTimeField(blank=True, null=True)

class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256, blank=True, default="")
    members = models.ManyToManyField(User)
