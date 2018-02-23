# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class usermanager(models.Manager):
    def validation(self,postData):
        errors = {}
        if len(postData['first_name']) <  1:
            errors['first_name'] = "First name should be no fewer than 2 characters"
        if any(char.isdigit() for char in postData['first_name']) == True:
            errors['first_name'] = "First name can not have numbers"
        if len(postData['last_name']) <  1:
            errors['last_name'] = "Last name should be no fewer than 2 characters"
        if any(char.isdigit() for char in postData['last_name']) == True:
            errors['last_name'] = "Last name can not have numbers"
        if not emailRegex.match(postData['email']):
            errors['email'] = "Invaild email address"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be greater than 8 characters"
        if postData['confirmpassword'] !=postData['password']:
            errors['confirmpassword'] = "Passwords do not match"
        return errors

    def loginvalidation(self,postData):
        loginerrors={}
        if user.objects.filter(email=postData['loginemail']):
            currentuser=user.objects.filter(email=postData['loginemail'])[0]
            hashed_pw=currentuser.password
            if bcrypt.checkpw(postData['loginpassword'].encode(), hashed_pw.encode()) == True:
                pass
            else:
                loginerrors['loginpassword']= "Wrong email or password"
        else:
            loginerrors['loginemail']= "Wrong email or password"
        return loginerrors
                


    

class user(models.Model):
    first_name =  models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True) 

    objects = usermanager()
