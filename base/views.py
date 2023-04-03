from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from base.forms import UserForm
from django.contrib import messages
# Create your views here.

class ProfileView(TemplateView):
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

        