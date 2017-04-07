from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


from .models import Course

class CourseListView(View):
    def get(self,request):
        all_course = Course.objects.all().order_by("-add_time")

        hot_courses = Course.objects.all().order_by('-click_nums')[:3]

        #课程排序
        sort = request.GET.get('sort',"")
        if sort:
            if sort == "students":
                all_course = all_course.order_by("-students")
            if sort == "hot":
                all_course = all_course.order_by("-click_nums")

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_course, 3, request=request)
        courses = p.page(page)

        return render(request,'course-list.html',{
            "all_course":courses,
            "sort":sort,
            "hot_courses":hot_courses
        })



class CourseDetailView(View):
    """
    课程详情页
    """
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        #增加课程点击数
        course.click_nums += 1
        course.save()

        return render(request,"course-detail.html",{
            'course':course
        })





