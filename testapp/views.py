from django.shortcuts import render,redirect
from testapp import forms
from testapp.models import Insertion
from .forms import InsertionForm
import sqlite3
from django.contrib import messages
from django.http import HttpResponse

def create(request):
    form=forms.InsertionForm()
    if request.method=='POST':
        form=forms.InsertionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            
    return render(request, 'insert.html',{'form':form})


def read(request):
    data= Insertion.objects.all()
    my_dict2={'data':data}
    #print(data2)
    return render(request, 'read.html',context=my_dict2)  

def delete(request,id):
     data2= Insertion.objects.get(id=id)
     data2.delete()
     return redirect("/read")

def edit(request,id):
    data2=Insertion.objects.get(id=id)
    my_dict2={'data2':data2}
    

    return render(request, 'edit.html',context=my_dict2)  


def update(request,id):
    if request.method=='POST':
        data2=Insertion.objects.get(id=id)
        #print(data2)
        my_dict2={'data2':data2}
        form=InsertionForm(request.POST,instance=data2)
        if form.is_valid:
            form.save(commit=True)
    return redirect("/read")
        
    #return render(request, 'read.html',context=my_dict2) 
'''  
def edit(request,id):
    firstname=request.POST.get('firstname')
    unique=request.POST.get('unique')
    db=sqlite3.connect('db.sqlite3')
    db.execute("update testapp_insertion set firstname='"+firstname+"' whrere id='"+unique+"'")


    db.commit()
    return redirect("/read")  
'''
# Create your views here.
