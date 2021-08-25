# from csvproject.csvapp.seralizers import SaveFileSerializer
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import NewShop
from csvapp.seralizers import FileUploadSerializer
from csvapp.seralizers import SaveFileSerializer
import io, csv, pandas as pd
from rest_framework.views import APIView

# Create your views here.


class UploadFileView(generics.CreateAPIView):
    serializer_class=FileUploadSerializer

    def post(self,request,*args,**kwargs):
        seralizer=self.get_serializer(data=request.data)
        seralizer.is_valid(raise_exception=True)
        file=seralizer.validated_data['file']
        reader=pd.read_csv(file)
        list=[]
        for index,row in reader.iterrows():
            shop_data={}
            # new_data=NewShop(action=row['action'],
            #               publisher_id=row['publisher_id'],
            #               timestamp=row['time_stamp'],
            #               shopper_id=row['shopper_id'],

            # 
            if row['action']=='SESSION_INIT':            
                    shop_data['action']=row['action']
                    shop_data['publisher_id']=row['publisher_id']
                    shop_data['time_stamp']=row['time_stamp']
                    shop_data['shopper_id']=row['shopper_id']
                    list.append(shop_data)
        # df=pd.DataFrame(list)
        # mydata=df.drop_duplicates()
        rem_list=[]
        for i in range(len(list)):
            if list[i] not in list[i+1:]:
                rem_list.append(list[i])
        
        print(rem_list)
        for data in rem_list:
            mydata=NewShop(action=data['action'],publisher_id=data['publisher_id'],timestamp=data['time_stamp'],shopper_id=data['shopper_id'])
            mydata.save()
                
        
        
        #     model_data=MyShop(action=data['action'],publisher_id=data['publisher_id'],
        #     timestamp=data['time_stamp'],shopper_id=data['shopper_id'])
        #     model_data.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)




class Data(APIView):

    def get(self, request, format=None):
        data = MyShop.objects.exclude(publisher_id="NULL")
      
        myshop_serializer = SaveFileSerializer(data, many=True, context={'request':request})
        data     =  {
            'data': myshop_serializer.data
        }
        return Response(data, status= status.HTTP_200_OK)




