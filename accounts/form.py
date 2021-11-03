from io import UnsupportedOperation
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
#from accounts.views import Train
from .models import Addtrain, Final, Reservation, userDetails,TrainDetail,RouteDetail,Station,Compartment,DayDetail,Compartmentmapping


class RegistraionForm(UserCreationForm):
    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'email',
            'username',
        }
        def save(self,commit=True):
            user = super(RegistraionForm,self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.username = self.cleaned_data['username']

            if commit:
                user.save()
            return user
    
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = {
            'username',
            'password',
        }

        def save(self,commit=True):
            user = super(UserLoginForm,self).save(commit=False)
            user.user_name = self.cleaned_data['username']
            user.password = self.cleaned_data['password']
            if commit:
                user.save()
            return user 

class Search(forms.Form):
        class Meta:
           model = User
           fields = {
            'Depart',
            'Return',
            'from',
            'to',
            'Adult',
            'Chidren',
            'Depart_date',
            'Return_date',
            'Compartment_type'
        }
class AddtrainForm(forms.Form):
    class Meta:
        model=Addtrain
    fields="__all__"

class FinalForm(forms.Form):
    class Meta:
        Model = Final
        fields="__all__"

class userDetailsForm(forms.Form):
    class Meta:
        Model = userDetails
        fields="__all__"
class ReservationForm(forms.Form):
    class Meta:
        Model = Reservation
        fields="__all__"

class TrainDetailForm(forms.Form):
    class Meta:
        Model = TrainDetail
        fields="__all__"

class RouteDetailForm(forms.Form):
    class Meta:
        Model = RouteDetail
        fields="__all__"

class StationForm(forms.Form):
    class Meta:
        Model = Station
        fields="__all__"

class CompartmentForm(forms.Form):
    class Meta:
        Model = Compartment
        fields="__all__"

class DayDetailForm(forms.Form):
    class Meta:
        Model = DayDetail
        fields="__all__"

class CompartmentmappingForm(forms.Form):
    class Meta:
        Model = Compartmentmapping
        fields="__all__"
