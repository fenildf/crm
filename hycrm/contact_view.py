# coding=utf-8
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from hycrm.authority import get_user_display_model
from hycrm.authority import get_user_contact, create_user_contact, edit_user_contact,get_user_customer_name

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

