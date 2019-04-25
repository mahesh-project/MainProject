from django.db import models
#from django import forms

# Create your models here.
class tbl_business(models.Model):
    Name = models.CharField(max_length=30)
    Address = models.CharField(max_length=90)
    Phone = models.IntegerField()
    Email = models.CharField(max_length=30)
    Discription = models.CharField(max_length=390)
    Status = models.CharField(max_length=30)


    class Meta:
        db_table = "tbl_business"


class tbl_catgry(models.Model):
    Name = models.CharField(max_length=30)
    Discription = models.CharField(max_length=390)
    Photo=models.CharField(max_length=225)

    class Meta:
        db_table = "tbl_catgry"  

class tbl_court(models.Model):
    Category = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    Location = models.CharField(max_length=30)
    Discription = models.CharField(max_length=390)
    Photo = models.CharField(max_length=225)
    Phone = models.IntegerField()
    Email = models.CharField(max_length=30)
    Facilities = models.CharField(max_length=390)             


    class meta:
        db_table = "tbl_court"


class tbl_tournament(models.Model):
    Tournament_Name = models.CharField(max_length=30)
    Time = models.CharField(max_length=30)
    Date = models.CharField(max_length=30)
    Type = models.CharField(max_length=390)        
    Venue = models.CharField(max_length=390) 

    class meta:
        db_table = "tbl_tournament"

class tbl_team(models.Model):
    Team_Name = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    Team_Manager = models.CharField(max_length=30)
    Phone = models.CharField(max_length=390)        
    Email = models.CharField(max_length=390) 
    Status = models.CharField(max_length=390) 

    class meta:
        db_table = "tbl_team"

class tbl_member(models.Model):
    Member_Name = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    DOB = models.CharField(max_length=30)
    Phone = models.CharField(max_length=390)        
    Email = models.CharField(max_length=390)  

    class meta:
        db_table = "tbl_member"
class tbl_login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    type1 = models.CharField(max_length=30)
     

    class meta:
        db_table = "tbl_login"


