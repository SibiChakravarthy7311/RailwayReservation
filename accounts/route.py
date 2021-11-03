from accounts.views import Route
from accounts.form import RouteDetailForm
from accounts.models import RouteDetail
from django.shortcuts import redirect, render


def create (request):
    if request.method =="GET":
        route=RouteDetail()
        route.Route_id=request.GET['Route_id']
        route.Source_id = request.GET['Source_id']
        route.Destination_id = request.GET['Destination_id']
        route.save()
        return redirect('train')
    else:       
      form =RouteDetailForm()      
      return render(request,'accounts/trainIDDetails.html',{'form':form})

def Route(request):
    return render(request,'accounts/routecreate.html')
def edit(request,id):
    return render(request,'accounts/routeedit.html',{'id':id})

def update(request,id):    
    object=RouteDetail.objects.get(id=id)
    object.Route_id = request.GET['Route_id']
    object.Source_id=request.GET['Source_id']
    object.Destination_id=request.GET['Destination_id']
    object.save()
    return redirect('train')


def delete(request,id):   
        RouteDetail.objects.filter(id=id).delete()
        return redirect('train')
