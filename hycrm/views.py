# coding=utf-8
# Create your views here.
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from hycrm.authority import get_user_display_model, get_user_customer, save_new_customer
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template import Context


def index(request):
    return render_to_response('login.html')


def main_view(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
    else:
        return HttpResponse("请先登陆")
    model_list = get_user_display_model(request.user.username)
    t = get_template('base.html')
    html = t.render(Context({'username': request.user.username, 'model_list': model_list}))
    return HttpResponse(html)


def main_page(request):
    return HttpResponse("个人主页")


def main_customer(request):
    #1.获取该用户的客户数据
    #2.建立用于显示的页面
    #3.数据和显示页面关联起来
    #4.完成页面的新增操作
    model_list = get_user_display_model(request.user.username)
    customer_data = get_user_customer(request.user.username)
    t = get_template('main_customer.html')
    html = t.render(Context(
        {'username': request.user.username,
         'model_list': model_list,
         'customer_data': customer_data}
    ))
    return HttpResponse(html)


def new_customer(request):
    # 储存数据
    save_new_customer([request.POST.get('name'),
                       request.POST.get('kind'),
                       request.POST.get('phone'),
                       request.POST.get('address'),
                       0,
                       request.user.username,
                       request.POST.get('note')])
    return HttpResponseRedirect('/crm/main_customer/')
def edit_customer(request):
    # 储存数据
    save_new_customer([request.POST.get('name'),
                       request.POST.get('kind'),
                       request.POST.get('phone'),
                       request.POST.get('address'),
                       0,
                       request.user.username,
                       request.POST.get('note')])
    return HttpResponseRedirect('/crm/main_customer/')

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