from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import ThoughtForm
from .models import Thought, Profile
from django.http import HttpResponseRedirect

def dashboard(request):
    if request.method == "POST":
        form = ThoughtForm(request.POST or None)
        if form.is_valid():
            thoughts = form.save(commit=False)
            thoughts.user = request.user
            thoughts.save()
            return redirect("socialapp:dashboard")
        
    # followed_thought = Thought.objects.filter(
    #     user_profile_in=request.user.profile.follows.all()
    # ).order_by("-created_at")

    # return render(request, 'socialapp/dashboard.html', {"form": form, "thoughts": followed_thought})


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


def like_view(request, pk):
    post = get_object_or_404(Thought, id=request.POST.get('user'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('dashboard', args=[str(pk)]))


def dislike_view(request, pk):
    post = get_object_or_404(Thought, id=request.POST.get('user'))
    post.dislikes.add(request.user)
    return HttpResponseRedirect(reverse('dashboard', args=[str(pk)]))




# Create your views here.
