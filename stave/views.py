from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import View, ListView
from stave.models import Stave
from stave.forms import StaveForm
# Create your views here.

class UserStaves(LoginRequiredMixin, ListView):
    context_object_name = 'staves'
    
    def get_queryset(self):
        return self.request.user.get_staves()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateStave(LoginRequiredMixin, View):
    def post(self, request):
        form = StaveForm(request.POST, request.FILES)
        if form.is_valid():
            stave = form.save(commit=False)
            stave.user = self.request.user
            stave.save()
            messages.success(self.request, 'Stave Uploaded')
            return redirect('base:home')


class DeleteStaveView(LoginRequiredMixin,UserPassesTestMixin, View):
    def get_stave(self, slug):
        return Stave.objects.get(slug=slug)

    def get(self, request, *args, **kwargs):
        stave = self.get_stave()
        if stave:
            stave.delete()
            messages.success(self.request, 'Stave Deleted')
        return redirect('base:home')

    def test_func(self):
        if self.reuqest.user == self.get_stave().user:
            return True
        return False
    
    def handle_no_permission(self):
        return redirect('base:home')