from django.shortcuts import render

# Create your views here.
def a2_first(request):
    return render(request,'a2_'first.html)
def a2_second(request):
    return render(request,'a2_second.html')
