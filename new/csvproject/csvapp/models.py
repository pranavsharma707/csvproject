from django.db import models


class Shop(models.Model):
    action=models.CharField(max_length=266,null=True,blank=True)
    timestamp=models.CharField(max_length=266,null=True,blank=True)
    publisher_id=models.CharField(max_length=266,null=True,blank=True)
    shopper_id=models.CharField(max_length=266,null=True,blank=True)


class Campaign(models.Model):
    campaign_id=models.CharField(max_length=266,null=True,blank=True)
    aff_medium=models.CharField(max_length=266,null=True,blank=True)
    aff_term=models.CharField(max_length=266,null=True,blank=True)
    aff_campaign=models.CharField(max_length=266,null=True,blank=True)
    aff_content=models.CharField(max_length=266,null=True,blank=True)
    parent_org=models.CharField(max_length=266,null=True,blank=True)
    