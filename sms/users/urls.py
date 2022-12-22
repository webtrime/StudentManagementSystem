from django.urls import include,path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('student_reg/',views.student_reg,name='student_reg'),
    path('add_user/',views.add_user,name="add_user"),
    path('update_user/',views.update_user,name="update_user"),
    path("accounts/",include("django.contrib.auth.urls")),
    path("dashboard/", views.dashboard, name="dashboard")
]
