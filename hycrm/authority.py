# coding=utf-8
__author__ = 'lwy'
# 根据用户显示主页的菜单
# 根据用户的组等来控制显示的权限
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
        return user_display_model
    if user == 'lwy':
        user_display_model = ['main_page',
                              'main_customer',
                              'main_contact']
        return user_display_model
