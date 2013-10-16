# coding=utf-8
from django.db import models
# 客户	customer
# 联系人	contact
# 业务机会	sale_opportunity
# 立项申请表	project_apply
# 周计划	Weekly_plan
# 出差申请表	 travel_request
# 出差汇报表	travel_report
# 业务费用申请报销表	budget_apply
# 商务支持申请	business_apply
# 统计报表	sale_report
class Customer(models.Model):
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    budget = models.CharField(max_length=50)
    #每个模型都要有一个用户(这里的用户指的是销售)
    username = models.CharField(max_length=30)
    #alter table hycrm_customer add column note varchar(100)
    note = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
# 姓名、职务、性别、对应客户、所属人
#部门、电话、手机、电子邮件、费用次数
# 费用累计
class Contact(models.Model):
    name = models.CharField(max_length=30)
    duty = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    #对应的客户名称
    customer_name = models.CharField(max_length=30)
    #对应的登录用户名称
    username = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    budget_count = models.CharField(max_length=30)
    budget_sum = models.CharField(max_length=30)
    note = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
## 基本信息（业务机会名称、对应客户、对应联系人、竞争对手分析、阶段、是否立项审批、推荐产品、客户决策链）；
## 项目信息（预先销售额、预计毛利、占年度目标比例、预计招标日期、签约时间、厂家支持率、是否报备、目前费用总和、目前面临的问题、下一步工作计划、资源需求、已处于本阶段几周、何时进入下一阶段、赢率）；
## 备注
#class Sale_opportunity(models.Model):
#    name = models.CharField(max_length=30)
#    customer_name = models.CharField(max_length=30)
#    contact_name = models.CharField(max_length=30)
#    username = models.CharField(max_length=30)
#    competitors_info = models.CharField(max_length=60)
#    phase = models.CharField(max_length=30)
#    project_apply_approved  = models.CharField(max_length=30)
#    recommend_products = models.CharField(max_length=30)
#    customer_decision = models.CharField(max_length=30)
#    projected_sales = models.CharField(max_length=30)
#    projected_gross_profit = models.CharField(max_length=30)
#    annual_goal_percentage = models.CharField(max_length=30)
#    expected_tender_date = models.CharField(max_length=30)
#    sign_Time = models.CharField(max_length=30)
#    manufacturers_support_rate = models.CharField(max_length=30)
#    is_filing = models.CharField(max_length=30)
#    current_budget_sum = models.CharField(max_length=30)
#    current_problem = models.CharField(max_length=30)
#    following_plan = models.CharField(max_length=30)
#    resource_Requirements = models.CharField(max_length=30)
#    current_week = models.CharField(max_length=30)
#    next_phase_time = models.CharField(max_length=30)
#    success_chance = models.CharField(max_length=30)
#    note = models.CharField(max_length=30)
#    def __unicode__(self):
#        return self.name
