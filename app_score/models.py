from django.db import models
import uuid


class Score(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_id = models.CharField(max_length=15, null=False, blank=False)
    index_set_question = models.SmallIntegerField()
    score = models.SmallIntegerField(default=-1)
    index_question = models.SmallIntegerField(default=0)
