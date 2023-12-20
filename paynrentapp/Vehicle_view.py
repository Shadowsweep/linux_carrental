from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view

from paynrentapp.serializers import VehicleSerializer
from paynrentapp.models import Vehicle
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def VehicleInterface(request):
    return render(request,'VehicleInterface.html')

@api_view(['GET','POST'])
def VehicleSubmit(request):
    if request.method == 'POST':
        vehicle_serializer = VehicleSerializer(data=request.data)
        if vehicle_serializer.is_valid():
            vehicle_serializer.save()
            return render(request,"VehicleInterface.html",{"message":"Record Submitted Successfully"})
        return render(request,"VehicleInterface.html",{"message":"Fail to Submit Record"})

@xframe_options_exempt
@api_view(['GET','POST'])
def DisplayVehicle(request):
  try:
    if request.method == 'GET':
      q = "select V.*,(select C.categoryname from paynrentapp_category C where C.id=V.cid) as categoryname, (select S.subcategoryname from paynrentapp_subcategory S where S.id=V.sid) as subcategoryname from paynrentapp_vehicle V"
      print(q)
      cursor = connection.cursor()
      cursor.execute(q)
      records = tuple_to_dict.ParseDictMultipleRecord(cursor)
      print("xxxxxxxxxx",records)
      
      return render(request,'VehicleDisplay.html',{'data':records})
  except Exception as e:
       print("Error:",e)
       return render(request,'VehicleDisplay.html',{'data':{}})   

@xframe_options_exempt
@api_view(['GET','POST'])
def DisplayByVehicleId(request):
  try:
    if request.method == 'GET':
      q="Select V.* ,(select C.categoryname from paynrentapp_category C where C.id=V.cid) as categoryname,( select S.subcategoryname from  paynrentapp_subcategory S where S.id = V.sid) as subcategoryname from  paynrentapp_vehicle  V where V.id={0} ".format(request.GET['id'])
      print(q)
      cursor=connection.cursor()
      cursor.execute(q)
      record=tuple_to_dict.ParseDictSingleRecord(cursor)
      
    #   print("xxxx",record)
      
      return render(request,'DisplayByVid.html',{'data':record})
  except Exception as e:
       print("Error:",e)
       return render(request,'DisplayByVid.html',{'data':{}})




#by this method we dont need to run query instead data is getting fetched to particular record we want
#this is ORM method but best for save and delete not helpful in joins

@xframe_options_exempt
@api_view(['GET','POST'])
def EditVehicle(request):
   try:
      if request.method =='GET':
         if(request.GET['btn']=="Edit"):
            vehicle=Vehicle.objects.get(pk=request.GET['id'])#hidden id
            vehicle.cid=request.GET['cid']
            vehicle.sid=request.GET['sid']
            vehicle.modelyear=request.GET['modelyear']
            vehicle.price=request.GET['price']
            vehicle.insured=request.GET['insured']
            vehicle.registrationno=request.GET['registrationno']
            vehicle.ownername=request.GET['ownername']
            vehicle.mobileno=request.GET['mobileno']
            vehicle.color=request.GET['color']
            vehicle.fueltype=request.GET['fueltype']
            vehicle.noofseats=request.GET['noofseats']
            vehicle.transmissiontype=request.GET['transmissiontype']
            vehicle.save()
         else:
            vehicle=Vehicle.objects.get(pk=request.GET['id'])
            vehicle.delete()

         return redirect('/api/displayvehicle')
   except Exception as e:
      print("Error:",e)
      return redirect('/api/displayvehicle')


@xframe_options_exempt
@api_view(['GET','POST'])
def DisplayVehicleIcon(request):
   try:
      if request.method =='GET':
         
         return render(request,'display_vehicle_icon.html',{'data':dict(request.GET)})
   except Exception as e:
      print("Error:",e)
      return render(request,'display_vehicle_icon.html',{'data':{}})


@xframe_options_exempt
@api_view(['GET','POST'])
def Vehicle_Save_icon(request):
  try:
    if request.method == 'POST':
      
       vehicle=Vehicle.objects.get(pk=request.POST['id'])
       vehicle.icon=request.FILES['icon']
       vehicle.save()
       
       return redirect('/api/displayvehicle')
  except Exception as e:
     print("Error:",e)
     return redirect('/api/displayvehicle') 
  

