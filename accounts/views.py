from django.contrib.admin.sites import AlreadyRegistered
from django.db.models.query import InstanceCheckMeta
from django.forms.forms import Form
from django.http import response
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from accounts.form import RegistraionForm, Search, UserLoginForm,TrainDetailForm
from .form import AddtrainForm,Final,userDetails
from .models import Addtrain, Compartment,Reservation, Station,TrainDetail,RouteDetail,DayDetail,Compartmentmapping
from django.contrib import messages
import mysql.connector

#Create your views here.
def home (request):
  return render(request,'accounts/home.html')

def Register(request):
  if request.method =="POST":
    form = RegistraionForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('home')
  else:
       form = RegistraionForm()
       return render(request,'accounts/register.html',{'form':form})



def login(request):
  if request.method =="POST":
    print(request.POST)  
    form = UserLoginForm(request,data=request.POST)
    print(form.is_valid())
    if form.is_valid():
      return redirect('call')
  else:
    form = UserLoginForm()
    return render(request,'accounts/login.html',{'form':form})


def Book(request):
  return render(request,'accounts/Book.html')

def call(request):
    if request.method =="POST":
      print(request.POST)  
      form =TrainDetailForm(request,data=request.POST)
      print(form.is_valid())
      if form.is_valid():
        return redirect('trainIDDettails')
    else:
      form =TrainDetailForm ()
    return render(request,"accounts/trainhome.html") 

def search (request):
  addtrain=Addtrain.objects.all()
  return render(request,"accounts/search1.html",{'addtrain':addtrain})

def  cancel (request):
  return render(request,'accounts/cancel.html')


def  check (request):
  return render(request,'accounts/check.html')


def  logout (request):
  print(request.GET)
  return render(request,'accounts/logout.html')
    #else:
    #return HttpResponse("<h1>asdasd</h1>")  

 
def index(request):
    if request.method=="POST":
      addTrain = Addtrain()
      addTrain.train_name=request.POST['train_name']
      addTrain.train_id = request.POST['train_id']
      addTrain.Seats_availability = request.POST['Seats_availability']
      addTrain.Compartment_type = request.POST['Compartment_type']
      addTrain.Source = request.POST['Source']
      addTrain.Destination = request.POST['Destination']
      addTrain.Departure_time = request.POST['Departure_time']                   
      addTrain.Arrival_time = request.POST['Arrival_time']
      addTrain.Travel_time = request.POST['Travel_time']
      addTrain.Fare = request.POST['Fare']
      addTrain.save()
      return redirect('retrieve')
    else:       
      form = AddtrainForm()      
      return render(request,'accounts/index.html',{'form':form})

"""def create(request):
    if request.method=="POST":
      train_name=request.POST['train_name']
      train_id=request.POST['train_id']
      Seats_availability=request.POST['Seats_availability']
      Compartment_type=request.POST['Compartment_type']
      Source=request.POST['Source']
      Destination=request.POST['Destination']
      Departure_time=request.POST['Departure_time']
      Arrival_time=request.POST['Arrival_time']
      Travel_time=request.POST['Travel_time']
      Fare=request.POST['Fare']
      obj=Addtrain.objects.create(train_name=train_name,train_id=train_id,Seats_availability=Seats_availability,Compartment_type=Compartment_type,Source=Source,Destination=Destination,Departure_time=Departure_time,Arrival_time=Arrival_time,Travel_time=Travel_time,Fare=Fare)
      obj.save()
    return redirect('/')"""

                         
def retrieve(request):
    addtrain=Addtrain.objects.all()
    return render(request,'accounts/retrieve.html',{'addtrain':addtrain})
                

def edit(request,id):
    object=Addtrain.objects.get(id=id)
    return render(request,'accounts/edit.html',{'object':object})

