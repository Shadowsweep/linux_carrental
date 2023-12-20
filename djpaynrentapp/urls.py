"""djpaynrentapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from paynrentapp import category_view
from paynrentapp import SubCategory_view
from paynrentapp import Vehicle_view
from paynrentapp import admin_login
from paynrentapp import user_view
from paynrentapp import addvehicle_view


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/categoryinterface',category_view.CategoryInterface),
    re_path(r'^api/categorysubmit/$',category_view.CategorySubmit),
    re_path(r'^api/displaycategory/$',category_view.DisplayCategory),
    re_path(r'^api/display_category_by_id/$',category_view.DisplayByCategoryId),
    re_path(r'^api/categoryedit/$',category_view.EditCategory),
    re_path(r'^api/display_category_icon/$',category_view.DisplayCategoryIcon),
    re_path(r'^api/category_save_icon/$',category_view.Category_Save_icon),
    re_path(r'^api/json_displaycategory/$',category_view.DisplayCategoryJSON),
    
    #######Subcategory########
    
    re_path(r'^api/subcategoryinterface/$',SubCategory_view.SubCategoryInterface),
    re_path(r'^api/subcategorysubmit',SubCategory_view.SubCategorySubmit),
    re_path(r'^api/displaysubcategory/$',SubCategory_view.DisplaySubCategory),
    re_path(r'^api/display_subcategory_by_id/$',SubCategory_view.DisplayBySubCategoryId),
    re_path(r'^api/subcategoryedit/$',SubCategory_view.EditSubCategory),
    re_path(r'^api/display_subcategory_icon/$',SubCategory_view.DisplaySubCategoryIcon),
    re_path(r'^api/subcategory_save_icon/$',SubCategory_view.SubCategory_Save_icon),
    re_path(r'^api/jsondisplaysubcategory/$',SubCategory_view.DisplayBySubCategoryIdByJSON),

    ######vehicle#####
    
    re_path(r'^api/vehicleinterface',Vehicle_view.VehicleInterface),
    re_path(r'^api/vehiclesubmit',Vehicle_view.VehicleSubmit),
    re_path(r'^api/displayvehicle/$',Vehicle_view.DisplayVehicle),
    re_path(r'^api/display_vehicle_by_id',Vehicle_view.DisplayByVehicleId),
    re_path(r'^api/vehicleedit/$',Vehicle_view.EditVehicle),
    re_path(r'^api/display_vehicle_icon/$',Vehicle_view.DisplayVehicleIcon),
    re_path(r'^api/vehicle_save_icon',Vehicle_view.Vehicle_Save_icon),


    ############## Admin ##########

    re_path(r'^api/adminlogin',admin_login.AdminLogin),
    re_path(r'^api/checkadminlogin',admin_login.CheckAdminLogin),
    re_path(r'^api/index',user_view.Index),
    re_path(r'^api/test',user_view.DisplayVehicleForUsers),
    re_path(r'^api/uservehiclelist',user_view.PageUserVehicleList),
    re_path(r'^api/selectedvehicle',user_view.DisplaySelectedVehicle),
    re_path(r'^api/showvehiclelist',user_view.ShowVehicleList),
    re_path(r'^api/setemailmobile',user_view.SetMobileAndEmail),


   ############### AddVehicle ############
    re_path(r'^api/addvehicleinterface/$',addvehicle_view.AddVehicleInterface),
    re_path(r'^api/addvehiclesubmit',addvehicle_view.AddVehicleSubmit),
    re_path(r'^api/adddisplayvehicle/$',addvehicle_view.DisplayAddVehicle),
    # re_path(r'^api/adddisplay_vehicle_by_id/$',addvehicle_view.DisplayByAddVehicleId),
    # re_path(r'^api/addvehicleedit/$',addvehicle_view.EditAddVehicle),
    # re_path(r'^api/adddisplay_vehicle_icon/$',addvehicle_view.DisplayVehicleIcon),
    # re_path(r'^api/addvehicle_save_icon/$',addvehicle_view.Vehicle_Save_icon),
    # re_path(r'^api/jsondisplayaddvehicle/$',addvehicle_view.DisplayAddVehicleJSON)
]
