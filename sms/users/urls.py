from django.urls import include,path
from . import views, mark_view

urlpatterns = [
    # paths to view, add, update and delete students
    path('',views.test_student_index,name='student_grid'),
    path('staff_view/',views.test1_student_practical_index,name='staff_view'),
    path('student_reg/',views.student_reg,name='student_reg'),
    path('add_student/',views.add_student,name='add_student'),
    path('update_student_new/<slug:student_id>/',views.update_student_new,name='update_student_new'),
    path('delete/<slug:student_id>/',views.delete_student,name='delete_student'),

    path('enter_test_details/',mark_view.enter_test_details, name = 'enter_test_details'),
    path('add_test_details/', mark_view.add_test_details, name = 'add_test_details'),
    path('show_tests/',mark_view.show_tests, name = 'show_tests'),
    path('update_test_details/<int:test_id>/', mark_view.update_test_details, name = 'update_test_details'),
    path('delete_test_details/<int:test_id>/', mark_view.delete_test_details, name = 'delete_test_details'),
    path('enter_marks_for_all/<int:test_id>/', mark_view.enter_marks_for_all, name = 'enter_marks_for_all'),
    path('save_marks/', mark_view.save_marks, name = 'save_marks')

    
]
