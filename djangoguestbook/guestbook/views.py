from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from article.models import Article
from .forms import WriteForm
from .process import get, write

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    form = WriteForm()
    c = {'count': list(range(1, 6)), 'form': form}

    if request.method == 'GET':
        articles = get()
        c['articles'] = articles
        
    elif request.method == 'POST':
        form = WriteForm(request.POST)
        if form.is_valid():
            write(request.POST)
        else:
            return HttpResponse(status=400)

    return render(request, 'index.html', c)