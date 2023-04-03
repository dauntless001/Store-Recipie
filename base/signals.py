from django.db.models.signals import post_save
from django.dispatch import receiver
from base.models import User


def save_user(sender, instance, created, **kwargs):
    if created:
        pass


post_save.connect(save_user,sender=User)