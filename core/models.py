from django.contrib.auth.models import User
from django.db import models


class CoffeeMatch(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    recipient = models.ForeignKey(User, related_name='recipient')
    candidate = models.ForeignKey(User, related_name='candidate')
    accepted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Coffee Matches"
