from django.shortcuts import render
def forloop(request):
    d={'name':'ashu'}
    return render(request,'forloop.html',d)

# Create your views here.
