from django.shortcuts import redirect,render
#from accounts.models import RouteDetail
from django.http.response import HttpResponse
import mysql.connector
from accounts.models import RouteDetail, TrainDetail, Station
from accounts.views import Route


"""def user(request):
    std_info = RouteDetail.objects.all()
    std_grade =  std_info.filter(Route_id='456') 
    return HttpResponse(std_grade)"""
def user(request):
    obj =RouteDetail.objects.all()
    route= obj.filter(Route_id='123')
    return HttpResponse(route)
    #return render(request,"accounts/.html",{'train':route})

mysqldb=mysql.connector.connect(host="localhost",user="test",password="Admin@123",database="Addtrain")#established connection between your database  
cursor=mysqldb.cursor() 
sql= "SELECT Train_name,Arrival_time,Departure_time,Source_id,Destination_id FROM accounts_traindetail INNER JOIN accounts_routedetail ON accounts_traindetail.Route_id = accounts_routedetail.Route_id"
#sql= "SELECT Source_id,Destination_id FROM accounts_routedetail INNER JOIN accounts_traindetail ON accounts_routedetail.Route_id = accounts_traindetail.Route_id"
cursor.execute(sql)
print(id)
rows=cursor.fetchall()
"""list1=list(rows)
    list1.append(From)
    list1.append(To)
print(list1)"""
for x in rows:  
  print(x)
  mysqldb.close()
