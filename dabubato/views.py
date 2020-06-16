from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # TODO: https://docs.djangoproject.com/ja/3.0/intro/tutorial03/
    context = {
        "context_key": "context_value",
    }
    return render(request, 'index.html', context)

def hello(request):
    return HttpResponse("Hello, world. You're at the polls index.")