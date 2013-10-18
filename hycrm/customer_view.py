# coding=utf-8
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from hycrm.authority import get_user_display_model
from hycrm.authority import get_user_customer, create_user_customer, edit_user_customer

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