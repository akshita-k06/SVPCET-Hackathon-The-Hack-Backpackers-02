

from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('subproblems/<str:mainproblem_name>/<int:id>/', views.subproblems, name="subproblems"),
    path('problems_form/<str:mainproblem_name>/<int:main_id>/<str:subproblem_name>/<int:sub_id>/', views.subproblems_form, name="subproblems_form"),
    path('verify_otp/', views.verify_otp, name="verify_otp"),
    path('problems_form_submit/<int:main_id>/<int:sub_id>/', views.problems_form_submit, name="problems_form_submit"),

]
