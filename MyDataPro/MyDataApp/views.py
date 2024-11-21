from django.shortcuts import render
from .models import MyData
def mydata(request):
    if request.method == 'GET':
        return render(request, 'mydata.html')
    else:
        fname1 = request.POST.get('fname')
        lname1 = request.POST.get('lname')
        age1 = request.POST.get('age')
        mobile_number1 = request.POST.get('mobile')
        email_id1 = request.POST.get('email')
        qualification1 = request.POST.get('qualification')
        percentage1 = request.POST.get('percentage')
        passed_out_year1 = request.POST.get('passedoutyear')
        college_name1 = request.POST.get('college')
        location1 = request.POST.get('location')
        MyData(
            first_name = fname1,
            last_name = lname1,
            age = age1,
            mobile_number = mobile_number1,
            email_id = email_id1,
            qualification = qualification1,
            percentage = percentage1,
            passed_out_year = passed_out_year1,
            college_name = college_name1,
            location = location1
        ).save()
        return render(request, 'mydata.html')
