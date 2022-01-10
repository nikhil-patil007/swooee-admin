from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
from datetime import datetime

# "0" Is Activate & "1" Is Deactivate
# Create your models here.

class Admin_user(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.username 

    
    
class User(models.Model):
    username = models.CharField(max_length=25,unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='email', max_length=255, unique=True, db_index=True)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=datetime.now, null=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, null=True, blank=True)
    checkbox = models.CharField(max_length=1,default='Not Verified')
    Image = models.ImageField(upload_to="userimages/",default='default-product.png', blank=True)
    status = models.CharField(max_length=1,default=0)
    
    def __str__(self):
        nameq = f'{self.first_name} {self.last_name}'
        return nameq
    

class Categories(MPTTModel):
    id = models.AutoField(primary_key=True)
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='child', on_delete=models.PROTECT)
    category = models.CharField(max_length=255, db_index=True)
    slug = AutoSlugField(populate_from='category', max_length=255, unique=True, db_index=True)
    created_at = models.DateTimeField(default=datetime.now, null=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, null=True, blank=True)
    Image = models.ImageField(upload_to="categoryimages/",default='default-product.png', blank=True)
    status = models.CharField(max_length=1,default=0)

    def __str__(self):
        return self.category
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', max_length=255, unique=True, db_index=True)
    discription = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, null=True, on_delete=models.SET_NULL)
    Image = models.ImageField(upload_to="productimages/",default="abc.jpg", blank=True)
    created_at = models.DateTimeField(default=datetime.now, null=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, null=True, blank=True)
    # Product Link Start Here
    # Amazon
    amazon = models.CharField(max_length=200)
    amazon_sell_price = models.CharField(max_length=20)
    amazon_MRP = models.CharField(max_length=20)
    # Awin
    awin = models.CharField(max_length=200)
    awin_sell_price = models.CharField(max_length=20)
    awin_MRP = models.CharField(max_length=20)
    # Ebay
    ebay = models.CharField(max_length=200)
    ebay_sell_price = models.CharField(max_length=20)
    ebay_MRP = models.CharField(max_length=20)
    # Walmart
    walmart = models.CharField(max_length=200)
    walmart_sell_price = models.CharField(max_length=20)
    walmart_MRP = models.CharField(max_length=20)
    # Youtube
    youtube = models.CharField(max_length=200)    
    # Product Link End Here
    status = models.CharField(max_length=1,default=0)
    
    def __str__(self):
        return self.name
    
class Static_page(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', max_length=255, unique=True, db_index=True)
    contain = RichTextField()
    Image = models.ImageField(upload_to="staticPages/",default="abc.jpg", blank=True)
    created_at = models.DateTimeField(default=datetime.now, null=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, null=True, blank=True)
    status = models.CharField(max_length=1,default=0)
    
    def __str__(self):
        return self.title
    
class Banner(models.Model):
    short_title =  models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='short_title', max_length=255, unique=True, db_index=True)
    contain = RichTextField()
    file = models.FileField(upload_to="Banners/",default='img.jpg', blank=True)
    extension = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now, null=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, null=True, blank=True)
    status = models.CharField(max_length=1,default=0)
    
    def __str__(self):
        return self.short_title