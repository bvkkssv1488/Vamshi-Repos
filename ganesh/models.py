from django.db import models
class Donation(models.Model):

  Gothram= models.CharField(max_length=500)
  LastName= models.CharField(max_length=500)
  FirstName= models.CharField(max_length=500)
  SpouceName= models.CharField(max_length=500)
  Child1= models.CharField(max_length=500)
  Child2=models.CharField(max_length=500)
  Amount=models.IntegerField()
  class Meta:
    db_table="ganesh_donation"

class Poojaevents(models.Model):

  Gotram= models.CharField(max_length=500)
  SurName= models.CharField(max_length=500)
  Name= models.CharField(max_length=500)
  SpouseName= models.CharField(max_length=500)
  Date=models.DateField(auto_now=False)
  Time=models.CharField(max_length=500,default='Morning')
  class Meta:
    db_table="ganesh_poojaevents"


