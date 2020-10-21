from django import forms
from django.contrib.auth import get_user_model
from attendance.models import Profile, UserPhoto

User = get_user_model()

class UserForm(forms.ModelForm):
    verify_password = forms.CharField(label = '비밀번호 확인', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields= ['email', 'password', 'verify_password']
        labels = {
            'email' : '이메일',
            'password': '비밀번호'
        }
        help_texts = {
               'password': ' 이메일과 너무 비슷하면 안됩니다.<br>\
                         영문, 숫자 조합 8자 이상',
           }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(attrs={
                'class': 'form-control'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            if User.objects.get(username=email):
                raise forms.ValidationError('이미 가입된 이메일입니다.')
        except:
            pass 
        return email

    def clean_verify_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('verify_password')
        if password1 != password2:
            raise forms.ValidationError('비밀번호가 일지하지 않습니다.')
        return password2    

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ['email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ['nickname', 'school', 'student_id']

        widgets = {
            'school': forms.TextInput(attrs={'placeholder': 'ex) OO대학교 00학과 or OO학원'}),
            'student_id': forms.TextInput(attrs={'placeholder': 'ex) 학번 or O학년 O반'}),
        }

class UserPhotoForm(forms.ModelForm):
    class Meta:
        model = UserPhoto
        fields= ['photo', ]

UserPhotoFormSet = forms.inlineformset_factory(Profile, UserPhoto, form=UserPhotoForm, extra=1)
UserPhotoFormSet2 = forms.inlineformset_factory(Profile, UserPhoto, form=UserPhotoForm, extra=2)

# class ProfileForm(forms.Form):
#     user = forms.ModelChoiceField(queryset=User.objects.all()) 
#     nickname = forms.CharField(required=False, initial='guest', widget=forms.Textarea(attrs={'placeholder': '닉네임'}))
#     school = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '소속 학교or기관'}))
#     student_id = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': '학번or학년/반(없으면 빈칸'}))
#     photo = forms.ModelMultipleChoiceField(queryset=UserPhoto.objects.all())

