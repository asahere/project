from django.shortcuts import render
from django.http import HttpResponse
from pro.models import student,employee

# Create your views here.

def home(request):
      # d={'name':'alex','age':20}
      d=student.objects.all()
      return render(request,'temp.html',{'d':d})
def index(request):
    return HttpResponse("hello welcome to this page")

def employee2(request):
      # d={'name':'alex','age':20}
      d=employee.objects.all()
      return render(request,'asa.html',{'d':d})