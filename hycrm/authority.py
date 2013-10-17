# coding=utf-8
__author__ = 'lwy'
# 根据用户显示主页的菜单
# 根据用户的组等来控制显示的权限
from hycrm.models import Customer, Contact,Sale_opportunity


def get_user_display_model(user):
    if user == 'admin':
        user_display_model = ['main_page',
                              'main_customer',
                              'main_contact',
                              'main_sale_opportunity',
                              'main_project_apply',
                              'main_weekly_plan',
                              'main_travel_request',
                              'main_travel_report',
                              'main_budget_apply',
                              'main_business_apply',
                              'main_sale_report']
    elif user == 'lwy':
        user_display_model = ['main_page',
                              'main_customer',
                              'main_contact']
    elif user == 'yh':
        user_display_model = ['main_page',
                              'main_customer',
                              'main_contact',
                              'main_sale_opportunity',
                              'main_project_apply',
                              'main_weekly_plan']
    return user_display_model

# 客户
def get_user_customer(user):
#if user == 'admin':
    return Customer.objects.all()
    #else:
    #    return Customer.objects.all().filter(username=user)

def create_user_customer(item):
    Customer(name=item[0],
             kind=item[1],
             phone=item[2],
             address=item[3],
             budget=item[4],
             username=item[5],
             note=item[6]).save()


def edit_user_customer(item):
    Customer.objects.filter(id=item[0]).update(name=item[1],
                                               kind=item[2],
                                               phone=item[3],
                                               address=item[4],
                                               note=item[5])
#联系人
def get_user_contact(user):
    return Contact.objects.all()
def create_user_contact(item):
    Contact(name=item[0],
            duty=item[1],
            gender=item[2],
            customer_name=item[3],
            username=item[4],
            department=item[5],
            telephone=item[6],
            mobile=item[7],
            email=item[8],
            budget_count=item[9],
            budget_sum=item[10],
            note=item[11]).save()
def edit_user_contact(item):
    Contact.objects.filter(id=item[0]).update(name=item[1],
                                              duty=item[2],
                                              gender=item[3],
                                              customer_name=item[4],
                                              department=item[5],
                                              telephone=item[6],
                                              mobile=item[7],
                                              email=item[8],
                                              note=item[9])
def get_user_customer_name(item):
    return Customer.objects.all().values('name')
def get_user_sale_opportunity(item):
    return Sale_opportunity.objects.all()