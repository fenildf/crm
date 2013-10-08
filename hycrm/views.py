# coding=utf-8
# Create your views here.
from django.http.response import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.shortcuts import render_to_response
from authority import  get_user_display_model
from django.contrib.auth.decorators import login_required

def index(request):
    return render_to_response('login.html')

def main_view(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
    else:
        return HttpResponse("请先登陆")
    model_list = get_user_display_model(request.user.username)
    return render_to_response('user_model.html', {'username': request.user.username, 'model_list': model_list})

def denglu(request):
    return HttpResponse("denglule")

# def weidenglu(request):
#     return HttpResponse("weidenglule")