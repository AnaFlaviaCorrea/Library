from django.shortcuts import render, HttpResponse
from . models import Books

def index(request):
    books = Books.objects.all()
    return render(request, 'pages/index.html', {'books': books})

def search(request):
    busca = request.GET.get('search')
   
    books= Books.objects.filter(name__icontains = busca)
    return render(request, 'pages/index.html', {'books': books})
