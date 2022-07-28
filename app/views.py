from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def deshboard(request):
    return render(request, 'home.html')
def home(request):
    return render(request, 'home.html')
def bgimage(request):
    return render(request, 'bgimage.html')
def bgvideo(request):
    return render(request, 'bgvideo.html')
def section(request):
        return render(request, 'section.html')
        
