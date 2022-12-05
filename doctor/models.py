from django.db import models

# Create your models here.



class doctor(models.Model):
    did = models.CharField(max_length=9,null=False)
    username = models.CharField(max_length=9,null=False)
    password = models.CharField(max_length=9,null=False)


class client(models.Model):
    did = models.CharField(max_length=9,null=False)
    name = models.CharField(max_length=15,null=False)
    age = models.SmallIntegerField(null=False)
    gender = models.CharField(max_length=5,null=False,default="male")
    WBC=models.CharField(max_length=5,null=False,default=" ")
    Neut=models.CharField(max_length=2 ,null=False ,default=" ")
    Lymph=models.CharField(max_length=2,null=False,default=" ")
    RBC=models.FloatField(max_length=5,null=False)
    HCT=models.CharField(max_length=2,null=False ,default=" ")
    Urea=models.CharField(max_length=2,null=False ,default=" ")
    HB=models.FloatField(max_length=4,null=False)
    Creatinine= models.FloatField(max_length=4,null=False,default=1.5)
    Iron=models.CharField(max_length=3,null=False,default=" ")
    HDL= models.CharField(max_length=3,null=False,default=" ")
    q1 = models.CharField(max_length=3,null=False)
    q2 = models.CharField(max_length=3,null=False)
    q3 = models.CharField(max_length=3,null=False)
    condition=models.CharField(max_length=3,null=False,default=" ")