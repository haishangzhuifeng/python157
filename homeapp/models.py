# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    id = models.BigIntegerField(primary_key=True)
    consignee = models.CharField(max_length=50, blank=True, null=True)
    detailaddress = models.CharField(max_length=100, blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    mobilephone = models.CharField(max_length=20, blank=True, null=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    extend = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class Category(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    parent_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Orderitem(models.Model):
    id = models.BigIntegerField(primary_key=True)
    productname = models.CharField(db_column='productName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='orderid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderitem'


class Orders(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ordernumber = models.CharField(db_column='orderNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dateinproduct = models.DateTimeField(db_column='dateInProduct', blank=True, null=True)  # Field name made lowercase.
    freight = models.FloatField(blank=True, null=True)
    expenditure = models.FloatField(blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, db_column='address', blank=True, null=True)
    customer = models.ForeignKey('User', models.DO_NOTHING, db_column='customer', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Product(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    face = models.CharField(max_length=100, blank=True, null=True)
    publishing_house = models.CharField(max_length=50, blank=True, null=True)
    edition = models.SmallIntegerField(blank=True, null=True)
    publishing_time = models.DateTimeField(blank=True, null=True)
    print_time = models.SmallIntegerField(blank=True, null=True)
    isbn = models.CharField(max_length=30, blank=True, null=True)
    word = models.CharField(max_length=20, blank=True, null=True)
    number_of_page = models.IntegerField(blank=True, null=True)
    format_of_book = models.CharField(max_length=20, blank=True, null=True)
    paper = models.CharField(max_length=20, blank=True, null=True)
    packagin = models.CharField(max_length=20, blank=True, null=True)
    emboitement = models.CharField(max_length=10, blank=True, null=True)
    sales = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    dangdang_price = models.FloatField(blank=True, null=True)
    review = models.BigIntegerField(blank=True, null=True)
    issue = models.DateTimeField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    sold_out = models.CharField(max_length=10, blank=True, null=True)
    recommand = models.CharField(max_length=10, blank=True, null=True)
    extend = models.CharField(max_length=50, blank=True, null=True)
    cate = models.ForeignKey(Category, models.DO_NOTHING, db_column='cate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    extend = models.CharField(max_length=100, blank=True, null=True)
    c_time = models.DateTimeField(auto_now_add=True)
    has_check = models.BooleanField(default=False, verbose_name='是否确认')

    class Meta:
        managed = False
        db_table = 'user'

class Check_user(models.Model):
    code = models.CharField(max_length=256, verbose_name='用户注册码')
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='关联的用户')
    code_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'check_user'

