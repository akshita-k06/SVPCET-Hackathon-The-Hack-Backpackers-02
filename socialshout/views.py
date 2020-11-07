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
