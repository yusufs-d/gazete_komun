from article.views import index
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        if User.objects.filter(username=username).exists():
            messages.info(request,"Bu kullanıcı adı daha önceden alınmış!")
            return redirect("/user/register/")
        newUser = User(username = username,email = email)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request, 'Başarıyla Kayıt Olundu!')
        return redirect(index)
    context = {
        "form" : form
    }
    return render(request,"register.html",context)

def loginusr(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        if user == None:
            messages.info(request,"Kullanıcı Adı Ya Da Parola Hatalı!")
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla Giriş Yapıldı!")
        login(request,user)
        return redirect("index")
        
        
    return render(request,"login.html",context)

def logoutusr(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yapıldı!")
    return redirect(index)
