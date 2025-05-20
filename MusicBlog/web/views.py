from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def piano(request):
    return render(request, 'piano.html')

def composition(request):
    return render(request, 'composition.html')

def theory(request):
    return render(request, 'theory.html')

def about(request):
    return render(request, 'About.html')