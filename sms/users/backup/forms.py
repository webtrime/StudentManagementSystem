
from django import forms

class StudentForm(forms.Form):
    unique_id = forms.CharField(label="UniqueId",max_length=50)
    roll_no = forms.CharField(label='RollNo',max_length=4)
    firstname = forms.CharField(label='Firstname',max_length=100)
    lastname = forms.CharField(label='Lastname',max_length=255)
    gender = forms.CharField(label='gender',max_length=6)
    email = forms.CharField(label='email',max_length=255)
    #photo need to create a field for photo upload
    date_of_birth = forms.CharField(label='date_of_birth', max_length=255)
    mobile_no = forms.CharField(label='mobile_no',max_length=255)
    hosteler = forms.CharField(label='hosteler',max_length=255)
    mother_tongue = forms.CharField(label='mother_tongue',max_length=255)
    other_languages = forms.CharField(label='other_languages',max_length=255)
    nationality = forms.CharField(label='nationality',max_length=255)
    community = forms.CharField(label='community',max_length=255)
    blood_group = forms.CharField(label='blood_group',max_length=255)
    educational_qualification = forms.CharField(label='educational_qualification',max_length=255)
    name_of_school_last_studied = forms.CharField(label='name_of_school_last_studied',max_length=1024)
    neet_marks = forms.CharField(label='neet_marks',max_length=255)
    extracurricular_activities = forms.CharField(label='extracurricular_activities',max_length=1024)
    fathers_name = forms.CharField(label='fathers_name',max_length=255)
    fathers_occupation = forms.CharField(label='fathers_occupation',max_length=255)
    fathers_mobile = forms.CharField(label='fathers_mobile',max_length=255)
    mothers_name = forms.CharField(label='mothers_name',max_length=255)
    mothers_occupation = forms.CharField(label='mothers_occupation',max_length=255)
    permanent_address = forms.CharField(label='permanent_address',max_length=1024)
    pincode = forms.CharField(label='pincode',max_length=255)
    parents_email = forms.CharField(label='parents_email',max_length=255)

class PracticalInternal(forms.Form):
    test_id = forms.CharField(label='test_id',max_length=100)
    max_marks = forms.CharField(label="max_marks",max_length=100)
    date_of_conduction = forms.DateField()

class AddPracticalMarks(forms.Form):
    unique_id = forms.CharField(label="unique_id",max_length=50)
    unique_test_id = forms.CharField(label="unique_test_id",max_length=50)
    marks = forms.CharField(label="mark_obtained",max_length=100)
    

