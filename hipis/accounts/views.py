from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        request.session['message'] = "Login, Failed!"
    return redirect("index")

def logout_view(request):
    logout(request)
    return redirect("index")
