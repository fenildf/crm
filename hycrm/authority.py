# coding=utf-8
__author__ = 'lwy'
# 根据用户显示主页的菜单
# 根据用户的组等来控制显示的权限
from hycrm.models import Customer, Contact, Sale_opportunity


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

#ajax获取客户名
def get_user_customer_name(request):
    return Customer.objects.all().values_list('name', flat=True)

#获取客户下属的联系人名
def get_user_contact_name(request):
    return Contact.objects.all().filter(customer_name=request.POST['name']).values_list('name', flat=True)


# 客户
def get_user_customer(user):
    return Customer.objects.all()


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


def get_user_sale_opportunity(item):
    return Sale_opportunity.objects.all()


def create_user_sale_opportunity(item):
    Sale_opportunity(name=item[0],
                     customer_name=item[1],
                     contact_name=item[2],
                     username=item[3],
                     project_id=item[4],
                     competitors_info=item[5],
                     phase=item[6],
                     project_apply_approved=item[7],
                     recommend_products=item[8],
                     customer_decision=item[9],
                     projected_sales=item[10],
                     projected_gross_profit=item[11],
                     annual_goal_percentage=item[12],
                     expected_tender_date=item[13],
                     sign_Time=item[14],
                     manufacturers_support_rate=item[15],
                     is_filing=item[16],
                     current_budget_sum=item[17],
                     current_problem=item[18],
                     following_plan=item[19],
                     resource_Requirements=item[20],
                     current_week=item[21],
                     next_phase_time=item[22],
                     success_chance=item[23],
                     note=item[24]).save();

def edit_user_sale_opportunity(item):
    Sale_opportunity.objects.filter(id=item[0]).update(name=item[1],
                                                       customer_name=item[2],
                                                       contact_name=item[3],
                                                       competitors_info=item[4],
                                                       phase=item[5],
                                                       project_apply_approved=item[6],
                                                       recommend_products=item[7],
                                                       customer_decision=item[8],
                                                       projected_sales=item[9],
                                                       projected_gross_profit=item[10],
                                                       annual_goal_percentage=item[11],
                                                       expected_tender_date=item[12],
                                                       sign_Time=item[13],
                                                       manufacturers_support_rate=item[14],
                                                       is_filing=item[15],
                                                       current_problem=item[16],
                                                       following_plan=item[17],
                                                       resource_Requirements=item[18],
                                                       current_week=item[19],
                                                       next_phase_time=item[20],
                                                       success_chance=item[21],
                                                       note=item[22]).save();