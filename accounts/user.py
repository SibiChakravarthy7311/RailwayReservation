from accounts.form import userDetailsForm
from accounts.models import userDetails
from django.shortcuts import redirect, render


def create (request):
    if request.method =="GET":
        obj=userDetails()
        obj.Name = request.GET['Name']
        obj.E_mail = request.GET['E_mail']
        obj.Password = request.GET['Password']
        obj.Phone_no=request.GET['Phone_no']
        obj.Age=request.GET['Age']
        obj.Gender = request.GET['Gender']
        obj.Aadhar_no = request.GET['Aadhar_no']
        obj.save()
        return redirect('train')
    else:       
      form =userDetailsForm()      
      return render(request,'accounts/trainIDDetails.html',{'form':form})

def update(request,id):
    object=userDetails.objects.get(id=id)
    object.Name = request.GET['Name']
    object.E_mail=request.GET['E_mail']
    object.Password=request.GET['Password']
    object.Phone_no = request.GET['Phone_no']
    object.Age = request.GET['Age']
    object.Gender = request.GET['Gender']
    object.Aadhar_no = request.GET['Aadhar_no']
    object.save()
    return redirect('train')

def user(request):
    return render(request,'accounts/usercreate.html')

def edit(request,id):
    return render(request,'accounts/useredit.html',{'id':id})
def delete(request,id):   
        userDetails.objects.filter(id=id).delete()
        return redirect('train')
