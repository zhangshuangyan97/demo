from django.shortcuts import render,redirect

from user.forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid(): # 返回True或Flase
            user = form.save()
            return redirect("/user/info")
        else:
            return render(request, "register.html",{"error": form.errors})
    return render(request,"register.html")
def login(request):
    return render(request,"register.html")
def logout(request):
    return render(request,"register.html")
def user_info(request):
    return render(request,"register.html")