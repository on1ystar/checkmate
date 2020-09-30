from django.urls import path
from . import views


app_name = 'attendance'

urlpatterns =[
    path('login/', views.login),
    path('sign_in/', views.sign_in),
    path('user_detail/<int:pk>', views.user_detail),
    path('classroom_list/<int:pk>', views.classroom_list),
    path('classroom_detail/<uuid:uuid>', views.classroom_detail),
]
