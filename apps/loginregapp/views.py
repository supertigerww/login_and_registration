# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import user
import bcrypt
import json

# Create your views here.
def index(request):
    return render(request, 'loginregapp/index.html')
def register(request):
    if request.method == 'POST':
        errors =  user.objects.validation(request.POST)
        if len(errors):
            for register,error in errors.iteritems():
                messages.error(request, error, extra_tags=register)
            return redirect('/')
        else:
            bcryptpassword = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            user.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=bcryptpassword)
            currentuser=user.objects.get(email=request.POST['email'])
            request.session['currentuser']=currentuser
            return redirect('/success')
    else:
        return redirect('/')
def login(request):
    loginerrors = user.objects.loginvalidation(request.POST)
    if len(loginerrors):
        for login, error in loginerrors.iteritems():
            messages.error(request,error,extra_tags=login)
            return redirect('/')
    else:
        currentuser=user.objects.get(email=request.POST['email'])
        request.session['currentuser']=currentuser
        return redirect('/success')
def success(request):
    if "currentuser"  in request.session:
        info={
            "user": request.session['currentuser']
        }
        return render(request, 'loginregapp/success.html',info)
    else:
        return redirect('/')
def logout(request):
    request.session.clear()
    return redirect('/')
    
        


    

               
               
               


