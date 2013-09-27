# Create your views here.
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response

def login_view(request):
    return render_to_response('login.html')

def login_auth(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username,password=password)
    if user is not None and user.is_active:
    # Correct password, and the user is marked "active"
        auth.login(request, user)
    # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")