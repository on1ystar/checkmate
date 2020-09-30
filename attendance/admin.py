from django.contrib import admin
from .models import Profile, Attendance, Role, Classroom, UserPhoto
from django.conf import settings
from django.contrib.auth.models import User


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'school', 'student_id']
    list_display_links = ['user_id']

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'name', 'desc', 'timer', 'personnel', 'created_at']
    list_display_links = ['uuid', 'name']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'classroom', 'is_attendance', 'time_out', 'checked_at']

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['user', 'classroom', 'is_checker']

@admin.register(UserPhoto)
class UserPhotoAdmin(admin.ModelAdmin):
    pass
