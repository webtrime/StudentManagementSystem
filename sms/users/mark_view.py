from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Student, TestType
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
    print(request.POST)
    context = {

    }

    return HttpResponseRedirect(reverse('show_tests'))

    pass


