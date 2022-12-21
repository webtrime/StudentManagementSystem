from django.db import models

# Create your models here.
class Users(models.Model):
    roll_no = models.CharField(max_length=4)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    gender = models.CharField(max_length=6)
    email = models.CharField(max_length=255)
    #photo need to create a field for photo upload
    date_of_birth = models.CharField(max_length=255)
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



