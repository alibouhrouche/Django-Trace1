from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
def login_view(request):
    if request.method == "GET":
        return render(request, "accounts/index.html")
    username = request.POST["username"]
    password = request.POST["password"]
    try:
        remember_me = request.POST["remember_me"]
    except KeyError:
        remember_me = None
    if remember_me == "on":
        request.session.set_expiry(60 * 60 * 24 * 7)
    else:
        request.session.set_expiry(0)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/")
    return render(request, "accounts/index.html", {"error": "Invalid username or password"})


def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect("/")

