from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import Student

class RegisterForm(UserCreationForm):
    username = forms.TextInput(attrs={'autocomplete': "off"})
    email = forms.EmailField
    first_name = forms.TextInput
    last_name = forms.TextInput

    GRADE_CHOICES = (
        ("FR", "Freshman"),
        ("SO", "Sophmore"),
        ("JR", "Junior"),
        ("SR", "Senior")
    )

    grade = forms.ChoiceField(choices = GRADE_CHOICES)
    
    
    class Meta:
        model = Student
        fields = ["username","first_name", "last_name", "email", "password1", "password2", "grade"]

class UpdateUserForm(forms.ModelForm):
    username = forms.TextInput(attrs={'autocomplete': "off"})
    first_name = forms.TextInput
    last_name = forms.TextInput
    email = forms.EmailField

    GRADE_CHOICES = (
        ("FR", "Freshman"),
        ("SO", "Sophmore"),
        ("JR", "Junior"),
        ("SR", "Senior")
    )

    grade = forms.ChoiceField(choices= GRADE_CHOICES)

    class Meta:
        model = Student
        fields = ["username", "first_name", "last_name", "email", "grade"]
