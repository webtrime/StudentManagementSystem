from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('student_reg/',views.student_reg,name='student_reg'),
    path('add_user/',views.add_user,name="add_user")
]
