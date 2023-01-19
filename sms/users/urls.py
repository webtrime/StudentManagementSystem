from django.urls import include,path
from . import views, mark_view, batch_view, attendance_view
from . import dashboard_view

urlpatterns = [

    # paths to view, add, update and delete students
    path('',views.test_student_index,name='student_grid'),
    path('staff_view/',views.test1_student_practical_index,name='staff_view'),
    path('student_reg/',views.student_reg,name='student_reg'),
    path('add_student/',views.add_student,name='add_student'),
    path('update_student_new/<slug:student_id>/',views.update_student_new,name='update_student_new'),
    path('delete/<slug:student_id>/',views.delete_student,name='delete_student'),

    #paths for dashboard
    path('dashboard_theory_grid/',dashboard_view.dashboard_theory_grid,name='dashboard_theory_grid'),

    # paths to view, add, update and delete batches
    path('batch_grid/',batch_view.batch_index, name = 'batch_grid'),
    path('add_batch/', batch_view.add_batch, name= 'add_batch'),
    path('update_batch/<slug:batch_id>/', batch_view.update_batch, name='update_batch'),
    path('delete_batch/<slug:batch_id>/', batch_view.delete_batch, name='delete_batch'),

    path('enter_test_details/',mark_view.enter_test_details, name = 'enter_test_details'),
    path('add_test_details/', mark_view.add_test_details, name = 'add_test_details'),
    path('show_tests/',mark_view.show_tests, name = 'show_tests'),
    path('update_test_details/<int:test_id>/', mark_view.update_test_details, name = 'update_test_details'),
    path('delete_test_details/<int:test_id>/', mark_view.delete_test_details, name = 'delete_test_details'),
    #path('enter_marks_for_all/<int:test_id>/', mark_view.enter_marks_for_all, name = 'enter_marks_for_all'),
    path('enter_marks_for_all_new/<int:test_id>/', mark_view.enter_marks_for_all_new, name = 'enter_marks_for_all_new'),
    path('save_marks/', mark_view.save_marks, name = 'save_marks'),

    path('attendance_grid/',attendance_view.attendance_grid,name='attendance_grid'),
    path('enter_attendance_details/',attendance_view.enter_attendance_details,name ='enter_attendance_details'),
    #path('add_attendance_details/', attendance_view.add_attendance_details,name='add_attendance_details'),
    path('update_attendance_details/<int:attendance_id>/',attendance_view.update_attendance_details,name='update_attendance_details'),
    path('delete_attendance_details/<int:attendance_id>/',attendance_view.delete_attendance_details,name='delete_attendance_details'),

    
]
