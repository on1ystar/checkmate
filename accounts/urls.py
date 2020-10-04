from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('profile/', views.profile, name='profile')
    # path('profile/edit/', views.profile_edit, name='profile_edit')
]