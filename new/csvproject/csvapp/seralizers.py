from rest_framework import serializers
from .models import Shop

class FileUploadSerializer(serializers.Serializer):
    #This serializer is used for upload a file and used in UploadFileView Class in views.py
    file = serializers.FileField()


class ShopSerializer(serializers.ModelSerializer):
    #This serializer is used for serialize data comes from Shop Table and used in GetData class.
    class Meta:
        model = Shop
        fields = ['action','timestamp','publisher_id','shopper_id']