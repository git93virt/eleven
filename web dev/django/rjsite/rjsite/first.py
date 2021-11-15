# this file is created by me

from django.http import HttpResponse


def hello(request):
    return HttpResponse('<h1>hello world</h1>')
