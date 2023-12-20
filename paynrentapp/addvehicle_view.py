from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from paynrentapp.serializers import AddVehicleSerializer
from paynrentapp.models import AddVehicle
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def AddVehicleInterface(request):
    return render(request,'AddVehicleInterface.html')

@xframe_options_exempt

@api_view(['GET','POST'])
def AddVehicleSubmit(request):
    if request.method == 'POST':
        addvehicle_serializer = AddVehicleSerializer(data=request.data)
        if addvehicle_serializer.is_valid():
            addvehicle_serializer.save()
            return render(request,"AddVehicleInterface.html",{"message":"Record Submitted Successfully"})
        return render(request,"AddVehicleInterface.html",{"message":"Fail to Submit Record"})


@api_view(['GET','POST'])
def DisplayAddVehicle(request):
    try:
        if request.method == 'GET':
            list_addvehicle = AddVehicle.objects.all()
            list_addvehicle_serializer = AddVehicleSerializer(list_addvehicle, many=True)
            addrecord = tuple_to_dict.ParseDict(list_addvehicle_serializer.data)
            print(addrecord)
      
            return render(request, 'AddVehicleDisplay.html', {'data': addrecord})
    except Exception as e:
        print("Error:", e)
        return render(request, 'AddVehicleDisplay.html', {'data': {}})



# @xframe_options_exempt
# @api_view(['GET','POST'])
# def DisplayByAddVehicleId(request):
#   try:
#     if request.method == 'GET':
#       q="Select * from paynrentapp_addvehicle where id={0} ".format(request.GET['id'])
#       cursor=connection.cursor()
#       cursor.execute(q)
#       record=tuple_to_dict.ParseDictSingleRecord(cursor)
      
#     #   print("xxxx",record)
      
#       return render(request,'DisplayById.html',{'data':record})
#   except Exception as e:
#        print("Error:",e)
#        return render(request,'DisplayById.html',{'data':{}})




# #by this method we dont need to run query instead data is getting fetched to particular record we want
# #this is ORM method but best for save and delete not helpful in joins

# @xframe_options_exempt
# @api_view(['GET','POST'])
# def EditAddVehicle(request):
#    try:
#       if request.method =='GET':
#          if(request.GET['btn']=="Edit"):
#             vehicle=AddVehicle.objects.get(pk=request.GET['id'])#hidden id
#             vehicle.cid=request.GET['brand']
#             vehicle.sid=request.GET['segment']
#             vehicle.modelyear=request.GET['model_name']
#             vehicle.price=request.GET['price']
#             vehicle.fueltype=request.GET['fueltype']
#             vehicle.noofseats=request.GET['noofseats']
#             vehicle.transmissiontype=request.GET['transmissiontype']
#             vehicle.save()
#          else:
#             vehicle=AddVehicle.objects.get(pk=request.GET['id'])
#             vehicle.delete()

#          return redirect('/api/displayvehicle')
#    except Exception as e:
#       print("Error:",e)
#       return redirect('/api/displayvehicle')


# @xframe_options_exempt
# @api_view(['GET','POST'])
# def AddDisplayVehicleIcon(request):
#    try:
#       if request.method =='GET':
         
#          return render(request,'display_vehicle_icon.html',{'data':dict(request.GET)})
#    except Exception as e:
#       print("Error:",e)
#       return render(request,'display_vehicle_icon.html',{'data':{}})
   
# @xframe_options_exempt
# @api_view(['GET','POST'])
# def AddDisplayUserVehicleIcon(request):
#    try:
#       if request.method =='GET':
         
#          return render(request,'display_vehicle_icon.html',{'data':dict(request.GET)})
#    except Exception as e:
#       print("Error:",e)
#       return render(request,'display_vehicle_icon.html',{'data':{}})


# @xframe_options_exempt
# @api_view(['GET','POST'])
# def AddVehicle_Save_icon(request):
#   try:
#     if request.method == 'POST':
      
#        vehicle=AddVehicle.objects.get(pk=request.POST['id'])
#        vehicle.icon=request.FILES['icon']
#        vehicle.save()
       
#        return redirect('/api/displayvehicle')
#   except Exception as e:
#      print("Error:",e)
#      return redirect('/api/displayvehicle') 
  
# @xframe_options_exempt
# @api_view(['GET','POST'])
# def AddUserVehicle_Save_icon(request):
#   try:
#     if request.method == 'POST':
      
#        vehicle=AddVehicle.objects.get(pk=request.POST['id'])
#        vehicle.icon=request.FILES['usericon']
#        vehicle.save()
       
#        return redirect('/api/displayvehicle')
#   except Exception as e:
#      print("Error:",e)
#      return redirect('/api/displayvehicle') 
  
# @xframe_options_exempt
# @api_view(['GET','POST'])
# def DisplayAddVehicleJSON(request):
#   try:
#     if request.method == 'GET':
#       list_addvehicle=AddVehicle.objects.all()
#       list_addvehicle_serializer=AddVehicleSerializer(list_addvehicle,many=True)
#       addrecord=tuple_to_dict.ParseDict(list_addvehicle_serializer.data)
      
      
#       return JsonResponse(addrecord,safe=False)
#   except Exception as e:
#        print("Error:",e)
#        return JsonResponse([],safe=False)
  
  

