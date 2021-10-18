from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import agregarambiente



# Create your views here.

def home(request):
    return HttpResponse('Holaa')

def forms(request):
    form=agregarambiente()
    return render(request,'formulario.html',{'form':form})