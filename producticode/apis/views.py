from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json


@csrf_exempt
def register(request):
    if request.method=="POST":
        data = json.loads(request.body)
        user = User.objects.create_user(username = data['username'], password = data['password'])
        user.save()
        
        
       
       
            
        return JsonResponse({
            'message':'hello'
        })
    return JsonResponse({
            'message':'hello'
        })    

@csrf_exempt
def login_page(request):
    if request.method=="POST":
        login_data = json.loads(request.body)
        user = authenticate(request, username = login_data['username'], password = login_data['passText'])
        if user is not None:
            login(request,user)


        
    
        return JsonResponse({'message': 'Login successful','username':request.user.username,'login_error':'No Error'})
    
@csrf_exempt
def logout_page(request):
    logout(request)
    return JsonResponse({'message' : "Logout successful"})    
     


        

    

# Create your views here.
