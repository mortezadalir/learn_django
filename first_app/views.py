from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from .forms import Personform

# Create your views here.
def index(request):
    name=['morteza','hosein','ali']
    form=Personform()
    my_dict={'name':name,'form':form,'insert':"Hello THIS is Injected from views"}
    if request.method=='POST':
        form=Personform(request.POST)
        form.save()
        print(form)
        if form.is_valid():
            print(form.cleaned_data['first_name'])
            print(form.cleaned_data['last_name'])
        
    #return HttpResponse("<em>Hello World</em>")
    return render(request,'first_app/index.html',my_dict)
    
    
def users(request):
    person_list=Person.objects.all()
    return render(request,"first_app/users.html",{'person_list':person_list})