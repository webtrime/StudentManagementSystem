from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Student
from .models import PracticalInternalStudent 
from .models import PracticalInt
from .forms import StudentForm 
from .forms import AddPracticalMarks
from .forms import PracticalInternalForm 

def test_index(request):
    my_users = Users.objects.all().values()
    template = loader.get_template('users_index.html')
    context = {
        'my_users' : my_users,
    }
    return HttpResponse(template.render(context,request))

def add_user(request):
    roll_no = request.POST['roll_no']
    first_name = request.POST['first_name']    
    lastname = request.POST['lastname']
    gender = request.POST['gender']
    email = request.POST['email']
    #photo need to create a field for photo upload
    date_of_birth = request.POST['date_of_birth']
    mobile_no = request.POST['mobile_no']
    hosteler = request.POST['hosteler']
    mother_tongue = request.POST['mother_tongue']
    other_languages = request.POST['other_languages']
    nationality = request.POST['nationality']
    community = request.POST['community']
    blood_group = request.POST['blood_group']
    educational_qualification = request.POST['educational_qualification']
    name_of_school_last_studied = request.POST['name_of_school_last_studied']
    neet_marks = request.POST['neet_marks']
    extracurricular_activities = request.POST['extracurricular_activities']
    fathers_name = request.POST['fathers_name']
    fathers_occupation = request.POST['fathers_occupation']
    fathers_mobile = request.POST['fathers_mobile']
    mothers_name = request.POST['mothers_name']
    mothers_occupation = request.POST['mothers_occupation']
    permanent_address = request.POST['permanent_address']
    pincode = request.POST['pincode']
    parents_email = request.POST['parents_email']
    user = Users(
        roll_no = roll_no,
        firstname = first_name,    
        lastname = lastname,
        gender = gender,
        email = email,
        #photo need to create a field for photo upload
        date_of_birth = date_of_birth,
        mobile_no = mobile_no,
        hosteler = hosteler,
        mother_tongue = mother_tongue,
        other_languages = other_languages,
        nationality = nationality,
        community = community,
        blood_group = blood_group,
        educational_qualification = educational_qualification,
        name_of_school_last_studied = name_of_school_last_studied,
        neet_marks = neet_marks,
        extracurricular_activities = extracurricular_activities,
        fathers_name = fathers_name,
        fathers_occupation = fathers_occupation,
        fathers_mobile = fathers_mobile,
        mothers_name = mothers_name,
        mothers_occupation = mothers_occupation,
        permanent_address = permanent_address,
        pincode = pincode,
        parents_email = parents_email
    ) 
    user.save()
    print("hello i am add_user")
    return HttpResponseRedirect(reverse("student_reg"))

def test_student_index(request):
    students = Student.objects.all().values()
    template = loader.get_template('students_index.html')
    context = {
        'students' : students,
    }
    print("hello")
    print(context['students'])
    return HttpResponse(template.render(context,request))

def test_student_practical_index(request):
    marks = PracticalInternalStudent.objects.all()
    student = Student.objects.all()
    template = loader.get_template('students_marks_practical_index.html')
    context = {
        'marks': marks,
        'student' : student,
    }
    print(context['student'])
    return HttpResponse(template.render(context,request))


def test1_student_practical_index(request):
    '''
    This view is created to check if multiple table values especially related
    ones are able to be displayed in a grid
    '''
    # Here we are planning to display all the test marks of all 
    # student

    # So all student unique_id, roll_no and names are to be collected
    # I have come with my work around, however should ask somebody with
    # experience

    # Final dict should be of the form
    # student = {
    #               unique_id : {
    #
        #               'name': student_name, 
        #               'roll_no': roll_no,
        #               'marks':{
        #                           test_id_1:[max_marks,marks_obtained],
        #                           test_id_2:[max_marks,marks_obtained]
        #                       } 
        #
        #                }

    #           }

    # first create a empty dictionary
    students = {}
    # get all the unique_id of all students
    all_student_data = Student.objects.all().order_by('unique_id')
    all_prac_test_data = PracticalInt.objects.all().order_by('test_id') 


    for i in all_student_data:
        student_prac_test_data = PracticalInternalStudent.objects.filter(s__unique_id=i.unique_id)
        print(student_prac_test_data)
        marks = {}
        for j in student_prac_test_data:
            marks[j.unique_test.test_id] = [j.unique_test.max_marks,j.marks]

        students[i.unique_id] = {
                                    'name': i.firstname,
                                    'roll_no' : i.roll_no,
                                    'marks' : marks,
                                }
    #print(students)

    template = loader.get_template('test_grid_display.html')
    context = {
        'practical_test_data' : all_prac_test_data,
        'students' : students,
    }
    print(context['students'])
    return HttpResponse(template.render(context,request))

