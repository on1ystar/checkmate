from django.urls import path
from . import views


app_name = 'attendance'

urlpatterns =[
    path('classroom_list/<int:pk>', views.classroom_list, name= 'classroom_list'),
    path('classroom_detail/<uuid:uuid>', views.classroom_detail, name= 'classroom_detail'),
]
