from django.urls import path
from . import views


app_name = 'attendance'

urlpatterns =[
    path('classroom/new', views.classroom_new, name='classroom_new'),
    path('classroom_list/<int:pk>', views.classroom_list, name= 'classroom_list'),
    path('classroom_detail/<uuid:uuid>/<str:is_checker>', views.classroom_detail, name= 'classroom_detail'),
    path('classroom/<uuid:uuid>/edit', views.classroom_edit, name= 'classroom_edit'),
    path('classroom/<uuid:uuid>/delete', views.classroom_delete, name= 'classroom_delete'),
]
