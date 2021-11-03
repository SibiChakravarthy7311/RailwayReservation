from django.db import models
from django.db.models.aggregates import Max
from django.db.models.fields import CharField

# Create your models here.
class Addtrain(models.Model):
    train_name = models.CharField(max_length=30,null=True)
    train_id = models.IntegerField(null=True)
    Seats_availability = models.IntegerField(null=True)
    COMPARTMENT_TYPE=(
        ('Firstclass','1A'),
        ('AC2tier class','AC2tier class'),
        ('AC 3tier class','AC 3tier class'),
        ('Sleeper class','Sleeper class'),
        ('Second class','Second class'),
        ('General class','General class'),
    )
    Compartment_type = models.CharField(max_length=30,null=True,choices=COMPARTMENT_TYPE)
    Source = models.CharField(max_length=30,null=True)
    Destination = models.CharField(max_length=30,null=True)
    Departure_time = models.CharField(max_length=30,null=True)
    Arrival_time = models.CharField(max_length=30,null=True)
    Travel_time = models.CharField(max_length=50,null=True) 
    Fare = models.IntegerField(null=True)
    def __str__(self) :
        return self.train_name

class Final(models.Model):
    Name = models.CharField(max_length=40,null=True)
    E_mail = models.CharField(max_length=40,null=True)
    Phone_no = models.CharField(max_length=40,null=True)
    Age = models.IntegerField(null=True)
    Gender = models.CharField(max_length=30,null=True)
    train_name = models.CharField(max_length=30,null=True)
    train_id = models.IntegerField(null=True)
    no_of_booked_seats = models.IntegerField(null=True)
    COMPARTMENT_TYPE=(
        ('Firstclass','1A'),
        ('AC2tier class','AC2tier class'),
        ('AC 3tier class','AC 3tier class'),
        ('Sleeper class','Sleeper class'),
        ('Second class','Second class'),
        ('General class','General class'),
    )
    Compartment_type = models.CharField(max_length=30,null=True,choices=COMPARTMENT_TYPE)
    Source = models.CharField(max_length=30,null=True)
    Destination = models.CharField(max_length=30,null=True)
    Departure_time = models.CharField(max_length=30,null=True)
    Arrival_time = models.CharField(max_length=30,null=True)
    Fare = models.IntegerField(null=True)
    Aadhar_no = models.IntegerField(null=True)
    Status = models.CharField(max_length=40,null=True)
    def __str__(self) :
        return self.Name

class userDetails(models.Model):
    Name = models.CharField(max_length=40,null=True)
    E_mail = models.CharField(max_length=40,null=True)
    Password=models.IntegerField(null=True)
    Phone_no = models.CharField(max_length=40,null=True)
    Age = models.IntegerField(null=True)
    Gender = models.CharField(max_length=30,null=True)
    Aadhar_no=models.IntegerField(null=True)
    def __str__(self) :
        return self.Name

class Reservation(models.Model):
    E_mail = models.CharField(max_length=40,null=True)
    PNR_id = models.IntegerField(null=True)
    Train_id=models.IntegerField(null=True)
    Reserved_mode=models.CharField(max_length=30,null=True)
    Reserved_date=models.DateField(null=True)
    Booked_status=models.CharField(max_length=30,null=True)
    no_of_booked_seats=models.IntegerField(null=True)
    Compartment_id=models.IntegerField(null=True)
    Route_id=models.IntegerField(null=True)
    Booked_amount=models.IntegerField(null=True)

class TrainDetail(models.Model):
    Train_id=models.IntegerField(null=True)
    Train_name=models.CharField(max_length=30,null=True)
    Route_id=models.IntegerField(null=True)
    Arrival_time = models.CharField(max_length=30,null=True)
    Departure_time = models.CharField(max_length=30,null=True)    

class RouteDetail(models.Model):
    Route_id=models.IntegerField(null=True)
    Source_id=models.IntegerField(null=True)
    Destination_id=models.IntegerField(null=True)

class Station(models.Model):
    Station_id=models.IntegerField(null=True)
    Station_name=models.CharField(max_length=30,null=True)
    def __str__(self) :
        return self.Train_name


class Compartment(models.Model):
    Compartment_id=models.IntegerField(null=True)
    Compartment_type=models.CharField(max_length=30,null=True)

class DayDetail(models.Model):
    Train_id=models.IntegerField(null=True)
    Sunday=models.CharField(max_length=30,null=True)
    Monday=models.CharField(max_length=30,null=True)
    Tuesday=models.CharField(max_length=30,null=True)
    Wednesday=models.CharField(max_length=30,null=True)
    Thursday=models.CharField(max_length=30,null=True)
    Friday=models.CharField(max_length=30,null=True)
    Saturday=models.CharField(max_length=30,null=True)              


class Compartmentmapping(models.Model):
    Train_id=models.IntegerField(null=True)
    Compartment_id=models.IntegerField(null=True)
    Total_no_of_seats=models.IntegerField(null=True)
    Available_no_of_seats=models.IntegerField(null=True)
    Booking_fare=models.IntegerField(null=True)
    Booked_seats=models.IntegerField(null=True)