# Create your views here.

def student_reg(request):
    '''
    Usage : to render a form where a student detail can be entered
    '''

    if request.method == 'POST':
        form = StudentForm(request.POST) 
        print("I am inside if post is true ")
        if form.is_valid():
            print("I am inside forms valid")
            return HttpResponseRedirect('/thanks/')
    else:
        print("i am inside else")
        form = StudentForm()
    print("I am using this student_reg")
    return render(request,'stu_reg_form.html',{'form':form})

def add_student(request):
    '''
    Usage: To save the student details to a form
    '''
    # copy the incoming post data
    student_data = request.POST.copy()
    # pop the 'csrfmiddlewaretoken'
    student_data.pop('csrfmiddlewaretoken')
    # convert it to a dictionary to create a Model object
    student_data_dict = student_data.dict()
    print(student_data_dict)
    
    # ** are required to unpack the dictionary

    student = Student(**student_data_dict)

    print("saving to student database")
    student.save()
    print("saving to student database")
    return HttpResponseRedirect(reverse("student_reg"))


def update_student_new(request,student_id):
    '''
    Usage: To update a student detail
    '''
    student = Student.objects.get(unique_id = student_id)

    if (request.method == 'POST'):

        form = StudentForm(request.POST, instance = student)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student_grid'))
        
        # update the record and goto users page again
        #print(request.POST)
        #post_data = request.POST.copy()
        #post_data.pop('csrfmiddlewaretoken')
        #updated_student_values = post_data.dict()  
        #print(updated_student_values)
        #print("updated_student_values")
        #print(type(updated_student_values))

        # remove the csrfmiddlewaretoken field from the dictionary
        # print(updated_student_values)
        #print(type(updated_student_values))

        # student = Student(**updated_student_values)
        # student.save(force_update = True)

        # return HttpResponseRedirect(reverse('index')) 

    elif (request.method == 'GET'):

        form = StudentForm(instance = student)

        template = loader.get_template('update_student.html') 
        context = {}
        context['form'] = form
        context['student'] = student
        # if view is called by a get method then call with values from database

        return HttpResponse(template.render(context,request))

def delete_student(request,student_id):
    '''
    Usage: To delete a student from the table
    '''
    student = Student.objects.get(unique_id = student_id)
    student.delete()
    return HttpResponseRedirect(reverse('student_grid'))

def enter_prac_marks(request):
    '''
    Usage : To render a 2 form from where test details and marks of all
    students can be entered 
    This view will be called to render the entry form for a single practical
    test

    # call the Student table and get the students
    # practical test details form from forms.py

    '''
    practical_test_details_form = PracticalInternalForm() 
    students = Student.objects.all().order_by('unique_id')
    #print('show student')
    #print(students)
    context = {
        'students': students,
        'test_details_form' : practical_test_details_form,
    }

    template = loader.get_template('practical_marks_entry_all.html')
    return HttpResponse(template.render(context,request))



    # call the 

    pass

def save_prac_marks(request):
    '''
    This view will be called to save the practical marks

    # the post data contains data for 2 models 1 for PracticalInt and another
    # for PracticalInternalStudent 
    # since data is supposed to go to 2 tables, need to decide on how the post
    # data is going to come, 
    #   - Should I use javascript on the front end to convert it to a json file
    #   and send 
    #   - Or should I use dynamically generated form field ids and process it
    #   here


    '''

    pass


def update_user(request,id):
    user = Users.objects.get(id=id)
    template = loader.get_template('update_student.html')
    context = {
        'user' : user,
    }
    return HttpResponse(template.render(context,request))

def dashboard(request):
    return render(request, "users/dashboard.html")


