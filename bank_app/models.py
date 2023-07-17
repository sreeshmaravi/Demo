from django.db import models
 
class District(models.Model):
    name = models.CharField(max_length=40)
 
    def __str__(self):
        return self.name
 
class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
 
    def __str__(self):
        return self.name

 
class Member(models.Model):
    name = models.CharField(max_length=124)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    account_type = models.CharField(max_length=20)
    materials_required = models.TextField(max_length=100)
    def __str__(self):
        return self.name