from django.urls import path
from .views import dashboard, list_of_profiles, profile, like_view, dislike_view 




app_name = 'thoughts',
app_name = 'socialapp'



urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('list_of_profiles/', list_of_profiles, name='list_of_profiles'),
    path('profile/<int:pk>', profile, name='profile'), 
    path('like/<int:pk>/', like_view, name='like_post'),
    path('like/<int:pk>/', dislike_view, name='dislike_post')
    

]




