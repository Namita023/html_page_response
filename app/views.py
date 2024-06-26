from django.shortcuts import render

# Create your views here.

def wish(request):
    return render(request,'wish.html')

def thank(request):
    return render(request,'thank.html')