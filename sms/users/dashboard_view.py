from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import Student, TestType, Test, Batch, AttendanceType 
from .forms import AttendanceTypeForm

# This view is used to display things in the dashboard


def dashboard_theory_grid(request):
    '''
    This dashboard will display all theory marks of all students in a single
    page
    '''
    #Logic
    #First query the TestType Model for the number of theory exams conducted.
    #   So get the number of theory tests conducted,
    #   Get the max marks of each test
    theory_tests = TestType.objects.filter(test_type = 'theory')
    no_of_theory_tests = theory_tests.count()
    print(no_of_theory_tests)
    for i in theory_tests:
        print("id ",i.id, "max_marks ", i.max_marks)
    print(theory_tests)

    students = Student.objects.all().order_by('unique_id')

    marks_dict = {}
    for i in students:
        print("test unique id", i.unique_id)
        theory_tests_of_i = Test.objects.filter(
                                test_type__test_type = 'theory',
                                student_id__unique_id = i.unique_id
                                )
        marks_dict[i] = []

        for j in theory_tests_of_i:
            marks_dict[i].append(j.marks_obtained)
            #print(j.marks_obtained)
    

    print(marks_dict) 
    template = loader.get_template('./dashboard/dashboard_theory.html') 
    context = {}
    context['theory_tests'] = theory_tests 
    context['marks_dict'] = marks_dict
    context['no_of_theory_tests'] = no_of_theory_tests

    return HttpResponse(template.render(context,request))
    


    #Second query the Student Model for the number of students
    #   So get the unique_id, roll_no

    #Third for each student display the marks along a row

    #Finally a dictionary should be created where the key should be the roll_no
    #the firstname, marks of the different tests as data

    pass
