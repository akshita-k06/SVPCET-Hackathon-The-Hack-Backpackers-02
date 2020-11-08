from django.shortcuts import render,redirect
from complaint.models import Complaint_Category,Complaint_Subcategory,Complaint_User
from django.contrib import messages
from django.db import IntegrityError
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from datetime import datetime,timedelta
import math
import random

# Create your views here.

def index(request):
    complaint_category = Complaint_Category.objects.all()
    params = {
        'complaint_category':complaint_category
    }
    return render(request,'socialShout/index.html',params)

def subproblems(request,mainproblem_name,id):
    complaint_subcategory = Complaint_Subcategory.objects.filter(complaint_category=id).all()
    params = {
        'complaint_subcategory':complaint_subcategory,
    }
    return render(request,'socialShout/subproblems.html',params)

def subproblems_form(request,mainproblem_name,main_id,subproblem_name,sub_id):
    params = {
        'mainproblem_name':mainproblem_name,
        'subproblem_name':subproblem_name,   
        'main_id':main_id,
        'sub_id':sub_id,
    }
    return render(request,'socialShout/problemsform.html',params)

def problems_form_submit(request,main_id,sub_id):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        inputaddress = request.POST['inputaddress']
        email = request.POST['email']
        contactno1 = request.POST['contactno1']
        contactno2 = request.POST.get('contactno2')
        aadharno = request.POST['aadharno']
        pincode = request.POST['pincode']
        inputcity = request.POST['inputcity']
        state = request.POST['state']
        complaint = request.POST.get('complaint')
        upload_file= request.FILES['file1'] if 'file1' in request.FILES else False
        upload_file1= request.FILES['file2'] if 'file2' in request.FILES else False

        digits = [i for i in range(0, 10)]
        random_str = ""
        for i in range(6):
            index = math.floor(random.random() * 10)
            random_str += str(digits[index])
        try:
            send_mail('Verfiy Your Complaint by enter OTP', 
            'Your OTP for Verfiy Your Complaint is '+random_str+'.',
                'admin@psmweb.in',
                [email],
                fail_silently=False)
            cu1= Complaint_User()
            cu1.complaint_category = Complaint_Category(main_id)
            cu1.complaint_subcategory = Complaint_Subcategory(sub_id)
            cu1.full_name =fullname
            cu1.address =  inputaddress
            cu1.email =  email
            cu1.phone =  contactno1
            cu1.alternative_phone =  contactno2
            cu1.aadhar_no =  aadharno
            cu1.pincode =  pincode
            cu1.city =  inputcity
            cu1.state =  state
            cu1.complaint_info =  complaint
            cu1.complaint_aadhar =  upload_file
            cu1.complaint_image =  upload_file1
            cu1.otp_code = random_str
            cu1.otp_created_at = datetime.now()
            cu1.save()
            request.session['complaint_email'] = email
            request.session['complaint__id'] = cu1.id
            messages.success(request,"Email is sucessfully sent")
            return redirect("/verify_otp/")

        except Exception as e:
            messages.error(request, e)
#            problems_form/<str:mainproblem_name>/<int:main_id>/<str:subproblem_name>/<int:sub_id>/
            return redirect("problems_form/mainproblem_name/"+str(main_id)+"/subproblem_name/"+str(sub_id)+"/")
        
        # try:
        #     send_mail('Verfiy Your Complaint by enter OTP', 
        #     'Your OTP for Verfiy Your Complaint is '+random_str+'.',
        #         'admin@psmweb.in',
        #         [email],
        #         fail_silently=False)
        # except Exception as e:
        #     messages.error(request, e)
        #     request.session['complaint_email'] = email
        # return redirect("/verify_otp/"+str(cu1.id)+"/")
    return render(request,'socialShout/otp_verify.html',params)    

def verify_otp(request):
    complaint_email = request.session.get('complaint_email')
    complaint_id = request.session.get('complaint__id')
    if request.method == 'POST':
        otp = request.POST['otp']
        complaint_user = Complaint_User.objects.get(id = complaint_id)
        time_limit =  complaint_user.otp_created_at + timedelta(minutes=10)
        now_time =  datetime.utcnow()
        if complaint_user.otp_created_at >= now_time: 
            if complaint_user.otp_code == otp:
                complaint_user.is_otp_verify = True
                complaint_user.save()
                messages.success(request,"Your complaint is sucessfully registered")
                return redirect("/")
            else:
                messages.error(request, "Plese enter correct otp")
                return redirect("/verify_otp/")
        else:
            messages.error(request, "Your otp is expire")
            return redirect("/verify_otp/")

        complaint_user = Complaint_User.objects.get(id=complaint_id)

    params = {
        'complaint_email':complaint_email,
        'complaint_id':complaint_id,
    } 
    return render(request,'socialShout/otp_verify.html',params)