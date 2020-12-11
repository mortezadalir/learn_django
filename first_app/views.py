from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from .forms import Personform

# Create your views here.
def index(request):
    form=Personform()
    if request.method=='POST':
        form=Personform(request.POST)
        form.save()
        print(form)
        if form.is_valid():
            print(form.cleaned_data['first_name'])
            print(form.cleaned_data['last_name'])
        
    #return HttpResponse("<em>Hello World</em>")
    return render(request,'first_app/index.html',{'form':form})
    
    
def myapp(request):
    return HttpResponse("<h1>this is myapp page</h1> ")