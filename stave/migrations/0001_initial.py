# Generated by Django 4.1.7 on 2023-04-03 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import storerecipe.utils.strings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Stave",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("content", models.TextField(max_length=280)),
                (
                    "status",
                    models.CharField(
                        choices=[("draft", "Draft"), ("published", "Published")],
                        default="draft",
                        max_length=100,
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        default=storerecipe.utils.strings.generate_random_url
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        null=True,
                        related_name="stave_likes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
