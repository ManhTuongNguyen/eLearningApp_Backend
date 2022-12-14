# Generated by Django 4.1 on 2022-10-16 10:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Questions",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("question", models.CharField(max_length=255)),
                ("list_answer", models.CharField(max_length=255)),
                ("correct_answer", models.CharField(max_length=100)),
            ],
        ),
    ]
