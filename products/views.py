from django.shortcuts import render, HttpResponse

# Create your views here.
def all(request):
    return render(request, 'all_prods.html')

def visc(request):
    return render(request, 'showcat.html')


def leth(request):
    return render(request, 'showcat.html')

def bro(request):
    return render(request, 'showcat.html')


def env(request):
    return render(request, 'showcat.html')