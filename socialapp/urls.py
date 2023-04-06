from django.urls import path
from .views import dashboard, list_of_profiles, profile, delete_thought, edit_thought





app_name = 'socialapp'




urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('list_of_profiles/', list_of_profiles, name='list_of_profiles'),
    path('profile/<int:pk>', profile, name='profile'),
    path('thought/<int:thought_id>/delete', delete_thought, name='delete_thought'), 
    path('thought/<int:thought_id>/edit_thought.html', edit_thought, name='edit_thought'),
]




