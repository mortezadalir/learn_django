from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("<em>Hello World</em>")
    return render(request,'first_app/index.html')
    
    
def myapp(request):
    return HttpResponse("<h1>this is myapp page</h1> ")