def student_profile_update(request):
    #this is the view that will be called when a student wants to update his
    # profile
    unique_id = request.POST['unique_id']
    roll_no = request.POST['roll_no']
    first_name = request.POST['first_name']    
    lastname = request.POST['lastname']
    gender = request.POST['gender']
    email = request.POST['email']
    #photo need to create a field for photo upload
    date_of_birth = request.POST['date_of_birth']
    mobile_no = request.POST['mobile_no']
    hosteler = request.POST['hosteler']
    mother_tongue = request.POST['mother_tongue']
    other_languages = request.POST['other_languages']
    nationality = request.POST['nationality']
    community = request.POST['community']
    blood_group = request.POST['blood_group']
    educational_qualification = request.POST['educational_qualification']
    name_of_school_last_studied = request.POST['name_of_school_last_studied']
    neet_marks = request.POST['neet_marks']
    extracurricular_activities = request.POST['extracurricular_activities']
    fathers_name = request.POST['fathers_name']
    fathers_occupation = request.POST['fathers_occupation']
    fathers_mobile = request.POST['fathers_mobile']
    mothers_name = request.POST['mothers_name']
    mothers_occupation = request.POST['mothers_occupation']
    permanent_address = request.POST['permanent_address']
    pincode = request.POST['pincode']
    parents_email = request.POST['parents_email']
    student = Student(
        unique_id = unique_id,
        roll_no = roll_no,
        firstname = first_name,    
        lastname = lastname,
        gender = gender,
        email = email,
        #photo need to create a field for photo upload
        date_of_birth = date_of_birth,
        mobile_no = mobile_no,
        hosteler = hosteler,
        mother_tongue = mother_tongue,
        other_languages = other_languages,
        nationality = nationality,
        community = community,
        blood_group = blood_group,
        educational_qualification = educational_qualification,
        name_of_school_last_studied = name_of_school_last_studied,
        neet_marks = neet_marks,
        extracurricular_activities = extracurricular_activities,
        fathers_name = fathers_name,
        fathers_occupation = fathers_occupation,
        fathers_mobile = fathers_mobile,
        mothers_name = mothers_name,
        mothers_occupation = mothers_occupation,
        permanent_address = permanent_address,
        pincode = pincode,
        parents_email = parents_email
    ) 
    student.save()
    return HttpResponseRedirect(reverse("student_reg"))

def enter_student_mark_practical(request):

    if request.method == 'POST':
        form = StudentForm(request.POST) 
        print("I am inside if post is true ")
        if form.is_valid():
            print("I am inside forms valid")
            return HttpResponseRedirect('/thanks/')
    else:
        print("i am inside else")
        form = AddPracticalMarks()
    print("Add practical marks of a student")
    return render(request,'add_student_mark_practical.html',{'form':form})


def add_student_mark_practical(request):

    s = request.POST['unique_id']
    unique_test = request.POST['unique_test_id']
    marks = request.POST['marks']

    unique_id = Student.objects.get(unique_id = s)
    unique_test_id = PracticalInt.objects.get(test_id = unique_test)

    studentPracticalMark = PracticalInternalStudent(
        s = unique_id,
        unique_test = unique_test_id,
        marks = marks,
    )
    #studentPracticalMark = PracticalInternalStudent(
    #    unique_id = unique_id,
    #    unique_test_id = unique_test_id,
    #    marks = marks,
    #)
    studentPracticalMark.save()
    return HttpResponseRedirect(reverse('enter_student_mark_practical'))

def enter_practical_test_details(request):
    if request.method == 'POST':
        form = PracticalInternalForm(request.POST) 
        print("I am inside if post is true ")
        if form.is_valid():
            print("I am inside forms valid")
            return HttpResponseRedirect('/thanks/')
    else:
        print("i am inside else enter_practical_test_details")
        form = PracticalInternalForm()
    print("Add practical marks of a student")
    return render(request,'add_practical_test_details.html',{'form':form})

def add_practical_test_details(request):
    test_id = request.POST['test_id']
    max_marks = request.POST['max_marks']
    date_of_conduction = request.POST['date_of_conduction']
    print("hello")


    practical_test_details = PracticalInt(
        test_id = test_id,
        max_marks = max_marks,
        date_of_conduction = date_of_conduction,
    )
    practical_test_details.save()
    return HttpResponseRedirect(reverse('enter_practical_test_details'))




def student_view_marks_attendance(request,unique_id):
    student = Student.objects.get(unique_id=unique_id)
    template = loader.get_template(name="show_marks_attendance.html")
    context = {
        'student' : student,
    }

    return HttpResponse(template.render(context,request))




    

