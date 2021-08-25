# from csvproject.csvapp.seralizers import SaveFileSerializer
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Compaign, NewShop
from csvapp.seralizers import FileUploadSerializer
from csvapp.seralizers import SaveFileSerializer
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
        list=[]
        for index,row in reader.iterrows():
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
                    list.append(shop_data)
        # df=pd.DataFrame(list)
        # mydata=df.drop_duplicates()
        # print(mydata)
        
        rem_list=[]
        for i in range(len(list)):
            if list[i] not in list[i+1:]:
                rem_list.append(list[i])

        for data in rem_list:
            mydata=NewShop(action=data['action'],publisher_id=data['publisher_id'],timestamp=data['time_stamp'],shopper_id=data['shopper_id'])
            compaign_data=Compaign(campaign_id=data['campaign_id'],aff_medium=data['aff_medium'],
            aff_term=data['aff_term'],aff_campaign=data['aff_campaign'],
            aff_content=data['aff_content'],parent_org=data['parent_org'])
            mydata.save()
            compaign_data.save()
        end=time.time() 

        return Response({"status": "success","response_time":end-start},
                        status.HTTP_201_CREATED)




class GetData(APIView):

    def get(self, request, format=None):
        data = NewShop.objects.all()
      
        newshop_serializer = SaveFileSerializer(data, many=True, context={'request':request})
        data     =  {
            'data': newshop_serializer.data
        }
        return Response(data, status= status.HTTP_200_OK)




