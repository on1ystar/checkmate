from django.urls import path
from . import views


app_name = 'attendance'

urlpatterns =[
    path('classroom/new', views.classroom_new, name='classroom_new'),
    path('classroom_list', views.classroom_list, name= 'classroom_list'),
    path('classroom_detail/<uuid:uuid>/<str:is_checker>', views.classroom_detail, name= 'classroom_detail'),
    path('classroom/<uuid:uuid>/edit', views.classroom_edit, name= 'classroom_edit'),
    path('classroom/<uuid:uuid>/delete', views.classroom_delete, name= 'classroom_delete'),
    path('camera_setting', views.camera_setting, name ='camera_setting'),
    path('classroom_enroll', views.classroom_enroll, name='classroom_enroll'),
    path('classroom_enroll_list/<uuid:uuid>', views.classroom_enroll_list, name='classroom_enroll_list'),

]
