# coding=utf-8
# Create your views here.
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from hycrm.authority import get_user_display_model
from hycrm.authority import get_user_customer, create_user_customer, edit_user_customer
from hycrm.authority import get_user_contact, create_user_contact, edit_user_contact, get_user_customer_name
from hycrm.authority import get_user_sale_opportunity
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template import Context
import json

#ajax方式获取联系人对应的所属客户
def get_customer_name(request):
    customer_name = get_user_customer_name(request)
    name = []
    for v in customer_name:
        name.append(v['name'])
    return HttpResponse(json.dumps(name, ensure_ascii=False))


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
    create_user_customer([request.POST.get('name'),
                          request.POST.get('kind'),
                          request.POST.get('phone'),
                          request.POST.get('address'),
                          0,
                          request.user.username,
                          request.POST.get('note')])
    return HttpResponseRedirect('/crm/main_customer/')


def edit_customer(request):
    # 储存数据
    edit_user_customer([request.POST.get('id'),
                        request.POST.get('name'),
                        request.POST.get('kind'),
                        request.POST.get('phone'),
                        request.POST.get('address'),
                        request.POST.get('note')])
    return HttpResponseRedirect('/crm/main_customer/')

#------------------------------------------------------------
def main_contact(request):
    model_list = get_user_display_model(request.user.username)
    contact_data = get_user_contact(request.user.username)
    t = get_template('main_contact.html')
    html = t.render(Context(
        {'username': request.user.username,
         'model_list': model_list,
         'contact_data': contact_data}
    ))
    return HttpResponse(html)


def new_contact(request):
    # 储存数据
    create_user_contact([request.POST.get('name'),
                         request.POST.get('duty'),
                         request.POST.get('gender'),
                         request.POST.get('customer_name'),
                         request.user.username,
                         request.POST.get('department'),
                         request.POST.get('telephone'),
                         request.POST.get('mobile'),
                         request.POST.get('email'),
                         0,
                         0,
                         request.POST.get('note')])
    return HttpResponseRedirect('/crm/main_contact/')


def edit_contact(request):
    # 储存数据
    edit_user_contact([request.POST.get('id'),
                       request.POST.get('name'),
                       request.POST.get('duty'),
                       request.POST.get('gender'),
                       request.POST.get('customer_name'),
                       request.POST.get('department'),
                       request.POST.get('telephone'),
                       request.POST.get('mobile'),
                       request.POST.get('email'),
                       request.POST.get('note')])
    print(request.POST.get('name'))
    return HttpResponseRedirect('/crm/main_contact/')


def main_sale_opportunity(request):
    model_list = get_user_display_model(request.user.username)
    sale_opportunity_data = get_user_sale_opportunity(request.user.username)
    t = get_template('main_sale_opportunity.html')
    html = t.render(Context(
        {'username': request.user.username,
         'model_list': model_list,
         'sale_opportunity_data': sale_opportunity_data}
    ))
    return HttpResponse(html)


def new_sale_opportunity(request):
    model_list = get_user_display_model(request.user.username)
    t = get_template('main_sale_opportunity_detail.html')
    html = t.render(Context(
        {'username': request.user.username,
         'title': "新建业务机会",
         'model_list': model_list}
    ))
    return HttpResponse(html)


def edit_sale_opportunity(request):
    model_list = get_user_display_model(request.user.username)
    t = get_template('main_sale_opportunity_detail.html')
    html = t.render(Context(
        {'username': request.user.username,
         'title': "编辑业务机会",
         'model_list': model_list}
    ))
    return HttpResponse(html)


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