from django import forms
from .models import Classroom, Role


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'