# from csvproject.csvapp.seralizers import SaveFileSerializer
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Shop,Campaign
from csvapp.seralizers import FileUploadSerializer
from csvapp.seralizers import ShopSerializer
import io, csv, pandas as pd
from rest_framework.views import APIView
import time

# Create your views here.


class UploadFileView(generics.CreateAPIView):
    serializer_class=FileUploadSerializer

    def post(self,request,*args,**kwargs):
        start=time.time()
        seralizer=self.get_serializer(data=request.data)
        seralizer.is_valid(raise_exception=True)
        file=seralizer.validated_data['file']
        reader=pd.read_csv(file)
        #here we store all data of csv in the form of dictionary  in csv_data list where action=SESSION_INIT
        csv_data=[]
        for row in reader.iterrows():
            #here all data comes from csv and added to shop_data dictionary where action=SESSION_INIT
            shop_data={}
            
            if row['action']=='SESSION_INIT':            
                    shop_data['action']=row['action']
                    shop_data['publisher_id']=row['publisher_id']
                    shop_data['time_stamp']=row['time_stamp']
                    shop_data['shopper_id']=row['shopper_id']
                    shop_data['campaign_id']=row['campaign_id']
                    shop_data['aff_medium']=row['aff_medium']
                    shop_data['aff_term']=row['aff_term']
                    shop_data['aff_campaign']=row['aff_campaign']
                    shop_data['aff_content']=row['aff_content']
                    shop_data['parent_org']=row['parent_org']
                    #here all data store in shop_data dictionary and then this dictionary is store in csv_data list
                    csv_data.append(shop_data)

        
        remove_duplicate=[]
        #data comes from list and check every record for  duplicate of shopper_id and if shopper_id is duplicate in list then it is not add
        #otherwise it is add into remove_duplicate list
        for data in range(len(list)):
            if csv_data[data] not in csv_data[data+1:]:
                remove_duplicate.append(remove_duplicate[data])
        
        #here data from remove_duplicate list means action,publisher_id,timestamp,shopper_id added to Shop Tabel
        #And campaign_id,aff_medium,aff_term,aff_campaign,aff_content,parent_org added to Campaign Model
        for data in remove_duplicate:
            shop_data=Shop(action=data['action'],publisher_id=data['publisher_id'],timestamp=data['time_stamp'],shopper_id=data['shopper_id'])
            campaign_data=Campaign(campaign_id=data['campaign_id'],aff_medium=data['aff_medium'],
            aff_term=data['aff_term'],aff_campaign=data['aff_campaign'],
            aff_content=data['aff_content'],parent_org=data['parent_org'])
            shop_data.save()
            campaign_data.save()
        end=time.time() 

        return Response({"status": "success","response_time":end-start},
                        status.HTTP_201_CREATED)




class GetData(APIView):

    def get(self, request, format=None):
        # Here we get all the data from shop table and display to end user as response
        data = Shop.objects.all()
        #Here we use ShopSerializer for serialize data from shop table and send serialize data to end user. 
        shop_serializer = ShopSerializer(data, many=True, context={'request':request})
        data     =  {
            'data': shop_serializer.data
        }
        return Response(data, status= status.HTTP_200_OK)




