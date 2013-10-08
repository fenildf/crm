# coding=utf-8
__author__ = 'lwy'

# 根据用户显示主页的菜单
user_display_model = ['客户', '联系人','业务机会','周计划','出差申请','出差汇报','业务费用申请报销','售前支持','商务支持','统计报表']

# 根据用户的组等来控制显示的权限
def get_user_display_model(user):
    if user == 'admin':
        return user_display_model
    if user == 'lwy':
        user_display_model.remove('业务机会')
        user_display_model.remove('周计划')
        user_display_model.remove('出差申请')
        user_display_model.remove('出差汇报')
        user_display_model.remove('业务费用申请报销')
        user_display_model.remove('售前支持')
        user_display_model.remove('商务支持')
        user_display_model.remove('统计报表')

        return user_display_model

# 用户数据权限的控制，实现方式是把模型加入到admin里，再调用admin里的函数么？
# def get_user_data_model(user):