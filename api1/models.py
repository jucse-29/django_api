from django.db import models

#creating company model
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=58)
    location=models.CharField(max_length=200)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('it','it'),
                                                  ('non it','non it'),
                                                  ('cloth','cloth')))
    added_date=models.DateTimeField(auto_now=True)
    active =models.BooleanField(default=True)
    def __str__(self):
        return self.name +'--'+ self.location
    
    #employee model
class Employee(models.Model):
     name=models.CharField(max_length=100)
     email=models.EmailField(max_length=100)
     address=models.CharField(max_length=100)
     phone=models.CharField(max_length=100)
     about=models.TextField()
     position=models.CharField(max_length=50,choices=(
         ('Manager','manager'),
         ('Software Developer','sd'),
         ('Project Leader','pl')
     ))
     
     company=models.ForeignKey(Company, on_delete=models.CASCADE)
     
        
        