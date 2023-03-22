from django.shortcuts import render
from .models import Profile

def dashboard(request):
    return render(request, 'index.html')


def list_of_profiles(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request,'socialapp/list_of_profiles.html', {'profiles': profiles})

# Create your views here.
