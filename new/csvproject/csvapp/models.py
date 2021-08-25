from django.db import models

# Create your models here.
# class Shop(models.Model):
#     action=models.CharField(max_length=266,null=True,blank=True)
#     timestamp=models.CharField(max_length=266,null=True,blank=True)
#     publisher_id=models.CharField(max_length=266,null=True,blank=True)
#     shopper_id=models.CharField(max_length=266,null=True,blank=True)



# class New(models.Model):
#     action=models.CharField(max_length=266,null=True,blank=True)
#     timestamp=models.CharField(max_length=266,null=True,blank=True)
#     publisher_id=models.CharField(max_length=266,null=True,blank=True)
#     shopper_id=models.CharField(max_length=266,null=True,blank=True)


# class NewShop(models.Model):
    # action=models.CharField(max_length=266,null=True,blank=True)
    # timestamp=models.CharField(max_length=266,null=True,blank=True)
    # publisher_id=models.CharField(max_length=266,null=True,blank=True)
    # shopper_id=models.CharField(max_length=266,null=True,blank=True)

# class MyShop(models.Model):
    # action=models.CharField(max_length=266,null=True,blank=True)
    # timestamp=models.CharField(max_length=266,null=True,blank=True)
    # publisher_id=models.CharField(max_length=266,null=True,blank=True)
    # shopper_id=models.CharField(max_length=266,null=True,blank=True)

class NewShop(models.Model):
    action=models.CharField(max_length=266,null=True,blank=True)
    timestamp=models.CharField(max_length=266,null=True,blank=True)
    publisher_id=models.CharField(max_length=266,null=True,blank=True)
    shopper_id=models.CharField(max_length=266,null=True,blank=True)