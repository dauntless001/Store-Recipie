from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from storerecipe.utils import choices, media
# Create your models here.

class User(AbstractUser):
    image = models.ImageField(
            upload_to=media.get_image_upload_path, null=True, blank=True
        )
    bio = models.TextField(default='Something amazing about me')
    display_name = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return f'{self.last_name} {self.first_name}' or self.username
    
    def image_url(self):
        if self.image:
                return getattr(self.image, 'url', None)
        return f"{settings.STATIC_URL}img/avatars/user-avatar.png" 
    
    def save(self, request, *args, **kwargs):
        if not self.display_name:
             self.display_name = self.username
        return super(self, User).save(*args, **kwargs)
        

