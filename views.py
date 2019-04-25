from django.shortcuts import render
from django.shortcuts import render,redirect
from app1.models import tbl_business,tbl_catgry,tbl_court,tbl_tournament,tbl_team,tbl_member,tbl_login
from django.conf  import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
# Create your views here.

def index (request):
    return render (request,'login.html')
def reg (request):
    return render (request,'buss_reg.html')
def add_cat (request):
    return render (request,'add_category.html')
def add_court (request):
    data=tbl_catgry.objects.all()
    return render (request,'court_reg.html',{'cat':data})       
def add_tour (request):
    return render (request,'tournament.html')
def add_team (request):
    return render (request,'team.html')
def add_member (request):
    return render (request,'team_member.html')
def admin1 (request):
    return render (request,'admin.html')
def customer1 (request):
    return render (request,'customer.html')
def bussiness1 (request):
    return render (request,'bussiness.html') 
def verify (request,id):
    items = tbl_business.objects.get(id=id)  
    return render(request,"verify.html",{'items':items })  
def verifysave (request,id):
    items = tbl_business.objects.get(id=id)
    items.Status="Ok"
    items.save()
    if request.method == 'POST':
        data = tbl_login()
        data.username=request.POST.get('txtEmail')  
        data.password=request.POST.get('txtPhone')  
        data.type1="bussiness"
        data.save()
        return render(request, 'view_bussiness.html')






def busisave(request):
    if request.method == 'POST':
        data = tbl_business()
        data.Name=request.POST.get('txtName')
        data.Address=request.POST.get('txtAddress')
        data.Phone=request.POST.get('txtPhone')
        data.Email=request.POST.get('txtEmail')
        data.Discription=request.POST.get('txtDiscription')
        data.Status="NP"
        data.save()
        return render(request, 'index.html')
    else:
        return HttpResponse("invalid")


def catsave(request):
    if request.method == 'POST':
        data = tbl_catgry()
        data.Name=request.POST.get('txtName')
        data.Discription=request.POST.get('txtDiscription')
        Photo = request.FILES['Photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        data.Photo=uploaded_file_url
        data.save()
        return render(request, 'login.html')
    else:
        return HttpResponse("Invalid data type")   



def courtsave(request):
    if request.method == 'POST':
        data = tbl_court()
        data.Category=request.POST.get('txtCategory')
        data.Name=request.POST.get('txtName')
        data.Location=request.POST.get('txtLocation')
        data.Discription=request.POST.get('txtDiscription')
        data.Phone=request.POST.get('txtPhone')
        data.Email=request.POST.get('txtEmail')
        data.Facilities=request.POST.get('txtFacilities')
        Photo = request.FILES['Photo']
        fs1 = FileSystemStorage()
        filename = fs1.save(Photo.name, Photo) 
        uploaded_file_url = fs1.url(filename)
        data.Photo=uploaded_file_url
        data.save()
        return render(request, 'login.html')
    else:
        return HttpResponse("Invalid data type")

def toursave(request):
    if request.method == 'POST':
        data = tbl_tournament()
        data.Name=request.POST.get('txtTname')
        data.Time=request.POST.get('txtTime')
        data.Date=request.POST.get('txtDate')
        data.Type=request.POST.get('txtType')
        data.Venue=request.POST.get('txtVenue')
        data.save()
        return render(request, 'login.html')
    else:
        return HttpResponse("invalid")


def teamsave(request):
    if request.method == 'POST':
        data = tbl_team()
        data.Team_Name=request.POST.get('txtTname')
        data.Address=request.POST.get('txtAddress')
        data.Team_Manager=request.POST.get('txtManager')
        data.Phone=request.POST.get('txtPhone')
        data.Email=request.POST.get('txtEmail')
        data.Status=request.POST.get('txtStatus')
        data.save()
        return render(request, 'login.html')
    else:
        return HttpResponse("invalid")

def membersave(request):
    if request.method == 'POST':
        data = tbl_member()
        data.Member_Name=request.POST.get('txtMname')
        data.Address=request.POST.get('txtAddress')
        data.DOB=request.POST.get('txtDOB')
        data.Phone=request.POST.get('txtPhone')
        data.Email=request.POST.get('txtEmail')
        data.save()
        return render(request, 'login.html')
    else:
        return HttpResponse("invalid")        

def cat1(request):
    items = tbl_catgry.objects.all()  
    return render(request,"view_product.html",{'items':items }) 
    

def cat2(request):
    items = tbl_court.objects.all()  
    return render(request,"view_court.html",{'items':items })     

def log(request):
    if request.method == 'POST':
        dataa = tbl_login.objects.all()
        
        un=request.POST.get('txtName')
        pwd=request.POST.get('txtPassword')
        flag=0
            
        for da in dataa:
            if un == da.username and pwd == da.password:
                type=da.type1
                flag = 1
                request.session['uid'] = da.id
                if type=="admin":
                    return redirect('/admin')
                elif type=="bussiness":
                    return redirect('/bussiness')
                elif type=="customer":
                    return redirect('/customer')    
                else:
                    return HttpResponse("Invalid acct type")

        if flag == 0:                
                return HttpResponse("User does not exist")
            
def verify_buss(request):
    items = tbl_business.objects.all()  
    return render(request,"view_bussiness.html",{'items':items })        


