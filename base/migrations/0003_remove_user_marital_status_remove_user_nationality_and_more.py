# Generated by Django 4.1.7 on 2023-04-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_user_display_name_user_image_user_marital_status_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="marital_status",
        ),
        migrations.RemoveField(
            model_name="user",
            name="nationality",
        ),
        migrations.RemoveField(
            model_name="user",
            name="sex",
        ),
        migrations.AddField(
            model_name="user",
            name="bio",
            field=models.TextField(default="Something amazing about me"),
        ),
    ]