from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
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


