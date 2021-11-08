from django import forms
from django.contrib import messages



class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Şifre",widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    email = forms.EmailField(label="Eposta")
    username = forms.CharField(max_length=50,min_length=4,label="Kullanıcı Adı")
    password = forms.CharField(max_length=20,min_length=8,label="Şifre",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20,min_length=8,label="Şifre Tekrar",widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and (password != confirm):
            raise forms.ValidationError("Girmiş olduğunuz şifreler uyuşmuyor!")

        values = {
            "username" : username,
            "password" : password,
            "email"    : email,

        }
        return values