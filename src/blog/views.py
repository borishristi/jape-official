from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index_view(request):
    return HttpResponse("<h1>news_link for index.html</h1>")
