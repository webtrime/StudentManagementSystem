from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('student_reg/',views.student_reg)
]
