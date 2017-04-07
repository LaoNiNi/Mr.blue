#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "BIGNI"
__date__ = "2017/4/2 12:10"
import re
from django import forms

from operation.models import UserAsk

#继承modelform
class UserAskForm(forms.ModelForm):
    #也可以添加自己所需的字段
    # my_field = forms.CharField()
    class Meta:
        #指定model
        model = UserAsk
        #指定需要model的那些字段
        fields = ['name','mobile','course_name']
    #s手机号码是有要求的，可以通过定义下面方法，必须是clean开头，这样初始化时会自动调用这个方法
    def clean_mobile(self):
        """
        验证手机是否合法
        """
        #modelform内置方法cleaned_data获取到mobile的value
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1\d{10}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码非法",code="mobile_invalid")
