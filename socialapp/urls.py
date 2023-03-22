from django.urls import path
from .views import dashboard, list_of_profiles

app_name = 'thoughts'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('list_of_profiles/', list_of_profiles, name='list_of_profiles')
]


