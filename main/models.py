import random
import string
from django.db import models

class TransmittedURL(models.Model):
    long_url = models.URLField(unique=True)
    short_id = models.CharField(max_length=7, unique=True, blank=True)

    def __str__(self):
        return self.short_id, self.long_url

    class Meta:
        verbose_name = "URL"
        verbose_name_plural = "URLs"
