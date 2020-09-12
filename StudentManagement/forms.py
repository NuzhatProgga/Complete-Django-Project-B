from django import forms
from .models import Student

class StudentInsertForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'contact_no')
