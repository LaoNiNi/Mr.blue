from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
# Create your views here.
from .models import UserProfile,EmailVerifyRecord
from .forms import LoginForm,RegisterForm,ForgetForm,ModifyForm
from utils.email_send import send_register_email
class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form":register_form})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email","")
            if UserProfile.objects.filter(email=user_name):
                return  render(request,"register.html",{"msg":"用户已存在","register_form":register_form})
            pass_word = request.POST.get("password","")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.is_active = False
            user_profile.save()

            send_register_email(user_name,"register")
            return render(request, "login.html", {})
        else:
            return  render(request,"register.html",{"register_form":register_form})


class ActiveUserView(View):
    def get(self,request,active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                #通过get方法获取匹配的数据，返回一个对象
                user = UserProfile.objects.get(email=email)
                #修改is_active字段的值
                user.is_active = True
                user.save()
        else:
            return render(request,"active_false.html")
        return render(request,"login.html")


class LoginaView(View):
    def get(self,request):
        return render(request,"login.html",{})
    def post(self,request):
        #通过指定提交方式，可以自动识别
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("UserName", "")
            passwd = request.POST.get("Password", "")
            user = authenticate(username=user_name, password=passwd)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", {"msg": "用户未激活"})
            else:
                return render(request, "login.html", {"msg": "请输入正确的用户名和密码"})
        else:
            return render(request, "login.html", {"msg": "请输入正确的用户名和密码"})


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username)|Q(email = username)|Q(moble_phone= username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class ForgetPwd(View):
    def get(self,request):
        forget_form = ForgetForm()
        return render(request,"forgetpwd.html",{"forget_form":forget_form})

    def post(self,request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email","")
            send_register_email(email,"forget")
            return render(request,"send_succeed.html")
        else:
            return render(request, "forgetpwd.html", {"forget_form": forget_form})


class ResetView(View):
    def get(self,request,reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request,"password_reset.html",{"email":email})
        else:
            return render(request,"active_false.html")
        return render(request,"login.html")

class ModifyPwdView(View):
    def post(self,request):
        modify_form = ModifyForm(request.POST)
        if modify_form.is_valid():
            pwd = request.POST.get("password",'')
            pwd2 = request.POST.get("password2",'')
            email = request.POST.get("email",'')
            if pwd !=pwd2:
                return render(request, "password_reset.html", {"email": email,"msg":"密码不一致"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request,"login.html")
        else:
            email = request.POST.get("email", '')
            return render(request, "password_reset.html", {"email": email,"modify_form":modify_form})



