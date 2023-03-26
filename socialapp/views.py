from django.shortcuts import render, redirect
from .forms import ThoughtForm
from .models import Thought, Profile

def dashboard(request):
    if request.method == "POST":
        form = ThoughtForm(request.POST or None)
        if form.is_valid():
            thoughts = form.save(commit=False)
            thoughts.user = request.user
            thoughts.save()
            return redirect("socialapp:dashboard")
    form=ThoughtForm()
    return render(request, 'socialapp/dashboard.html', {"form": form})



def list_of_profiles(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request,'socialapp/list_of_profiles.html', {'profiles': profiles})

def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()


    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, 'socialapp/profile.html', {'profile': profile})

# Create your views here.
