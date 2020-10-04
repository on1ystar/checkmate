from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from .forms import LoginForm
from django.contrib import messages
import logging
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                username = User.objects.get(email=email)
                user = authenticate(username = username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, '로그인 성공.')
                    return redirect('root')
                else:
                    messages.error(request, 'password를 잘못 입력하셨습니다.')

            except ObjectDoesNotExist:
                logging.error("User does not exist")
                messages.error(request, 'email을 잘못 입력하셨습니다.')
    
    form = LoginForm()
    return render(request, 'accounts/login_form.html',{
        'form': form,
    })
    
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

'''
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
'''