from django.shortcuts import render



import datetime
import uuid

from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView



from userextend.forms import UserExtendForm



class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserExtendForm
    # success_url = reverse_lazy('dashboard')


    # if form valid:
    # bla bla
    # redirect('template')

    # @login_required
    # def profile(request):
    # if request.method == 'POST':
    #     u_form = UserUpdateForm(request.POST, instance=request.user)
    #     p_form = ProfileUpdateForm(request.POST,
    #                                request.FILES,
    #                                instance=request.user.profile)
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, f'Your account has been updated!')
    #         # This is to prevent the user from resubmitting the form
    #         return redirect('profile')






    




# Create your views here.
