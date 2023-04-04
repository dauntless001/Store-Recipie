from django.db import models
from storerecipe.utils.models import TimeBasedModel
# Create your models here.
class Follow(TimeBasedModel):
    followee = models.ForeignKey('base.User', on_delete=models.CASCADE, related_name='followee')
    follower = models.ForeignKey('base.User', on_delete=models.CASCADE, related_name='follower')

    def __str__(self):
        return f'{self.follower} followed {self.followee}'