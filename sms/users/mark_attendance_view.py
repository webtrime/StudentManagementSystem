from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import Student, Batch, AttendanceType 
from .forms import AttendanceTypeForm

def show_attendance_register(request):
    '''
    This view will display the attendance register
    If the attendance Type was "Theory" or "AETCOM" or "ECE" then all the students should be shown
    as a list
    If the attendance Type was "practical" or "sdl" then the students of that
    particular batch should be displayed
    On the display the following should be shown, Roll No, Student name, and
    the students presence (check box by default will be marked present)
    '''


