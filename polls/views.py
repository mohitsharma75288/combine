from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import contactform
from .models import question

def index(request):
    if request.method=='POST':
    	form=contactform(request.POST)
    	if form.is_valid():
    		name=form.cleaned_data.get('name')
    		email=form.cleaned_data.get('mail')
    		message=form.cleaned_data.get('message')
    		dsobj=question()
    		dsobj.name='name'
    		dsobj.email='email'
    		dsobj.message='message'
    		dsobj.save()


    form=contactform()
    return render(request,'polls/index.html', {'form':form}) 	