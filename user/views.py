from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.hashers import make_password,mask_hash
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from .models import Users
from .forms import UserCreationForm

def register(request):
    if request.method == "GET":
        return render(
            request, "registration/registration.html",
            {"form": UserCreationForm}
        )
    elif request.method == "POST":
        try:
            form = UserCreationForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'your account is successfully Created')
                return redirect('/user/accounts/login/')
            else:
                messages.error(request,form.errors)
                return redirect('/user/register/')

        except IntegrityError as e:
            messages.error(request,"Email is already used, please use new Email")
            return redirect('/user/register/')
        except Exception as e:
            messages.error(request,e)
            return redirect('/user/register/')
