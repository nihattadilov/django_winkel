from django.shortcuts import redirect, render

from django.http import HttpResponse
from core.forms import ContactForm

from core.models import Setting,Products,Testimonial

# Create your views here.

def home(request):
    context={
        'title':'Home page',
        'products':Products.objects.all(),
        'testimonials':Testimonial.objects.all()
    }    
    return render(request,'index.html',context)

def contact(request):
    if request.method=='POST':
        form= ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form=ContactForm()
        
    context ={
        'title':'Contact Page',
        'form':form,
        
    }
    return render(request,"contact.html",context=context)
        
    