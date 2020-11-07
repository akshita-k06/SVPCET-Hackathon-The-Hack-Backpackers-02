

from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('subproblems/<str:mainproblem_name>/<int:id>/', views.subproblems, name="subproblems"),
    path('problems_form/<str:mainproblem_name>/<int:main_id>/<str:subproblem_name>/<int:sub_id>/', views.subproblems_form, name="subproblems_form"),
]
