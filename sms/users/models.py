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

class TestType(models.Model):
    '''
    A base class for the tests
    test_id = a unique id that represents the test
    test_type = the type of test , theory, practical, viva
    date_of_conduction = some date on which the test was conducted
    max_marks = the max marks that the student can score in that test
    '''
    test_id = models.CharField(max_length = 50, unique = True)
    test_type = models.CharField(max_length = 50)
    max_marks = models.PositiveIntegerField()
    date_of_conduction = models.DateField()

class Tests(models.Model):
    '''
    student_id = a foreign key that references to the student Table
    test_type = a foreign key that references to the TestType Table
    marks_obtained = marks obtained by the student
    '''
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE,related_name = "student")
    test_type = models.ForeignKey(TestType,on_delete=models.CASCADE,related_name = "type_of_test")
    marks_obtained = models.IntegerField()

    



    





