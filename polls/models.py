from datetime import datetime
from django.db import models
from django.utils.timezone import now
from .tasks import delete_expired_paste
import string
import random


# Create your models here.
class Paste(models.Model):
    content = models.TextField()
    slug = models.CharField(max_length=10, unique=True, blank=True)
    is_public = models.BooleanField(default=False)
    expires_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_slug(self):
        length = 8
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug()
            while Paste.objects.filter(slug=self.slug).exists():
                self.slug = self.generate_slug()
        super().save(*args, **kwargs)

        if self.expires_at:
            delay = (self.expires_at - now()).total_seconds()
            delay = max(delay, 0)
            delete_expired_paste.apply_async((self.id,), countdown=delay)

    def __str__(self):
        return self.slug


