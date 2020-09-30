from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from .models import Profile, UserPhoto, Classroom, Role

# Create your views here.
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(Profile, user_id=pk)
    photo = get_list_or_404(UserPhoto, user_id=pk)
    return render(request, 'attendance/user_detail.html',{
        'user': user,
        'profile': profile,
        'photo': photo,
    })

def classroom_list(request, pk):
    classroom_role = []
    q = request.GET.get('q', '')

    role = get_list_or_404(Role, user_id = pk)
    for r in role:
        classroom_role.append([Classroom.objects.get(uuid=r.classroom_id), r])
    return render(request, 'attendance/classroom_list.html',{
        'classroom_role': classroom_role,
    })

def classroom_detail(request, uuid):
    classroom = get_object_or_404(Classroom, uuid= uuid)
    return render(request, 'attendance/classroom_detail.html',{
        'classroom': classroom,
    })

# 로그인 user가 checker일 경우 
def mate_list(request, pk):  # pk = user의 pk 
    pass


def login(request):
    return render(request, 'attendance/login.html')

def sign_in(request):
    return render(request, 'attendance/sign_in.html')

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