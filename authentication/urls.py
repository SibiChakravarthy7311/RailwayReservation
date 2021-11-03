"""authentication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path
from accounts import compartmap, views,train,route,station,compart,day,user,reservation,userdetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('Register/',views.Register,name="Register"),
    path('login/', views.login, name='login'),
    path('Book/', views.Book, name='Book'),
    path('search/', views.search,name='search'),
    path('train/', views.train, name='train'),
    path('cancel/', views.cancel, name='cancel'),
    path('check/', views.check, name='check'),
    path('logout', views.logout, name='logout'),
    path('index/',views.index,name='index'),
    path('call',views.call,name="call"), 
    path('Stationdetail',views.stationdetail,name="Stationdetail"), 
    path('Dayorder',views.Dayorder,name="Dayorder"),  
    path('Mapping',views.Mapping,name="Mapping"),  
    path('compart',views.compartment,name="compart"), 
    path('retrieve',views.retrieve,name="retrieve"),
    path('edit/<int:id>',views.edit,name="edit"),



    path('trainedit/<int:id>',train.edit,name="trainedit"),
    path('traindelete/<int:id>',train.delete,name="traindelete"),
    path('summa',train.summa,name="summa"),
    path('traincreate',train.create,name="traincreate"),
    path('trainupdate/<int:id>',train.update,name="trainupdate"),

    path('routeedit/<int:id>',route.edit,name="routeedit"),
    path('routedelete/<int:id>',route.delete,name="routedelete"),
    path('Route',route.Route,name="Route"),
    path('routecreate',route.create,name="routecreate"),
    path('routeupdate/<int:id>',route.update,name="routeupdate"),
   
    path('stationedit<int:id>',station.edit,name="stationedit"),
    path('stationdelete/<int:id>',station.delete,name="stationdelete"),
    path('station',station.station,name="station"),
    path('stationcreate',station.create,name="stationcreate"),
    path('stationupdate/<int:id>',station.update,name="stationupdate"),

    path('compartedit<int:id>',compart.edit,name="compartedit"),
    path('compartdelete/<int:id>',compart.delete,name="compartdelete"),
    path('comp',compart.comp,name="comp"),
    path('compartcreate',compart.create,name="compartcreate"),
    path('compartupdate/<int:id>',compart.update,name="compartupdate"),

    path('dayedit<int:id>',day.edit,name="dayedit"),
    path('daydelete/<int:id>',day.delete,name="daydelete"),
    path('day',day.day,name="day"),
    path('daycreate',day.create,name="daycreate"),
    path('dayupdate/<int:id>',day.update,name="dayupdate"),

    path('useredit<int:id>',user.edit,name="useredit"),
    path('userdelete/<int:id>',user.delete,name="userdelete"),
    path('user',user.user,name="user"),
    path('usercreate',user.create,name="usercreate"),
    path('userupdate/<int:id>',user.update,name="userupdate"),

    path('reservationedit<int:id>',reservation.edit,name="reservationedit"),
    path('reservationdelete/<int:id>',reservation.delete,name="reservationdelete"),
    path('reservation',reservation.reservation,name="reservation"),
    path('reservationcreate',reservation.create,name="reservationcreate"),
    path('reservationupdate/<int:id>',reservation.update,name="reservationupdate"),

    path('compartmaptedit<int:id>',compartmap.edit,name="compartmapedit"),
    path('compartmapdelete/<int:id>',compartmap.delete,name="compartmapdelete"),
    path('compmap',compartmap.compmap,name="compmap"),
    path('compartmapcreate',compartmap.create,name="compartmapcreate"),
    path('compartmapupdate/<int:id>',compartmap.update,name="compartmapupdate"),

    path('delete/<int:pk>', views.delete,name="delete"),  
    path('doll',views.doll,name='doll'),
    #path('final/<int:id>',views.final,name='final'),
    path('Register/Stationdetail',views.stationdetail,name="Stationdetail"),
   
    path('user1',userdetail.user,name='user1'),

]

