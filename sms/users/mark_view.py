from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import Student, TestType, Test
from .forms import TestTypeForm

def enter_test_details(request):
    '''
    To render the form from where the test details are entered
    '''
    if request.method == 'POST':
        test_detail_form = TestTypeForm(request.POST) 
        print("I am inside if post is true ")
        if test_detail_form.is_valid():
            print("I am inside forms valid")
            return HttpResponseRedirect('/thanks/')
    else:
        print("i am inside else")
        test_detail_form = TestTypeForm()
    print("I am using this test_type_form")
    return render(request,'./test/enter_test_details.html',{'form':test_detail_form})

def show_tests(request):
    '''
    To display the tests that were conducted 
    '''
    tests = TestType.objects.all().values()

    template = loader.get_template('./test/test_grid.html')
    context = {
        'tests' : tests,
    }
    print("hello")
    print(context['tests'])
    return HttpResponse(template.render(context,request))
    

def add_test_details(request):
    '''
    to save the test details
    '''
    # copy the incoming post data
    test_data = request.POST.copy()
    # pop the 'csrfmiddlewaretoken'
    test_data.pop('csrfmiddlewaretoken')
    # convert it to a dictionary to create a Model object
    test_data_dict = test_data.dict()
    print(test_data_dict)
    test = TestType(**test_data_dict)

    print("saving to test database")
    test.save()
    print("saving to test database")
    return HttpResponseRedirect(reverse("enter_test_details"))

def update_test_details(request,test_id):
    '''
    Usage: To update a test detail
    '''
    print(" ia m being called")
    test = TestType.objects.get(test_id = test_id)
    if (request.method == 'POST'):
        form = TestTypeForm(request.POST, instance = test)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('show_tests'))

    elif (request.method == 'GET'):
        form = TestTypeForm(instance = test)
        print("I am inside elif")

        template = loader.get_template('./test/update_test.html') 
        context = {}
        context['form'] = form
        context['test'] = test 
        # if view is called by a get method then call with values from database

        return HttpResponse(template.render(context,request))

def delete_test_details(request,test_id):
    '''
    To delete a test
    '''
    test = TestType.objects.get(test_id = test_id)
    test.delete()
    return HttpResponseRedirect(reverse('show_tests'))

def enter_marks_for_all(request,test_id):
    #get the details of the test "test_id"

    test_details = TestType.objects.get(test_id = test_id)
    students = Student.objects.all()

    template = loader.get_template('./test/enter_marks_for_all.html')
    print("enter_marks_for_all")
    context = {
        'test_details' : test_details,
        'students' : students,
    }

    return HttpResponse(template.render(context,request))

def save_marks(request):

    mark_data = request.POST.copy()
    # pop the 'csrfmiddlewaretoken'
    mark_data.pop('csrfmiddlewaretoken')
    # convert it to a dictionary to create a Model object


    # Get the values for each key
    marks = mark_data.getlist('mark')
    student_ids = mark_data.getlist('student_id')
    test_ids = mark_data.getlist('test_id')
    # Zip the lists together and iterate over the resulting tuples
    for mark, student, test_id in zip(marks, student_ids, test_ids):
        # Create an instance of the 'TestResult' model

        # check if the instance for the particular student_id and test_type is
        # present
        print("I am trying to update")
        test_student = Test.objects.filter(
            student_id = Student.objects.get(unique_id = student),
            test_type = TestType.objects.get(test_id = test_id)
        ).first()
        print(test_student)

        # if there are no matching instances then create a new record
        if test_student == None: 
            Test.objects.create(
                marks_obtained = mark,
                student_id = Student.objects.get(unique_id = student),
                test_type = TestType.objects.get(test_id = test_id)
            )
        # if there is an instance like this
        else:
            test_student_id = test_student.id
            row = Test.objects.get(id = test_student_id)
            row.marks_obtained = mark
            row.save()


    print("saved_data")
    
    test_table_values = Test.objects.all().values()
    print(test_table_values)
    

    return HttpResponseRedirect(reverse('show_tests'))

def update_marks(request):
    '''
    Use this function to update the marks if they are already present
    '''
    pass 

def enter_marks_for_all_new(request,test_id):
    #get the details of the test "test_id"

    test_details = TestType.objects.get(test_id = test_id)

    students = Student.objects.all()
    # filter the test_marks which are for a particular test
    test_marks = Test.objects.filter(test_type = test_details).values()

    context = {
        'test_details' : test_details,
        'students' : students,
    }

    combined_lists = zip(students,test_marks)

    # if atleast one instance is present in the Test Table then update the
    # marks for the test
    if test_marks.exists(): 
        #context['blank'] = False
        context['combined_lists'] = combined_lists
        template = loader.get_template('./test/enter_or_update_marks_for_all.html')
        #print(context['test_marks'])
        print(context['combined_lists'])
        print(context['test_details'])
        print("Inside update marks")
    else:
        #context['blank'] = True
        template = loader.get_template('./test/enter_marks_for_all.html')
        print("enter_marks_for_all")

    return HttpResponse(template.render(context,request))



        

