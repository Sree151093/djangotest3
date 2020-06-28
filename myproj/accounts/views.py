from django.shortcuts import render
from django.http import HttpResponse
from .models import PersonalDetails

# Create your views here.

def home(request):
 val = PersonalDetails.objects.get(id=6)
 return render(request,'home.html',{'key':val})
