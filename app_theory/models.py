from django.db import models
import uuid


class Theory(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(unique=True, max_length=75)
    content = models.TextField()
