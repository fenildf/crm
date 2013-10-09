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
def main_page(request):
    return HttpResponse("个人主页")
def main_customer(request):
    return HttpResponse("客户")
def main_contact(request):
    return HttpResponse("联系人")
def main_sale_opportunity(request):
    return HttpResponse("业务机会")
def main_project_apply(request):
    return HttpResponse("立项申请")
def main_weekly_plan(request):
    return HttpResponse("周计划")
def main_travel_request(request):
    return HttpResponse("出差申请")
def main_travel_report(request):
    return HttpResponse("出差汇报")
def main_budget_apply(request):
    return HttpResponse("业务费用申请")
def main_business_apply(request):
    return HttpResponse("商务支持申请")
def main_sale_report(request):
    return HttpResponse("销售报表")