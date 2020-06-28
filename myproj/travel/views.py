from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TravelData
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def main(request):
 Travelobj = TravelData.objects.all()
 return render(request,'index.html',{'TravelData': Travelobj})

def main_details(request,pk):
 Travelobj = TravelData.objects.filter(pk = pk)
 return render(request,'details.html',{'TravelData': Travelobj})

def signup(request):
 if request.method == 'POST':
     first_name = request.POST['first_name']
     last_name = request.POST['last_name']
     username = request.POST['username']
     password = request.POST['password']
     email = request.POST['email']
     u = User.objects.create_user(first_name = first_name, last_name = last_name, username = username,
     password = password, email= email  )
     u.save()
     messages.info(request,'Registration Successful!!')
     return redirect('/travel/main/')

 else:
      return render(request,'signup.html')


def login(request):
 if request.method == 'POST':
     username = request.POST['username']
     password = request.POST['password']
     user = auth.authenticate(username=username, password=password)

     if user is not None:
         auth.login(request,user)
         return redirect('/travel/main/')
     else:
         messages.info(request,'Invalid Credentials')
         return redirect('/travel/login/')  

 else:
      return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/travel/main/') 