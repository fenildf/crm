# coding=utf-8
# Create your views here.
from django.http.response import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.shortcuts import render_to_response
from authority import  get_user_display_model

def index(request):
    return render_to_response('login.html')

def login_view(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)

    if user.username == "lwy":
        # return render_to_response('user_model.html',{'username':'lwy'})
        model_list = get_user_display_model(user.username)
        return render_to_response('user_model.html', {'username':'lwy','model_list': model_list})
    else:
        return render_to_response('main.html',{'username':'admin'})

def denglu(request):
    return  HttpResponse("denglule")

def weidenglu(request):
    return index(request)