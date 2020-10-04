from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, blank=True , default='guest', verbose_name='닉네임')
    school = models.CharField(max_length=20, verbose_name='소속 학교or기관')
    student_id = models.CharField(max_length=20, blank=True, verbose_name='학번or학년/반')
    classroom_set = models.ManyToManyField('Classroom', blank=True, through='Role')

    def __str__(self):
        return f'{self.user}'

class UserPhoto(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='checkmate/user', blank=True, verbose_name='얼굴 정면 사진')  # photo.url 로 접근해야 이미지 보임


class Classroom(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, verbose_name='클래스룸 명')
    desc = models.TextField(blank=True, verbose_name='소개')
    timer = models.DurationField(default=300, blank=False, null=False, verbose_name='자리비움 시간')
    personnel = models.PositiveIntegerField(default=10, verbose_name='제한인원')
    created_at = models.DateTimeField(auto_now_add=True)
    # profile_set -> related name
    # add, remove 함수로 유저 추가, 삭제

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('attendance:classroom_detail', args=[self.uuid, True])


    class Meta:
        ordering = ['name', 'uuid']    
    
class Role(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    is_checker = models.BooleanField(default=False, verbose_name='체커')

    def __str__(self):
        return f'{self.is_checker}' 

    class Meta:
        ordering = ['classroom', 'is_checker', '-user' ]

class Attendance(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    is_attendance = models.BooleanField(default=False, verbose_name='출석 여부')
    time_out = models.DurationField(default=0, blank=True, verbose_name='자리비운 시간')
    checked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['classroom', 'user']