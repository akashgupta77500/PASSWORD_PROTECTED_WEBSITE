from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login

def login(request):
    error=""
    if request.method == "POST":
        u = request.POST["username"]
        p = request.POST["password"]
        user = authenticate(request, username=u, password=p)
        if user:
            try:
                auth_login(request, user)
                error="no"
            except:
                error="yes"   
        else:
            error="yes"    
    d = {'error' : error}
    return render(request,"login.html",d)


def api(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,"api.html")

def logout_logout(request):
    logout(request)
    return redirect ('login')