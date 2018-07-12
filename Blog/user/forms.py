from django import forms
from user.models import User
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname","password","icon","age","sex"]
    password2 = forms.CharField(max_length=128)

    def clean_password2(self):
        cleande_data = super().clean()
        if cleande_data["password"] != cleande_data["password2"]:
            raise forms.ValidationError('两次密码不一致 ')
