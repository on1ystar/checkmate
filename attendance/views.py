from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from .models import Profile, UserPhoto, Classroom, Role, ClassroomEnroll
from .forms import ClassroomForm, RoleForm, ClassroomEnrollForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json

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
            messages.success(request, '새로운 classroom을 생성했습니다.')
            return redirect(classroom)
    else:
        form = ClassroomForm()
        
    return render(request, 'attendance/classroom_form.html', {
        'form': form,
        'classroom': None,
    })

@login_required
def classroom_edit(request, uuid):
    classroom = get_object_or_404(Classroom, uuid = uuid)

    if request.method == 'POST':
        form = ClassroomForm(request.POST, request.FILES, instance=classroom)
        if form.is_valid():
            classroom = form.save()
            messages.success(request, 'classroom을 수정했습니다.')
            return redirect(classroom)
    else:
        form = ClassroomForm(instance=classroom)
        
    return render(request, 'attendance/classroom_form.html', {
        'form': form,
        'classroom': classroom,
    })


@login_required
def classroom_delete(request, uuid):
    classroom = get_object_or_404(Classroom, uuid = uuid)
    if request.method == 'POST':
        classroom.delete()
        messages.success(request, 'classroom을 삭제했습니다.')
        return redirect('attendance:classroom_list')
    return render(request, 'attendance/classroom_confirm_delete.html',{
        'classroom': classroom,
    })

@login_required
def classroom_list(request):
    role_list = Role.objects.select_related('user').select_related('classroom').filter(user=request.user.pk)
    return render(request, 'attendance/classroom_list.html',{
        'role_list': role_list
    })

@login_required
def classroom_detail(request, uuid, is_checker):
    classroom = get_object_or_404(Classroom, uuid= uuid)
    checker = Role.objects.all().filter(classroom=classroom).get(is_checker=True).user
    role_list = classroom.role_set.all().exclude(user=checker)
    return render(request, 'attendance/classroom_detail.html',{
        'classroom': classroom,
        'is_checker': is_checker,
        'checker': checker,
        'role_list': role_list,
    })

def camera_setting(request):
    return render(request, 'attendance/camera_setting.html',{

    })

@login_required
def classroom_enroll(request):
    classroom_list = Classroom.objects.all()
    if request.method == 'GET':
        q = request.GET.get('q', '')    
        if q:
            qs = classroom_list.filter(name__icontains=q).exclude(profile=request.user.pk)
        else:
            qs = None
    elif request.method == 'POST':
        classroom_enroll_form = ClassroomEnrollForm(request.POST)
        if classroom_enroll_form.is_valid():
            classroom_enroll = classroom_enroll_form.save(commit = False)
            classroom_enroll.user = request.user.profile
            classroom_enroll.save()
            messages.success(request, 'classroom을 신청했습니다.')
            return render(request, 'attendance/classroom_enroll.html',{
             })
        else:
            print(classroom_enroll_form.errors)

    return render(request, 'attendance/classroom_enroll.html',{
        'classroom_list': qs,
    })

@login_required
def classroom_enroll_list(request, uuid):
    classroom_enroll_list = ClassroomEnroll.objects.all().filter(classroom=uuid)

    return render(request, 'attendance/classroom_enroll_list.html', {
        'classroom_enroll_list': classroom_enroll_list,
        'classroom_uuid': uuid,
    })

@login_required
def classroom_enroll_ajax(request, uuid):
    if request.method == 'POST':
        for user, check in json.loads(request.body.decode("utf-8")).items():
            user = get_object_or_404(Profile, user=get_object_or_404(User, username=user))
            classroom = get_object_or_404(Classroom, uuid=uuid)
            if check == 'True':
                form_role = RoleForm()
                role = form_role.save(commit=False)
                role.user = user
                role.classroom = classroom
                role.is_checker = False
                role.save()
            ClassroomEnroll.objects.all().filter(user=user, classroom=classroom).delete()

        classroom_enroll_list = ClassroomEnroll.objects.all().filter(classroom=uuid)
        return render(request, 'attendance/classroom_enroll_list.html', {
        'classroom_enroll_list': classroom_enroll_list,
        'classroom_uuid': uuid,
    })

'''
얼굴인식 설정
출석관리
'''