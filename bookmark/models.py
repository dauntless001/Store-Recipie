from django.db import models
from storerecipe.utils.models import TimeBasedModel
# Create your models here.
class Bookmark(TimeBasedModel):
    user = models.ForeignKey('base.User', on_delete=models.CASCADE, 
                             related_name='user_bookmark')
    stave = models.ForeignKey('stave.Stave', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - Bookmark {self.stave.slug}'