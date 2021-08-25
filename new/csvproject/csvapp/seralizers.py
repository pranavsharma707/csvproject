from rest_framework import serializers
from .models import NewShop

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class SaveFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewShop
        fields = ['action','timestamp','publisher_id','shopper_id']