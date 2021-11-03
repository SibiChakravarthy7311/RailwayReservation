from django.contrib import admin
from accounts.models import Addtrain, Compartment, Final, Reservation, RouteDetail, Station,userDetails
from accounts.models import TrainDetail,DayDetail,Compartmentmapping
# Register your models here.
class AddtrainAdmin(admin.ModelAdmin):
    Train_details = ['train_name','train_id','Seats_availability','Compartment_type','Source','Destination','Departure_time','Arrival_time','Travel_time','Fare']
    admin.site.register(Addtrain)

class FinalAdmin(admin.ModelAdmin):
    object_details=['Name','E_mail','Phone_no','Age','Gender','train_name','train_id','no_of_Booked_seats','Compartment_type','Source','Destination','Departure_time','Arrival_time','Fare','Aadhar_no','Status']
    admin.site.register(Final)

class userDetailsAdmin(admin.ModelAdmin):
    object_details=['Name','E_mail','Password','Phone_no','Age','Gender','Aadhar_no']
    admin.site.register(userDetails)


class ReservationAdmin(admin.ModelAdmin):
    object_details=['E_mail','PNR_id','Train_id','Reserved_mode','Reserved_date','Booked_status','no_of_booked_seats','Compartment_id','Route_id','Booked_amount']
    admin.site.register(Reservation)

class TrainDetailAdmin(admin.ModelAdmin):
    object_details=['Train_id','Train_name','Route_id','Arrival_time','Departure_time']
    admin.site.register(TrainDetail)

class RouteDetailAdmin(admin.ModelAdmin):
    object_details=['Route_id','Sourec_id','Destination_id']
    admin.site.register(RouteDetail)

class StationAdmin(admin.ModelAdmin):
    object_details=['Station_id','Station_name']
    admin.site.register(Station)

class CompartmentAdmin(admin.ModelAdmin):
    object_details=['Compartment_id','Compartment_type']
    admin.site.register(Compartment)

class DayDetailAdmin(admin.ModelAdmin):
    object_details=['Train_id','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    admin.site.register(DayDetail)


class CompartmentmappingAdmin(admin.ModelAdmin):
    object_details=['Train_id','Compartment_id','Total_no_of_seats','Available_no_of_seats','Booking_fare','Booked_seats']
    admin.site.register(Compartmentmapping)
