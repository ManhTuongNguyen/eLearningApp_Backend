from django.db import models

# Create your models here.


class MostCommonWord(models.Model):
    word = models.CharField(max_length=20, unique=True, blank=False, null=False)

    class Meta:
        db_table = "tb_words"
