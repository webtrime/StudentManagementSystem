from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Users
from .forms import StudentForm 

def index(request):
    my_users = Users.objects.all().values()
    template = loader.get_template('users_index.html')
    context = {
        'my_users' : my_users,
    }
    return HttpResponse(template.render(context,request))

# Create your views here.

def student_reg(request):
    if request.method == 'POST':
        form = StudentForm(request.POST) 
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = StudentForm()
    return render(request,'student_reg_form.html',{'form':form})


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
    return HttpResponseRedirect(reverse("student_reg"))

def update_user(request,id):
    user = Users.objects.get(id=id)
    template = loader.get_template('update_student.html')
    context = {
        'user' : user,
    }
    return HttpResponse(template.render(context,request))

def dashboard(request):
    return render(request, "users/dashboard.html")
    
