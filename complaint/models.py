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
    solver_role = models.SmallIntegerField(default=1,blank=True,null=True)
    
    def __str__(self):
        return str(self.id)+" - "+self.name


'''
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    alternative_phone = models.CharField(max_length=15, blank=True, null=True)
    aadhar_no = models.CharField(max_length=15,unique=True,default=None)
    user_role = models.SmallIntegerField(default=0) 
    is_active = models.BooleanField(default=False) 
    is_admin = models.BooleanField(default=False)
    otp_code = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True,null=True)
    no_of_complaint =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    upload_aadhar = models.FileField(upload_to="user_files")
    upload_id = models.FileField(upload_to="user_files")
'''

class Complaint_User(models.Model):
    complaint_category = models.ForeignKey(Complaint_Category,default=None,on_delete=models.CASCADE)
    complaint_subcategory = models.ForeignKey(Complaint_Subcategory,default=None,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250, default=None)
    complaint_info = models.TextField(default=None,blank=True,null=True)
    email = models.CharField(max_length=250, default=None)
    address = models.CharField(max_length=5000, default=None)
    phone = models.CharField(max_length=15, blank=True, null=True)
    alternative_phone = models.CharField(max_length=15, blank=True, null=True)
    aadhar_no = models.CharField(max_length=15,default=None)
    pincode = models.CharField(max_length=10, default=None)
    city = models.CharField(max_length=50, default=None)
    state = models.CharField(max_length=50, default=None)
    complaint_aadhar = models.ImageField(upload_to="complaint_aadhar")
    complaint_image = models.ImageField(upload_to="complaint_image")
    created_at = models.DateTimeField(auto_now_add=True)
    is_otp_verify = models.BooleanField(default=False)
    otp_code = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)+" - "+self.full_name
