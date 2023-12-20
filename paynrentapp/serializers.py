from rest_framework import serializers 
from paynrentapp.models import Category
from paynrentapp.models import SubCategory
from paynrentapp.models import Vehicle
from paynrentapp.models import Administrator 
from paynrentapp.models import AddVehicle


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','categoryname','description','icon')

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id','cid','companyname','subcategoryname','description','icon')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id','cid','sid','modelyear','price','insured','registrationno','ownername','mobileno','color','fueltype','noofseats','transmissiontype','icon','variant')

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ('id','adminname','monileno','emailid','password')

class AddVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddVehicle
        fields = ('id','brand','segment','model_name','price','fueltype','noofseats','transmissiontype','icon','usericon')


 