from django.shortcuts import render
from django.http import JsonResponse
from bookmark.models import Bookmark
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
# Create your views here.


class AddRemoveBookmark(View):
    def get(self, request, *args, **kwargs):
        response = {
            'status' : False
        }
        slug = self.kwargs['stave_slug']
        try:
            Bookmark.objects.get(user=self.request.user, stave__slug=slug).delete()
        except Bookmark.DoesNotExist:
            Bookmark.objects.create(user=self.request.user, stave__slug=slug)
            response['following'] = True
        return JsonResponse(response, safe=False)

