#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "BIGNI"
__date__ = "2017/3/12 12:52"

import xadmin

from .models import CityDict
from  .models import CourseOrg
from .models import Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc','add_time']
    search_fields = ['name', 'desc','add_time']
    list_filter = ['name', 'desc','add_time']


xadmin.site.register(CityDict,CityDictAdmin)


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums','image','address','city','add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums','image','address','city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums','image','address','city','add_time']


xadmin.site.register(CourseOrg,CourseOrgAdmin)



class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company','work_position','points','click_nums','fav_nums','add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company','work_position','points','click_nums','fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company','work_position','points','click_nums','fav_nums','add_time']

xadmin.site.register(Teacher,TeacherAdmin)






