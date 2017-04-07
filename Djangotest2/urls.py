# _*_ encoding:utf-8 _*_
"""Djangotest2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
# from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve
from django.conf.urls.static import static
# from apps.message.views import getform
from users.views import LoginaView,RegisterView,ActiveUserView,ForgetPwd,ResetView,ModifyPwdView
from oraganization.views import OrgView
from .settings import MEDIA_ROOT
urlpatterns = [
    #后台
    url(r'^xadmin/', xadmin.site.urls),
    url('^$',TemplateView.as_view(template_name="index.html"),name="index"),
    #登陆页
    url('^login/$',LoginaView.as_view(),name="login"),
    #注册页
    url("^register/$",RegisterView.as_view(),name="register"),
    #验证码，每个app可以书写自己的url，然后通过include进来
    url(r'^captcha/', include('captcha.urls')),
    #注册激活链接
    url(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name="user_active"),
    #忘记密码链接
    url(r'^forget/$',ForgetPwd.as_view(),name="forget_pwd"),
    #重置密码页面
    url(r'^reset/(?P<reset_code>.*)/$',ResetView.as_view(),name="reset_code"),
    url(r'^modifypwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    #课程机构url配置,验证码，每个app可以书写自己的url，然后通过include进来
    url(r'^org/', include('oraganization.urls',namespace="org")),
    # 课程相关url配置
    url(r'^course/', include('course.urls', namespace="course")),
    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),

]
