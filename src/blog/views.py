from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index_view(request):
    return render(request, 'blog/index.html')

def article_view(request, numero_article):
    if numero_article in ["01", "02", "03"]:
        return render(request, f'blog/article_{numero_article}.html')
    return render(request, 'blog/page_not_found.html')