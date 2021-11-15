
from django.http.response import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("<h1><center>Home page</center></h1>")
    return render(request,"home.html")
