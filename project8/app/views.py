from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *
# Create your views here.


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        customer = Customer(cname=name, email=email, pno=pno, un=un, pw=pw)
        customer.save()
        return HttpResponse('Regisrtations Successfull')
    return render(request, 'register.html')

def register_django_forms(request):
    ECFO = CustomerForm()
    d = {'ECFO': ECFO}
    if request.method == 'POST':
        name = request.POST.get('name')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        customer = Customer(cname=name, email=email, pno=pno, un=un, pw=pw)
        customer.save()
        return HttpResponse('Regisrtations Successfull')
    return render(request, 'register_django_forms.html', d)