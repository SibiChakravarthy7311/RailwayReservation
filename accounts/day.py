from accounts.form import DayDetailForm
from accounts.models import DayDetail
from django.shortcuts import redirect, render


def create (request):
    if request.method =="GET":
        obj=DayDetail()
        obj.Train_id=request.GET['Train_id']
        obj.Sunday=request.GET['Sunday']
        obj.Monday = request.GET['Monday']
        obj.Tuesday = request.GET['Tuesday']
        obj.Wednesday=request.GET['Wednesday']
        obj.Thursday=request.GET['Thursday']
        obj.Friday = request.GET['Friday']
        obj.Saturday = request.GET['Saturday']
        obj.save()
        return redirect('train')
    else:       
      form =DayDetailForm()      
      return render(request,'accounts/trainIDDetails.html',{'form':form})
def update(request,id):
    object=DayDetail.objects.get(id=id)
    object.Train_id = request.GET['Train_id']
    object.Sunday=request.GET['Sunday']
    object.Monday=request.GET['Monday']
    object.Tuesday = request.GET['Tuesday']
    object.Wednesday = request.GET['Wednesday']
    object.Thursday=request.GET['Thursday']
    object.Friday = request.GET['Friday']
    object.Saturday = request.GET['Saturday']
    object.save()
    return redirect('train')
    
def day(request):
    return render(request,'accounts/daycreate.html')

def edit(request,id):
    return render(request,'accounts/dayedit.html',{'id':id})
def delete(request,id):   
        DayDetail.objects.filter(id=id).delete()
        return redirect('train')
