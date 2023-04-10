from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import ThoughtForm
from .models import Thought, Profile
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.urls import reverse

@login_required
def dashboard(request):
    form = ThoughtForm(request.POST or None)
    profile = Profile.objects.filter(user=request.user).get()
    if request.method == "POST":
        if form.is_valid():
            thoughts = form.save(commit=False)
            thoughts.profile = profile
            thoughts.save()
            return redirect("socialapp:dashboard")
    profiles = list(profile.follows.all())
    profiles.append(profile)
    followed_thoughts = Thought.objects.filter(
        profile__in=profiles
    ).order_by("-created_at")

    return render(request, 'socialapp/dashboard.html', {"form": form, "thoughts": list(followed_thoughts), "profile": profile})



@login_required
def delete_thought(request, thought_id):
    thought = get_object_or_404(Thought, pk=thought_id)
    profile = get_object_or_404(Profile, user=request.user)
    if thought.profile != profile:
        raise Exception("Not mine!!!")
    if request.method == "POST":
        thought.delete()
        return redirect("socialapp:dashboard")
    return redirect("socialapp:dashboard")

@login_required
def edit_thought(request, thought_id):
    thought = get_object_or_404(Thought, pk=thought_id)
    profile = get_object_or_404(Profile, user=request.user)
    if thought.profile != profile:
        raise Exception("Not mine!!!")
    if request.method == "POST":
        form = ThoughtForm(request.POST, instance = thought)
        if form.is_valid():
            thoughts = form.save(commit=True)
            thoughts.profile = profile
            thoughts.save()
            return redirect("socialapp:dashboard")
    else:
        print(f"thought: {thought.unique_error_message} not valid")
        form = ThoughtForm(instance=thought)
    return render(request, "socialapp/edit_thought.html", {"form": form})

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

# def profile(request, pk):
#     if not hasattr(request.user, 'profile'):
#         missing_profile = Profile(user=request.user)
#         missing_profile.save()

#     profile = Profile.objects.get(pk=pk)

#     if request.method == "POST":
        
#         if 'photo' in request.FILES:
#             photo = request.FILES['photo']
#             fs = FileSystemStorage(location=settings.MEDIA_ROOT)
#             filename = fs.save(photo.name, photo)
#             profile.photo = filename
#             profile.save()
#             return redirect('socialapp:profile', pk=pk)

#         current_user_profile = request.user.profile
#         data = request.POST
#         action = data.get("follow")
#         if action == "follow":
#             current_user_profile.follows.add(profile)
#         elif action == "unfollow":
#             current_user_profile.follows.remove(profile)
#         current_user_profile.save()

#     return render(request, 'socialapp/profile.html', {'profile': profile})