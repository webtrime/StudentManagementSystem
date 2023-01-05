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

class TestTypeForm(ModelForm):
    CHOICES = [
        ('theory', 'Theory'),
        ('practical','Practical'),
        ('viva','Viva')
              ]
    test_type = forms.ChoiceField(choices = CHOICES) 
    
    class Meta:
        model = models.TestType
        fields = '__all__'
        widgets = {
            'date_of_conduction' : AdminDateWidget(
                attrs={'type':'date',}
            ),
        }



