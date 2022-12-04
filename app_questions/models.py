from django.db import models
import uuid

# Create your models here.


class Questions(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    question = models.CharField(max_length=255, blank=False, null=False)
    list_answer = models.CharField(max_length=255, blank=False, null=False)
    correct_answer = models.CharField(max_length=100, blank=False, null=False)


class SetOfQuestion(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    list_question = models.CharField(max_length=2500)
