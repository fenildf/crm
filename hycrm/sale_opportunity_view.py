# coding=utf-8
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from hycrm.authority import get_user_display_model
from hycrm.authority import get_user_sale_opportunity, get_user_customer_name, get_user_contact_name, create_user_sale_opportunity, edit_user_sale_opportunity
from django.contrib.auth.decorators import login_required
import json


@login_required(login_url='/')
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


@login_required(login_url='/')
def new_sale_opportunity(request):
    model_list = get_user_display_model(request.user.username)
    t = get_template('main_sale_opportunity_detail.html')
    customer_data = get_user_customer_name(request)
    html = t.render(Context(
        {'username': request.user.username,
         'title': "新建",
         'customer_data': customer_data,
         'model_list': model_list}
    ))
    return HttpResponse(html)


def save_new_sale_opportunity(request):
    create_user_sale_opportunity([request.POST.get('name'),
                                  request.POST.get('customer_name'),
                                  request.POST.get('contact_name'),
                                  request.user.username,
                                   'No.123',
                                  request.POST.get('competitors_info'),
                                  request.POST.get('phase'),
                                  request.POST.get('project_apply_approved'),
                                  request.POST.get('recommend_products'),
                                  request.POST.get('customer_decision'),
                                  request.POST.get('projected_sales'),
                                  request.POST.get('projected_gross_profit'),
                                  request.POST.get('annual_goal_percentage'),
                                  request.POST.get('expected_tender_date'),
                                  request.POST.get('sign_Time'),
                                  request.POST.get('manufacturers_support_rate'),
                                  request.POST.get('is_filing'),
                                  0,
                                  request.POST.get('current_problem '),
                                  request.POST.get('following_plan'),
                                  request.POST.get('resource_Requirements'),
                                  request.POST.get('current_week'),
                                  request.POST.get('next_phase_time'),
                                  request.POST.get('success_chance'),
                                  request.POST.get('note')])
    return HttpResponseRedirect('/crm/sale_opportunity/')


@login_required(login_url='/')
def edit_sale_opportunity(request):
    model_list = get_user_display_model(request.user.username)
    t = get_template('main_sale_opportunity_detail.html')
    #@todo:把所有从数据库取到数据放到一个"数据模型"里渲染
    customer_data = get_user_customer_name(request)
    html = t.render(Context(
        {'username': request.user.username,
         'title': "编辑",
         'customer_data': customer_data,
         'model_list': model_list}
    ))
    return HttpResponse(html)


def save_edit_sale_opportunity(request):
    edit_user_sale_opportunity([request.POST.get('id'),
                                request.POST.get('name'),
                                request.POST.get('customer_name'),
                                request.POST.get('contact_name'),
                                request.POST.get('competitors_info'),
                                request.POST.get('phase'),
                                request.POST.get('project_apply_approved'),
                                request.POST.get('recommend_products'),
                                request.POST.get('customer_decision'),
                                request.POST.get('projected_sales'),
                                request.POST.get('projected_gross_profit'),
                                request.POST.get('annual_goal_percentage'),
                                request.POST.get('expected_tender_date'),
                                request.POST.get('sign_Time'),
                                request.POST.get('manufacturers_support_rate'),
                                request.POST.get('is_filing'),
                                request.POST.get('current_problem '),
                                request.POST.get('following_plan'),
                                request.POST.get('resource_Requirements'),
                                request.POST.get('current_week'),
                                request.POST.get('next_phase_time'),
                                request.POST.get('success_chance'),
                                request.POST.get('note')])
    return HttpResponseRedirect('/crm/sale_opportunity/')


def get_sale_opportunity_contact_name(request):
    contact_name = get_user_contact_name(request)
    return HttpResponse(json.dumps(list(contact_name), ensure_ascii=False))