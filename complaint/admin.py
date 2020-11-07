from django.contrib import admin
from .models import Complaint_Category,Complaint_Subcategory
# Register your models here.


class Complaint_SubcategoryAdmin(admin.StackedInline):
    model = Complaint_Subcategory

@admin.register(Complaint_Category)
class Complaint_CategoryAdmin(admin.ModelAdmin):
    inlines = [Complaint_SubcategoryAdmin]
    list_display = ("id","name")
    class Meta:
        model=Complaint_Category


@admin.register(Complaint_Subcategory)
class Complaint_SubcategoryAdmin(admin.ModelAdmin):
    pass