# Generated by Django 4.1.7 on 2023-04-03 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stave", "0003_alter_stave_likes_alter_stave_reply"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stave",
            name="reply",
            field=models.ManyToManyField(blank=True, to="stave.stave"),
        ),
    ]
