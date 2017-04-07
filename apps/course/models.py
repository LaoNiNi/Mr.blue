from django.db import models
from datetime import datetime

from oraganization.models import CourseOrg
# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg,verbose_name="课程机构",null=True,blank=True)
    name = models.CharField(max_length=50,verbose_name="课程名")
    desc = models.CharField(max_length=300,verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")
    degree = models.CharField(verbose_name='难度',max_length=5,choices=(("cj","初级"),("zj","中级"),("gj","高级")))
    learn_times = models.IntegerField(default=0,verbose_name="学习时长(分钟数)")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0,verbose_name="收藏人数")
    image = models.ImageField(upload_to="course/%Y/%m",verbose_name="封面图",max_length=100)
    click_nums = models.IntegerField(default=0,verbose_name="点击数")
    category = models.CharField(default="后端开发",max_length=20, verbose_name="课程类别")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_zj_nums(self):
        #获取章节数目
        return self.lesson_set.all().count()

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]


class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name="课程")
    name = models.CharField(max_length=100,verbose_name="章节名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name




class Video(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name="章节")
    name = models.CharField(max_length=100,verbose_name="视频名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course,verbose_name="课程")
    name = models.CharField(max_length=100,verbose_name="名称")
    download = models.FileField(upload_to="course/%Y/%m",verbose_name="资源文件",max_length=100)
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

