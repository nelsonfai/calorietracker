from django.shortcuts import render

# Create your views here.

def loginPage(request):
    return render(request, "login.html")
def registerPage(request):
    return render(request, "register.html")
def dashboardPage(request):
    return render(request, "index.html")