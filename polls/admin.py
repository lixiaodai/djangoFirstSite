#encoding:utf-8
from django.contrib import admin
from polls.models import Poll, Choise
from django.contrib.admin.templatetags.admin_list import date_hierarchy

# Register your models here.

#可以使用StackedInline，一个列表
#也可以使用TabularInline，一个表格
class ChoiseInline(admin.TabularInline):
    model = Choise
    extra = 1

#自定义的Model管理类
class PollAdmin(admin.ModelAdmin):
    #定义field顺序
    #fields = ['put_date','question']
    #使用fieldsets分割field，分组显示field。
    #collapse用于fieldsets收缩、伸展
    fieldsets = [
        ('Question',{'fields':['question']}),
        ('Data Infomation',{'fields':['put_date'],'classes':['collapse']})
    ]
    inlines = [ChoiseInline]
    #定义在列表页面展示的列，既可以是类的属性，也可是是类的方法名。
    #类的属性支持排序，但是类的方法名的返回值不支持排序
    list_display = ('question','put_date','was_published_recently')
    #定义列表页面的过滤属性，如果是DatetimeField，Django会自动添加范围的内容
    list_filter = ['question','put_date']
    #添加搜索字段，但是这个搜索字段是一个搜索栏，不是多个搜索条件，所以适合只使用一个field
    search_fields = ['question']
    #每页显示的记录数
    list_per_page = 20
    

#指定自定的管理类管理Model
admin.site.register(Poll,PollAdmin)
#admin.site.register(Choise)