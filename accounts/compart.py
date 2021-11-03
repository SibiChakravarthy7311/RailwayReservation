from mysql import connector
from accounts.views import Compartment
from accounts.form import CompartmentForm
from accounts.models import Compartment
from django.shortcuts import redirect, render


def create (request):
    if request.method =="GET":
        comp=Compartment()
        comp.Compartment_id=request.GET['Compartment_id']
        comp.Compartment_type=request.GET['Compartment_type']
        comp.save()
        return redirect('train')
    else:       
      form =CompartmentForm()      
      return render(request,'accounts/trainIDDetails.html',{'form':form})
def update(request,id):
    object=Compartment.objects.get(id=id)
    object.Compartment_id = request.GET['Compartment_id']
    object.Compartment_type = request.GET['Compartment_type']
    object.save()
    return redirect('train')

def comp(request):
    return render(request,'accounts/compcreate.html')


def edit(request,id):
    return render(request,'accounts/compedit.html',{'id':id})
def delete(request,id):   
        Compartment.objects.filter(id=id).delete()
        return redirect('train')
