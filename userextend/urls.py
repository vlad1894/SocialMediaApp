from django.urls import path
from userextend import views




urlpatterns = [
    path('create_user/', views.UserExtendCreateView.as_view(), name='create_user'),
]
