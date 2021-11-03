from accounts.form import CompartmentmappingForm
from accounts.models import Compartmentmapping
from django.shortcuts import redirect, render


def create (request):
    if request.method =="POST":
        obj=Compartmentmapping()
        obj.Train_id = request.GET['Train_id']
        obj.Compartment_id=request.GET['Compartment_id']
        obj.Total_no_of_seats=request.GET['Total_no_of_seats']
        obj.Available_no_of_seats = request.GET['Available_no_of_seats']
        obj.Booking_fare = request.GET['Booking_fare']
        obj.save()
        return redirect('train')
    else:       
      form =CompartmentmappingForm()      
      return render(request,'accounts/trainIDDetails.html',{'form':form})
def update(request,id):
    object=Compartmentmapping.objects.get(id=id)
    object.Train_id = request.GET['Train_id']
    object.Compartment_id=request.GET['Compartment_id']
    object.Total_no_of_seats=request.GET['Total_no_of_seats']
    object.Available_no_of_seats = request.GET['Available_no_of_seats']
    object.Booking_fare = request.GET['Booking_fare']
    object.save()
    return redirect('train')
def compmap(request):
        return render(request,'accounts/compmapcreate.html')

def edit(request,id):
    return render(request,'accounts/compmapedit.html',{'id':id})
def delete(request,id):   
        Compartmentmapping.objects.filter(id=id).delete()
        return redirect('train')
