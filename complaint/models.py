from django.db import models

# Create your models here.



class Complaint_Category(models.Model):
    name = models.CharField(max_length=100,default=None,blank=True,null=True)    
    def __str__(self):
        return str(self.id)+" - "+self.name

class Complaint_Subcategory(models.Model):
    complaint_category = models.ForeignKey(Complaint_Category,default=None,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default=None,blank=True,null=True)
    priority = models.SmallIntegerField(default=1,blank=True,null=True)
    
    def __str__(self):
        return str(self.id)+" - "+self.name
