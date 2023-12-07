from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def login_view(request):
    if request.method == "GET":
        return render(request, "accounts/index.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    remember_me = request.POST.get("remember_me", False)
    if remember_me == "on":
        request.session.set_expiry(60 * 60 * 24 * 7)
    else:
        request.session.set_expiry(0)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if request.headers.get("HX-Request", "") == "true":
            return HttpResponse(headers={
                "HX-Refresh": "true",
            })
        return redirect("/")
    if request.headers.get("HX-Request", "") == "true":
        return render(request, "core/alerts.html", {
            "type": "error",
            "title": "Error",
            "message": "Invalid username or password",
        })
    return render(request, "accounts/index.html", {"error": "Invalid username or password"})


def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect("/")

