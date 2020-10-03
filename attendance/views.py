from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from .models import Profile, UserPhoto, Classroom, Role
from .forms import ClassroomForm, RoleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def classroom_new(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST, request.FILES)
        form_role = RoleForm()
        if form.is_valid():
            classroom = form.save()
            role = form_role.save(commit=False)
            role.user = request.user.profile
            role.classroom = classroom
            role.is_checker = True
            role.save()
            return redirect(classroom)
    else:
        form = ClassroomForm()
        
    return render(request, 'attendance/classroom_form.html', {
        'form': form,
    })

@login_required
def classroom_edit(request, uuid):
    classroom = get_object_or_404(Classroom, uuid = uuid)

    if request.method == 'POST':
        form = ClassroomForm(request.POST, request.FILES, instance=classroom)
        if form.is_valid():
            classroom = form.save()
            return redirect(classroom)
    else:
        form = ClassroomForm(instance=classroom)
        
    return render(request, 'attendance/classroom_form.html', {
        'form': form,
    })

@login_required
def classroom_list(request, pk):
    role_list = Role.objects.select_related('user').select_related('classroom').filter(user=pk)
    return render(request, 'attendance/classroom_list.html',{
        'role_list': role_list
    })

@login_required
def classroom_detail(request, uuid, is_checker):
    classroom = get_object_or_404(Classroom, uuid= uuid)
    return render(request, 'attendance/classroom_detail.html',{
        'classroom': classroom,
        'is_checker': is_checker,
    })

# 로그인 user가 checker일 경우 
@login_required
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