from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.contrib import messages
import logging
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from attendance.models import Profile, UserPhoto
from .forms import LoginForm, ProfileForm, UserPhotoFormSet


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
def logout(request):
    pass

def sign_up(request):
    pass


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def profile_edit(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        photo_formset = UserPhotoFormSet(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid() and photo_formset.is_valid():
            profile_form.save()
            photo_formset.save()
            messages.success(request, 'profile을 수정했습니다.')
            return redirect('accounts:profile')
        
    profile_form = ProfileForm(instance=profile)
    photo_formset = UserPhotoFormSet(instance=profile)

    return render(request, 'accounts/profile_form.html', {
        'profile_form': profile_form,
        'photo_formset': photo_formset,
    })
