from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hello,hsn!')


def article(request, n):
    # return HttpResponse('the text')
    return render(request, 'index.html')
