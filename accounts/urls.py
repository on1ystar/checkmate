from django.contrib.auth.views import  LogoutView
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('logout/', LogoutView.as_view( ), name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]