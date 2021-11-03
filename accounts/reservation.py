from accounts.form import ReservationForm
from accounts.models import Reservation
from django.shortcuts import redirect, render


def create (request):
    if request.method =="GET":
        obj=Reservation()
        obj.E_mail = request.GET['E_mail']
        obj.PNR_id=request.GET['PNR_id']
        obj.Train_id=request.GET['Train_id']
        obj.Reserved_mode = request.GET['Reserved_mode']
        obj.Booked_status=request.GET['Booked_status']
        obj.no_of_booked_seats=request.GET['no_of_booked_seats']
        obj.Compartment_id = request.GET['Compartment_id']
        obj.Route_id = request.GET['Route_id']
        obj.Booked_amount=request.GET['Booked_amount']
        obj.save()
        return redirect('train')
    else:       
      form =ReservationForm()      
      return render(request,'accounts/trainIDDetails.html',{'form':form})

def update(request,id):
    object=Reservation.objects.get(id=id)
    object.E_mail = request.GET['E_mail']
    object.PNR_id=request.GET['PNR_id']
    object.Train_id=request.GET['Train_id']
    object.Reserved_mode = request.GET['Reserved_mode']
    object.Booked_status = request.GET['Booked_status']
    object.no_of_booked_seats=request.GET['no_of_booked_seats']
    object.Compartment_id=request.GET['Compartment_id']
    object.Route_id = request.GET['Route_id']
    object.Booked_amount = request.GET['Booked_amount']
    object.save()
    return redirect('train')
def reservation(request):
    return render(request,'accounts/reservecreate.html')

def edit(request,id):
    return render(request,'accounts/reserveedit.html',{'id':id})


def delete(request,id):   
        Reservation.objects.filter(id=id).delete()
        return redirect('train')
