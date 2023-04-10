from django.shortcuts import render



import datetime
import uuid

from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.db import IntegrityError
from django.db import IntegrityError
from .forms import UserExtendForm
from .models import UserToken

from userextend.forms import UserExtendForm



class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    form_class = UserExtendForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        try:
            user = form.save(commit=True)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            UserToken.objects.create(user=user)
            login(self.request, user)
        except IntegrityError:
            form.add_error('username', 'A user with that username already exists.')
            return self.form_invalid(form)
        
        return super().form_valid(form)
        








    




# Create your views here.
