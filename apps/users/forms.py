#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "BIGNI"
__date__ = "2017/3/19 18:53"
from django import forms


from captcha.fields import CaptchaField
class LoginForm(forms.Form):
    #required为True，表字段不能为空,username和password这两个名称必须和html里form表单的name名称一致，
    # 否则不会进行校验
    UserName = forms.CharField(required=True)
    Password = forms.CharField(required=True,min_length=4)

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=4)
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})


class ModifyForm(forms.Form):
    password = forms.EmailField(required=True,min_length=5)
    password2 = forms.EmailField(required=True,min_length=5)