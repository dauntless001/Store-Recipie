from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from base.forms import UserForm
from django.contrib import messages
from django.views.generic import View
from follow.models import Follow
from stave.models import Stave
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
# Create your views here.

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = ''

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        # Pass extra context here
        return context
    
    def post(self, request, **kwargs):
        form = UserForm(request.POST, request.FILES, instance=self.request.user)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Profile updated successfully')
            return redirect('base:home')
        else:
            messages.error(self.request, 'Error updating profile')
        return redirect('base:profile')


class IndexView(LoginRequiredMixin,View):
    template_name = 'home.html'
    def get_following_staves(self):
        people_followed = Follow.objects.filter(follower=self.request.user).values_list('username', flat=True)
        staves = Stave.objects.filter(
            Q(user__username__in=people_followed) | 
            Q(user__user=self.request.user)
            ).published().ordered_by('-created_at')
        return staves

    def get(self, request, *args, **kwargs):
        context = {
            'posts' : self.get_following_staves()
        }
        return render(request, self.template_name, context)
        