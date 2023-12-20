from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view

from paynrentapp.serializers import AdministratorSerializer
from paynrentapp.models import Administrator
from . import tuple_to_dict

@api_view(['GET','POST','DELETE'])
def AdminLogin(request):
    return render(request,"AdminLogin.html",{'message':''})

@api_view(['GET','POST','DELETE'])
def CheckAdminLogin(request):
    try:
        if request.method == 'GET':
            q = "select * from  paynrentapp_administrator  where (mobileno='{0}' or emailid='{0}') and password='{1}'".format(request.GET['mobileno'],request.GET['password'])

            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictSingleRecord(cursor)
            print("check",record)
            if(len(record)==0):
                
                return render(request,"AdminLogin.html",{'message':"Invalid Adminid/Password"})
            else:
    
                print("xxxxxxxxxx",record)
            return render(request,"DashBoard.html",{'data':record})
    except Exception as e:
        print("Error : ",e)
        return render(request,"DashBoard.html",{'data':[]})
   

