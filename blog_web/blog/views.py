from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def article(request, article_id):
    # return HttpResponse('the text')
    return render(request, 'article'+article_id+'.html')

'''
def article_index(request):
    return render(request, 'index.html')
'''
