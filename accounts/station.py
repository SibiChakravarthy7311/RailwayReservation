from accounts.views import  stationdetail
from accounts.form import StationForm
from accounts.models import Station
from django.shortcuts import redirect, render

def create (request):
    if request.method =="GET":
        obj=Station()
        obj.Station_id = request.GET['Station_id']
        obj.Station_name=request.GET['Station_name']
        obj.From=request.GET.get['From']
        obj.To = request.GET.get['To']
        obj.save()
        return redirect('train')
    else:       
      form =StationForm()      
      return render(request,'accounts/trainIDDetails.html',{'form':form})
def update(request,id):
    object=Station.objects.get(id=id)
    object.Station_id = request.GET['Station_id']
    object.Station_name=request.GET['Station_name']
    object.save()
    return redirect('train')
def station(request):
    return render(request,'accounts/stationcreate.html')


def edit(request,id):
    return render(request,'accounts/stationedit.html',{'id':id})

def delete(request,id):   
        Station.objects.filter(id=id).delete()
        return redirect('train')
