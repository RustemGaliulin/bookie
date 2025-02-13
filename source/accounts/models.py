from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # favorite_books = models.ManyToManyField("Book", related_name="favorited_by", blank=True)
    dummy_field = models.CharField()

