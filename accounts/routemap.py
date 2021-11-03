from accounts.views import Train
from accounts.form import RoutemappingForm
from accounts.models import Routemapping
from django.shortcuts import redirect, render


def routemap (request):
    if request.method =="POST":
        obj=Routemapping()
        obj.Route_id = request.POST['Route_id']
        obj.Train_id=request.POST['Train_id']
        obj.Arrival_time=request.POST['Arrival_time']
        obj.Departure_time = request.POST['Departure_time']
        obj.save()
        return redirect('train')
    else:       
      form =RoutemappingForm()      
      return render(request,'accounts/trainIDDetails.html',{'form':form})

def update(request,id):
    Route_id=request.GET.get('Route_id')
    Train_name=request.GET.get('Train_name')
    Arrival_time=request.GET.get('Arrival_time')
    Departure_time=request.GET.get('Departure_time')
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

def useredit(request,id):
    object=TrainDetail.useobjects.get(id=id)
    return render(request,'accounts/useredit.html',{'object':object})
def delete(request,pk):   
        Addtrain.objects.filter(id=pk).delete()
        return redirect('retrieve')
