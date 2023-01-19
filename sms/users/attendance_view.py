from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import Student, Batch, AttendanceType 
from .forms import AttendanceTypeForm

def attendance_grid(request):
    '''
    This displays the attendance grid
    '''
    attendance = AttendanceType.objects.all().order_by('date_of_attendance')
    template = loader.get_template('./attendance/attendance_grid.html')
    context = {
        'attendance' : attendance,
    }
    print("hello")
    print(context['attendance'])
    return HttpResponse(template.render(context,request))
    pass

def enter_attendance_details(request):
    '''
    This view will be called when a new attendance detail has to entered
    '''

    if request.method == 'POST':
        attendance_detail_form = AttendanceTypeForm(request.POST) 
        print("I am inside if post is true ")
        if attendance_detail_form.is_valid():
            print("I am inside forms valid")
            # copy the incoming post data
            attendance_data = request.POST.copy()
            print(attendance_data)
            # pop the 'csrfmiddlewaretoken'
            attendance_data.pop('csrfmiddlewaretoken')
            # convert it to a dictionary to create a Model object
            attendance_data_dict = attendance_data.dict()
            #print("student_data_batch",student_data_dict['batch'])
            print("I am inside add attendance")

            if attendance_data_dict['batch'] == '':
                print(" iam inside if of batch None")
                null_batch = None 
                attendance_data_dict['batch'] = null_batch 
                try:
                    print(attendance_data_dict['batch'])
                except:
                    print("I am inside except")
                attendance = AttendanceType(**attendance_data_dict)
            
            # ** are required to unpack the dictionary
            else:
                attendance_data_dict['batch'] = Batch.objects.get(id=attendance_data_dict['batch'])
                attendance = AttendanceType(**attendance_data_dict)
                #print("batch_id = ",student.batch)

            print("saving to attendance database")
            attendance.save()
            print("saving to attendance database")

            
            return HttpResponseRedirect(reverse(enter_attendance_details))
    else:
        print("i am inside else")
        attendance_detail_form = AttendanceTypeForm()
    print("I am using this attendance_detail_form")
    return render(request,'./attendance/enter_attendance_details.html',{'form':attendance_detail_form})

def update_attendance_details(request,attendance_id):
    '''
    This view willl be callled to update or modify details to already existing
    attendance details
    '''

    attendance = AttendanceType.objects.get(id = attendance_id)

    if (request.method == 'POST'):
        form = AttendanceTypeForm(request.POST, instance = attendance)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(attendance_grid))

    elif (request.method == 'GET'):
        form = AttendanceTypeForm(instance = attendance)
        template = loader.get_template('./attendance/update_attendance_type.html') 
        context = {}
        context['form'] = form
        context['attendance_id'] = attendance_id
        print(context['attendance_id'])
        # if view is called by a get method then call with values from database
        return HttpResponse(template.render(context,request))


def delete_attendance_details(request,attendance_id):
    '''
    This view will be called to delete a particular attendance detail

    '''

    attendance = AttendanceType.objects.get(id = attendance_id)
    attendance.delete()
    return HttpResponseRedirect(reverse(attendance_grid))
    pass