def update(request,id):
  trainname =request.GET.get('train_name')
  trainid =request.GET.get('train_id')
  Seatsavailability =request.GET.get('Seats_availability')
  Compartmenttype =request.GET.get('Compartment_type')
  Source =request.GET.get('Source')
  Destination =request.GET.get('Destination')
  Arrivaltime=request.GET.get('Arrival_time')
  Departuretime =request.GET.get('Departure_time')
  Traveltime =request.GET.get('Travel_time')
  Fare =request.GET.get('Fare')
  mysqldb=mysql.connector.connect(host="localhost",user="test",password="Admin@123",database="Addtrain")#established connection between your database  
  cursor=mysqldb.cursor()#cursor() method create a cursor object  
  try:     
    sql="UPDATE accounts_addtrain SET train_name= %s,train_id= %s,Seats_availability=%s,Compartment_type=%s,Source=%s,Destination=%s,Arrival_time=%s,Departure_time=%s,Travel_time=%s,Fare=%s WHERE id=%s"
    value= (trainname,trainid,Seatsavailability,Compartmenttype,Source,Destination,Arrivaltime,Departuretime,Traveltime,Fare,id)
    cursor.execute(sql, value)
    #Execute SQL Query to update record
    mysqldb.commit() # Commit is used for your changes in the database  
    print('Record updated successfully...')   
  except:   
   # rollback used for if any error  
    mysqldb.rollback()  
    mysqldb.close()#Connection Close 
  return retrieve(request)
  
 

def User(request):
        user=userDetails.objects.all()
        return render(request,"accounts/user.html",{'user':user})   
def Reservationdetail(request):
        reserved=Reservation.objects.all()
        return render(request,"accounts/Book.html",{'form':reserved})   

def train (request):
  form=Compartment.objects.all()
  addtrain=TrainDetail.objects.all()
  station=Station.objects.all()
  route = RouteDetail.objects.all()  
  day=DayDetail.objects.all()
  map=Compartmentmapping.objects.all()
  user=userDetails.objects.all()
  reserved=Reservation.objects.all()

  p={
    'addtrain':addtrain,'form':form,'station':station,'route':route,'day':day,'map':map,'user':user,'reserved':reserved

  }
  return render(request,"accounts/trainIDDetails.html",{'p':p}) 


def Route(request):
        route = RouteDetail.objects.all()      
        return render(request,"accounts/route.html",{'form':route})   


def stationdetail(request):
  form=Station.objects.all()
  return render(request,"accounts/station.html",{'form':form})   


def compartment(request):
  addtrain=Compartment.objects.all()
  return render(request,"accounts/comp.html",{'form':addtrain})   

def Dayorder(request):
      day=DayDetail.objects.all()
      return render(request,"accounts/day.html",{'form':day})   

def Mapping(request):
        map=Compartmentmapping.objects.all()
        return render(request,"accounts/side.html",{'form':map})   

def delete(request,pk):   
        Addtrain.objects.filter(id=pk).delete()
        return redirect('retrieve')

def doll(request):
  addtrain=Addtrain.objects.all()
  return render(request,'accounts/doll.html',{'addtrain':addtrain})

def user(request,id):
  mysqldb=mysql.connector.connect(host="localhost",user="test",password="Admin@123",database="Addtrain")#established connection between your database  
  cursor=mysqldb.cursor()  
  cursor.execute("SELECT * FROM accounts_routedetail WHERE id="+str(id))
  myresult = cursor.fetchone()
  print(id)
  Route_id =request.GET.get('Route_id')
  Email =request.GET.get('E_mail')  
  Phoneno =request.GET.get('Phone_no')
  Age =request.GET.get('Age')
  Gender =request.GET.get('Gender')   
  Aadhar_no =request.GET.get('Aadhar_no')
  Status =request.GET.get('Status')
  list1=list(myresult)
  sql = "INSERT INTO accounts_user (Name', 'E_mail', 'Age','Gender', 'train_name','train_id', 'no_of_booked_seats', 'Source', 'Destination','Departure_time','Arrival_time','Fare', 'Aadhar_no','Status','Phone_no', 'Compartment_type') VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
  value=(Route_id)
  #1, 'Kerala Express', 23456, 100, 'chennai', 'Madurai', '10.00', '3.00AM', '5.00', 'General class', 300, 
  list1.append(Route_id)
  list1.append(Email)
  list1.append(Phoneno)
  list1.append(Age)
  list1.append(Gender)
  list1.append(Aadhar_no)
  list1.append(Status)
  print(list1)

  for x in myresult:
    print(x)
  return render (request,'accounts/final.html',{'myresult':list1})
