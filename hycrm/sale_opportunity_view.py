# coding=utf-8
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from hycrm.authority import get_user_display_model
from hycrm.authority import get_user_sale_opportunity,get_user_customer_name,get_user_contact

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
    customer_data = get_user_customer_name(request.user.username)
    html = t.render(Context(
        {'username': request.user.username,
         'title': "新建",
         'customer_data':customer_data,
         'model_list': model_list}
    ))
    return HttpResponse(html)

def save_new_sale_opportunity(request):
    model_list = get_user_display_model(request.user.username)
    sale_opportunity_data = get_user_sale_opportunity(request.user.username)
    t = get_template('main_sale_opportunity.html')
    html = t.render(Context(
        {'username': request.user.username,
         'model_list': model_list,
         'sale_opportunity_data': sale_opportunity_data}
    ))
    return HttpResponse(html)

def edit_sale_opportunity(request):
    model_list = get_user_display_model(request.user.username)
    t = get_template('main_sale_opportunity_detail.html')
    #@todo:把所有从数据库取到数据放到一个"数据模型"里渲染

    html = t.render(Context(
        {'username': request.user.username,
         'title': "编辑",
         'model_list': model_list}
    ))
    return HttpResponse(html)

