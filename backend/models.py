from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    members = models.ManyToManyField(User)
