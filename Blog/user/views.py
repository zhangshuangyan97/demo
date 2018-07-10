from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,"register.html")
def login(request):
    return render(request,"register.html")
def logout(request):
    return render(request,"register.html")
def user_info(request):
    return render(request,"register.html")