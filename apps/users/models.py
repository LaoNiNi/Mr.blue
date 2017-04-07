from django.db import models
from datetime import datetime

#AbstractUser是auth_user的model
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name='昵称',default='')
    birday = models.DateField(verbose_name='生日',null=True,blank=True)
    gender = models.CharField(max_length=6,choices=(("male","男"),("female",'女')),default='male')
    # email = models.EmailField(max_length=50,verbose_name='邮箱')
    address = models.CharField(max_length=100,verbose_name='地址',default='')
    moble_phone = models.CharField(max_length=11,verbose_name='手机',null=True,blank=True)
    image = models.ImageField(upload_to="image/%Y/%m",default='image/default.png',max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name='验证码')
    email = models.EmailField(max_length=50,verbose_name='邮箱')
    send_type = models.CharField(verbose_name="验证码类型",max_length=20,choices=(("register","注册"),("forget","找回密码")))
    #这里的now方法，如果加了括号，则时间是这个model编译的时间，不加括号则是这个class实例化的时间
    send_time = models.DateTimeField(verbose_name="发送时间",default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return '{0}({1})'.format(self.code,self.email)

class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name="标题")
    #这里数据库中存储的是图片的地址
    image = models.ImageField(upload_to="banner/%Y/%m",verbose_name="轮播图")
    url  = models.URLField(max_length=200,verbose_name="访问地址")
    index = models.IntegerField(default=100,verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name




