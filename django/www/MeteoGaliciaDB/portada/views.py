from django.shortcuts import render

def index(request):
    return render(request, 'portada/index.html', None)