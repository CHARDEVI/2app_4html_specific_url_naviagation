from django.shortcuts import render

# Create your views here.

def messi(request):
    return render(request,'messi.html')
def ronaldo(request):
    return render(request,'ronaldo.html')