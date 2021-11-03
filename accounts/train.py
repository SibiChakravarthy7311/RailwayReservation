from django.http.response import HttpResponse
from accounts.views import train
from accounts.form import TrainDetailForm
from accounts.models import TrainDetail
from django.shortcuts import redirect, render


def create (request):
    if request.method =="GET":
        train=TrainDetail()
        train.Train_id = request.GET['Train_id']
        train.Train_name=request.GET['Train_name']
        train.Route_id=request.GET['Route_id']
        train.Arrival_time = request.GET['Arrival_time']
        train.Departure_time = request.GET['Departure_time']
        train.save()
        return redirect('train')
    else:       
      form =TrainDetailForm()      
      return render(request,'accounts/trainIDDetails.html',{'form':form})
def summa(request):
    return render(request,'accounts/traincreate.html')

def edit(request,id):
    return render(request,'accounts/trainedit.html',{'id':id})

def update(request,id):
    object=TrainDetail.objects.get(id=id)
    object.Train_id = request.GET['Train_id']
    object.Train_name=request.GET['Train_name']
    object.Route_id=request.GET['Route_id']
    object.Arrival_time = request.GET['Arrival_time']
    object.Departure_time = request.GET['Departure_time']
    object.save()
    return redirect('train')

def delete(request,id):   
        TrainDetail.objects.filter(id=id).delete()
        return redirect('train')
