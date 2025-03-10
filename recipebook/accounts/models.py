from django.db import models
from django.contrib.auth.models import User


class Profile(User):
    name = models.CharField(max_length=50)
    short_bio = models.TextField()