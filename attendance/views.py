from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from .models import Profile, UserPhoto, Classroom, Role

# Create your views here.
def classroom_list(request, pk):
    q = request.GET.get('q', '')

    role_list = Role.objects.select_related('user').select_related('classroom').filter(user=pk)
    return render(request, 'attendance/classroom_list.html',{
        'role_list': role_list
    })


def classroom_detail(request, uuid):
    classroom = get_object_or_404(Classroom, uuid= uuid)
    return render(request, 'attendance/classroom_detail.html',{
        'classroom': classroom,
    })

# 로그인 user가 checker일 경우 
def mate_list(request, pk):  # pk = user의 pk 
    pass


'''
model._meta.model_name
model._meta.app_lable

FBV or CBV
get object
get templete
dispatch -> render

로그인
회원가입
마이페이지
클래스 생성
클래스 목록
클래스 디테일
출석관리
'''