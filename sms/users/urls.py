from django.urls import include,path
from . import views

urlpatterns = [
    path('',views.test_student_index,name='index'),
    path('staff_view/',views.test1_student_practical_index,name='staff_view'),
    path('student_reg/',views.student_reg,name='student_reg'),
    path('add_student/',views.add_student,name='add_student'),
    path('update_student/<slug:student_id>/',views.update_student,name = 'update_student'),
    path('students_marks_practical_index/',views.test_student_practical_index,name='students_marks_practical_index'),
    path('enter_student_mark_practical/',views.enter_student_mark_practical,name='enter_student_mark_practical'),
    path('add_student_mark_practical/',views.add_student_mark_practical,name='add_student_mark_practical'),

    path('enter_practical_test_details/',views.enter_practical_test_details,name='enter_practical_test_details'),
    path('add_practical_test_details/',views.add_practical_test_details,name='add_practical_test_details'),

    path('add_user/',views.add_user,name="add_user"),
    path('update_user/',views.update_user,name="update_user"),
    path("accounts/",include("django.contrib.auth.urls")),
    path("dashboard/", views.dashboard, name="dashboard")
]
