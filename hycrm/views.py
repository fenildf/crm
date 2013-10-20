# coding=utf-8
# Create your views here.
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from hycrm.authority import get_user_display_model
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.decorators import login_required


def index(request):
    return render_to_response('login.html')
#todo:session注销用户之后，用浏览器后退还能进入登陆状态??????
@login_required(login_url='/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def main_view(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        model_list = get_user_display_model(request.user.username)
        t = get_template('base.html')
        html = t.render(Context({'username': request.user.username, 'model_list': model_list}))
        return HttpResponse(html)
    else:
        return HttpResponseRedirect("/")


@login_required(login_url='/')
def main_page(request):
    return HttpResponse("个人主页")


@login_required(login_url='/')
def main_project_apply(request):
    return HttpResponse("立项申请")


@login_required(login_url='/')
def main_weekly_plan(request):
    return HttpResponse("周计划")


@login_required(login_url='/')
def main_travel_request(request):
    return HttpResponse("出差申请")


@login_required(login_url='/')
def main_travel_report(request):
    return HttpResponse("出差汇报")


@login_required(login_url='/')
def main_budget_apply(request):
    return HttpResponse("业务费用申请")


@login_required(login_url='/')
def main_business_apply(request):
    return HttpResponse("商务支持申请")


@login_required(login_url='/')
def main_sale_report(request):
    return HttpResponse("销售报表")