from django.urls import path
from .views import dashboard, list_of_profiles, profile, thought_edit




app_name = 'thoughts',
app_name = 'socialapp'



urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('list_of_profiles/', list_of_profiles, name='list_of_profiles'),
    path('profile/<int:pk>', profile, name='profile'), 
    # path('like/<int:pk>/', like_item, name='like_item'),
    path('thought/int:id>/', thought_edit, name='thought_edit'),
    
    

]




