from django.db import models
from django.contrib.admin.widgets import AdminDateWidget

# Create your models here.

class Student(models.Model):
    unique_id = models.CharField(max_length = 100,unique = True)
    roll_no = models.CharField(max_length = 4, unique = True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    gender = models.CharField(max_length=6)
    email = models.CharField(max_length=255)
    #photo need to create a field for photo upload
    date_of_birth = models.DateField()
    mobile_no = models.CharField(max_length=255)
    hosteler = models.CharField(max_length=255)
    mother_tongue = models.CharField(max_length=255)
    other_languages = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    community = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=255)
    educational_qualification = models.CharField(max_length=255)
    name_of_school_last_studied = models.CharField(max_length=1024)
    neet_marks = models.CharField(max_length=255)
    extracurricular_activities = models.CharField(max_length=1024)
    fathers_name = models.CharField(max_length=255)
    fathers_occupation = models.CharField(max_length=255)
    fathers_mobile = models.CharField(max_length=255)
    mothers_name = models.CharField(max_length=255)
    mothers_occupation = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=1024)
    pincode = models.CharField(max_length=255)
    parents_email = models.CharField(max_length=255)
    

class PracticalInt(models.Model):
    '''
    test_id = 20221111, date in the reverse will be test id
    max_marks = 20 , max_marks for the test
    date_of_conduction = 2022-11-11, date on which the date is conducted
    '''
    test_id = models.CharField(max_length = 50, unique = True)
    max_marks = models.IntegerField()
    date_of_conduction = models.DateField()

class PracticalInternalStudent(models.Model):
    s = models.ForeignKey(Student,on_delete=models.CASCADE,related_name = "student")
    unique_test = models.ForeignKey(PracticalInt,on_delete=models.CASCADE,related_name = "practical_test")
    marks = models.IntegerField()



    





