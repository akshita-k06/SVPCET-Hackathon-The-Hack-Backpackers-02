from django.shortcuts import render
from .models import Complaint_Category,Complaint_Subcategory,Complaint_User
from user.models import Users
# Create your views here.

def user_solver(request):

    complaint_subcategory = Complaint_Subcategory.objects.get(solver_role=request.user.user_role)
    complaint_user = Complaint_User.objects.filter(complaint_subcategory=complaint_subcategory,is_otp_verify=True).all()
    params = {
        'complaint_user':complaint_user,
    } 
    return render(request,'user/user_solver.html',params)