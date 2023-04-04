from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import ThoughtForm
from .models import Thought, Profile
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

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


    # form=ThoughtForm()
    # return render(request, 'socialapp/dashboard.html', {"form": form})

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
        form = ThoughtForm(request.POST or None)
        if form.is_valid():
            thoughts = form.save(commit=False)
            thoughts.profile = profile
            thoughts.save()
            return redirect("socialapp:dashboard")
    return redirect("socialapp:dashboard")

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

class EditPost(UpdateView):
    model = Thought
    fields = ['body']
    template_name = "socialapp/post_edit.html"

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy("dashbaord", kwargs={'pk': pk})
    
class DeletePost(DeleteView):
    model = Thought
    template_name = "socialapp/post_delete.html"
    success_url = reverse_lazy('dashboard')





# def like_view(request, pk):
#     post = get_object_or_404(Thought, id=request.POST.get('user'))
#     post.likes.add(request.user)
#     return HttpResponseRedirect(reverse('dashboard', args=[str(pk)]))


# def dislike_view(request, pk):
#     post = get_object_or_404(Thought, id=request.POST.get('user'))
#     post.dislikes.add(request.user)
#     return HttpResponseRedirect(reverse('dashboard', args=[str(pk)]))


# def like_item(request):
#     user=request.user
#     item_id = request.POST.get('item_id')
#     item = Thought.objects.get(id=item_id)
#     likes = Like.objects.filter(user=user, item=item)
#     if not likes.exists():
#         Like.objects.create(user=user, item=item)


# Create your views here.