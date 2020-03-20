from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib.auth.models import User

from .models import CustomUser

def profile(request):
    current_user = CustomUser.objects.get(user__username=request.user)
    return render(request,'registration/profile.html',{'current_user':current_user})