from django.contrib import admin
from django.urls import path

from exam import views as exam_view
from student import views as s_v

urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        exam_view.test
    ),

    path(
        'api/students/',
        s_v.get_students
    ),

    path(
        'api/add/',
        s_v.add_student
    ),

    path(
        'api/update/<int:id>/',
        s_v.update_student
    ),

    path(
        'api/delete/<int:id>/',
        s_v.delete_student
    ),

]