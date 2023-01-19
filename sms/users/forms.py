# Trying out class based models
from django import forms
from django.forms import ModelForm
from django.forms import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
from . import models

class BatchForm(ModelForm):
    class Meta:
        model = models.Batch
        fields = '__all__'


class StudentForm(ModelForm):

    batch = forms.ModelChoiceField(
                            queryset=models.Batch.objects.all(),
                            required=False,
                            blank=True,
                            empty_label="Select a Batch"
                        )
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


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and instance.batch != None:
            print("instance.batch_id = ",instance.batch_id)
            print("i am inside instance")
            #print(models.Batch.objects.get(id=instance.batch_id).batch_name)
            self.fields['batch'].initial = models.Batch.objects.get(
                id = instance.batch.id
            ).batch_name

        else:
            print("i am inside else of studentform")
            #batch = forms.ModelChoiceField(
            #                        queryset=models.Batch.objects.all(),
            #                        blank=True,
            #                        empty_label="Select a Batch"
            #                    )

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


class AttendanceTypeForm(ModelForm):
    batch = forms.ModelChoiceField(
        queryset=models.Batch.objects.all(),
        empty_label='Select a Batch',
        required=False,
        blank=True
    )

    CHOICES = [
        ('theory', 'Theory'),
        ('practical','Practical'),
        ('sdl','SDL'),
        ('ece','ECE'),
        ('aetcom', 'AETCOM'),
              ]
    type_of_class = forms.ChoiceField(choices = CHOICES) 
    
    class Meta:
        model = models.AttendanceType
        fields = '__all__'
        widgets = {
            'date_of_attendance' : AdminDateWidget(
                attrs={'type':'date',}
            ),
        }
    def clean(self):
        cleaned_data = super().clean()
        print(" i am inside clean")
        attendance_type = cleaned_data.get('type_of_class')
        batch = cleaned_data.get('batch')

        class_types_attended_in_batches = [
            'practical',
            'sdl'
        ] 
        print("attendance_type is in list",attendance_type in class_types_attended_in_batches )

        if (attendance_type in class_types_attended_in_batches) and not batch:
            self.add_error('batch','Batch must be selected for this class type')


        
