from django import forms
from django.contrib.auth.models import User
from attendance.models import Profile, UserPhoto

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ['email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ['nickname', 'school', 'student_id']

class UserPhotoForm(forms.ModelForm):
    class Meta:
        model = UserPhoto
        fields= ['photo']

UserPhotoFormSet = forms.inlineformset_factory(Profile, UserPhoto, form=UserPhotoForm, extra=1)


# class ProfileForm(forms.Form):
#     user = forms.ModelChoiceField(queryset=User.objects.all()) 
#     nickname = forms.CharField(required=False, initial='guest', widget=forms.Textarea(attrs={'placeholder': '닉네임'}))
#     school = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '소속 학교or기관'}))
#     student_id = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': '학번or학년/반(없으면 빈칸'}))
#     photo = forms.ModelMultipleChoiceField(queryset=UserPhoto.objects.all())

