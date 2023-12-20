from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from paynrentapp.serializers import SubCategorySerializer
from paynrentapp.models import SubCategory
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def SubCategoryInterface(request):
    return render(request,'SubCategoryInterface.html')

@api_view(['GET','POST'])
def SubCategorySubmit(request):
    if request.method == 'POST':
        subcategory_serializer = SubCategorySerializer(data=request.data)
        if subcategory_serializer.is_valid():
            subcategory_serializer.save()
            return render(request,"SubCategoryInterface.html",{"message":"Record Submitted Successfully"})
        return render(request,"SubCategoryInterface.html",{"message":"Fail to Submit Record"})


@xframe_options_exempt
@api_view(['GET','POST'])
def DisplaySubCategory(request):
  try:
    if request.method == 'GET':
      q = "select S.*,(select C.categoryname from paynrentapp_category C where C.id=S.cid) as categoryname from paynrentapp_subcategory S"
      print(q)
      cursor = connection.cursor()
      cursor.execute(q)
      records = tuple_to_dict.ParseDictMultipleRecord(cursor)
      print("xxxxxxxxxx",records)
      
      return render(request,'SubCategoryDisplay.html',{'data':records})
  except Exception as e:
       print("Error:",e)
       return render(request,'SubCategoryDisplay.html',{'data':{}})      



# @api_view(['GET','POST'])
# def DisplaySubCategory(request):
#   try:
#     if request.method == 'GET':
#       list_subcategory=SubCategory.objects.all()
#       list_subcategory_serializer=SubCategorySerializer(list_subcategory,many=True)
#       records=tuple_to_dict.ParseDict(list_subcategory_serializer.data)
#       # print(records)
      
#       return render(request,'SubCategoryDisplay.html',{'data':records})
#   except Exception as e:
#        print("Error:",e)
#        return render(request,'SubCategoryDisplay.html',{'data':{}})   

@xframe_options_exempt
@api_view(['GET','POST'])
def DisplayBySubCategoryId(request):
  try:
    if request.method == 'GET':
      q = "select S.*,(select C.categoryname from paynrentapp_category C where C.id=S.cid) as categoryname from paynrentapp_subcategory S where S.id={0}".format(request.GET['id'])
      cursor=connection.cursor()
      cursor.execute(q)
      record=tuple_to_dict.ParseDictSingleRecord(cursor)
      
    #   print("xxxx",record)
      
      return render(request,'DisplayByScid.html',{'data':record})
  except Exception as e:
       print("Error:",e)
       return render(request,'DisplayByScid.html',{'data':{}})
  
@xframe_options_exempt
@api_view(['GET','POST'])
def DisplayBySubCategoryIdByJSON(request):
  try:
    if request.method == 'GET':
      q="Select * from paynrentapp_subcategory where cid={0}".format(request.GET['cid'])
      cursor=connection.cursor()
      cursor.execute(q)
      record=tuple_to_dict.ParseDictMultipleRecord(cursor)
      
      print("xxxx",record)
      
      return JsonResponse(record,safe=False)
  except Exception as e:
       print("Error:",e)
       return JsonResponse([],safe=False)





#by this method we dont need to run query instead data is getting fetched to particular record we want
#this is ORM method but best for save and delete not helpful in joins

@xframe_options_exempt
@api_view(['GET','POST'])
def EditSubCategory(request):
   try:
      if request.method =='GET':
         if(request.GET['btn']=="EDIT"):
            subcategory=SubCategory.objects.get(pk=request.GET['id'])#hidden id
            subcategory.cid=request.GET['cid']
            subcategory.subcategoryname=request.GET['subcategoryname']
            subcategory.companyname=request.GET['companyname']
            subcategory.description=request.GET['description']
            subcategory.save()
         else:
            subcategory=SubCategory.objects.get(pk=request.GET['id'])
            subcategory.delete()

         return redirect('/api/displaysubcategory')
   except Exception as e:
      print("Error:",e)
      return redirect('/api/displaysubcategory')
   

@xframe_options_exempt
@api_view(['GET','POST'])
def DisplaySubCategoryIcon(request):
   try:
      if request.method =='GET':
         
         return render(request,'display_subcategory_icon.html',{'data':dict(request.GET)})
   except Exception as e:
      print("Error:",e)
      return render(request,'display_subcategory_icon.html',{'data':{}})

@xframe_options_exempt
@api_view(['GET','POST'])
def SubCategory_Save_icon(request):
  try:
    if request.method == 'POST':
      
       subcategory=SubCategory.objects.get(pk=request.POST['id'])
       subcategory.icon=request.FILES['icon']
       subcategory.save()
       
       return redirect('/api/displaysubcategory')
  except Exception as e:
     print("Error:",e)
     return redirect('/api/displaysubcategory') 
  

