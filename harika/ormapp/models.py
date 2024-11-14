from django.db import models
from django.contrib import admin
class Bankloan (models.Model):
    eid=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=100)
    Salary=models.IntegerField()
    Age=models.IntegerField()
    Email=models.EmailField()
 
class LoanAdmin(admin.ModelAdmin):
    list_display=('eid','Name','Salary','Age','Email')

