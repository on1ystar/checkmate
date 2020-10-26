from django import forms
from .models import Classroom, Role, ClassroomEnroll


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ('name', 'desc', 'timer', 'personnel')

        widgets = {
            'desc': forms.Textarea(attrs={'placeholder': 'classroom 소개'}),
            'timer': forms.TextInput(attrs={'placeholder': '입력 양식 00:00(분:초)'})
            }


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'


class ClassroomEnrollForm(forms.ModelForm):
    class Meta:
        model = ClassroomEnroll
        fields = ('classroom', 'msg')
