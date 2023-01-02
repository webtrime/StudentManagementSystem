# Trying out class based models
from django import forms
from django.forms import ModelForm
from django.forms import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
from . import models

class StudentForm(ModelForm):
    class Meta:
        model = models.Student
        fields = '__all__'
        #the * operator unpacks the range now
        years = [*range(1900,2100,1)]
        # you may need it here
        # https://simpleisbetterthancomplex.com/tutorial/2019/01/03/how-to-use-date-picker-with-django.html
        # https://www.youtube.com/watch?v=1IP7Vkwhb_A
        # the following post helped me render the calendar widget in my
        # student_reg page
        # https://stackoverflow.com/questions/66258610/django-admindatewidget-apprearing-as-textinput/68468821#68468821
        # It is found in
        # https://docs.djangoproject.com/en/4.1/ref/forms/widgets/ under
        # styling-widget-instances
        widgets = {
            'date_of_birth' : AdminDateWidget(
                attrs={'type':'date',}
            ),
        }

class PracticalInternalForm(ModelForm):
    class Meta:
        model = models.PracticalInt
        fields = '__all__'

    #test_id = forms.CharField(label='test_id',max_length=100)
    #max_marks = forms.CharField(label="max_marks",max_length=100)
    #date_of_conduction = forms.DateField()

class AddPracticalMarks(forms.Form):
    unique_id = forms.CharField(label="unique_id",max_length=50)
    unique_test_id = forms.CharField(label="unique_test_id",max_length=50)
    marks = forms.CharField(label="mark_obtained",max_length=100)
    

