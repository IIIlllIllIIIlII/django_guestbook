from django.shortcuts import render

# Create your views here.

def index(request):
    c = {'count': list(range(1, 6))}
    return render(request, 'index.html', c)