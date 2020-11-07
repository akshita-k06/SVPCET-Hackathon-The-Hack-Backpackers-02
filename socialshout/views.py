from django.shortcuts import render
from complaint.models import Complaint_Category,Complaint_Subcategory
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
    }
    return render(request,'socialShout/problemsform.html',params)

def problems_form_submit(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        inputaddress = request.POST['inputaddress']
        email = request.POST['email']
        contactno1 = request.POST['contactno1']
        contactno2 = request.POST.get('contactno2')
        aadharno = request.POST['aadharno']
        pincode = request.POST['pincode']
        inputcity = request.POST['inputcity']
        password = request.POST['state']
        password = request.POST.get('complaint')
        upload_file= request.FILES['file1'] if 'file' in request.FILES else False
        upload_file= request.FILES['file1'] if 'file' in request.FILES else False



    return render(request,'socialShout/otp_verify.html',params)    

def verify_otp(request):
    params = {

    }
    return render(request,'socialShout/otp_verify.html',params)