from django.http import JsonResponse
from django.shortcuts import render
from follow.models import Follow
from base.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
# Create your views here.
class FollowAUser(LoginRequiredMixin,View):
    def get_followee(self, **kwargs):
        return User.objects.get(username=self.kwargs['username'])

    def get(self, **kwargs):
        response = {
            'following' : False,
        }
        try:
            Follow.objects.get(follower=self.request.user, followee=self.get_followee()).delete()
        except Follow.DoesNotExist:
            Follow.objects.create(follower=self.request.user, followee=self.get_followee())
            response['following'] = True
        return JsonResponse(response, safe=False)
        