from django.db import models

# Create your models here.


class test_app(models.Model):
    one = models.CharField(max_length=15,null=True,verbose_name="第一")
    two = models.CharField(max_length=15,null=True,verbose_name="第二")
    three = models.CharField(max_length=15, null=True, verbose_name="第三")

    class Meta:
        # 指明一个易于理解和表述的对象名称，单数形式,
        verbose_name = '测试app'
        # 如果这个值没有设置， Django 将会使用该 model 的类名的分词形式作为他的对象表述名: CamelCase 将会转换为camel case 。
        verbose_name_plural = verbose_name
        db_table = "test_123"#定义该 model 在数据中的表名称: