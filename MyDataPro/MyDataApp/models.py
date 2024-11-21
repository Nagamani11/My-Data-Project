from django.db import models
class MyData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    mobile_number = models.IntegerField()
    email_id = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    percentage = models.IntegerField()
    passed_out_year = models.IntegerField()
    college_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
