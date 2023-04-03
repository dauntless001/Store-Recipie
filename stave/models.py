from django.db import models
from django.db.models.lookups import Q
from storerecipe.utils.models import TimeBasedModel
from storerecipe.utils import choices, strings
# Create your models here.

class StaveManager(models.Manager):
    def published(self):
        return self.get_queryset().filter(status=choices.Status.Published)


class Stave(TimeBasedModel):
    user = models.ForeignKey('base.User', on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    status = models.CharField(max_length=100, choices=choices.Status.choices, 
                              default=choices.Status.Draft)
    likes = models.ManyToManyField('base.User', null=True, related_name='stave_likes')
    slug = models.SlugField(default=strings.generate_random_url)

    objects = StaveManager()

    def __str__(self):
        return f'stave - {self.slug}'