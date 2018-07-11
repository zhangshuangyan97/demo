from django import forms
from user.models import User
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname","password","icon","age","sex"]
    password2 = forms.CharField(max_length=128)
    