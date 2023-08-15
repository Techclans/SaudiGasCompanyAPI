# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class City(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    citynameen = models.CharField(db_column='CityNameEn', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    citynamear = models.CharField(db_column='CityNameAr', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'City'


class Collectionagent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    agentname = models.CharField(db_column='AgentName', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    addrline1 = models.CharField(db_column='AddrLine1', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    addrline2 = models.CharField(db_column='AddrLine2', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='City_ID')  # Field name made lowercase.
    coordinates = models.CharField(db_column='Coordinates', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CollectionAgent'


class Customer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    agent = models.ForeignKey(Collectionagent, models.DO_NOTHING, db_column='Agent_ID')  # Field name made lowercase.
    person = models.ForeignKey('Person', models.DO_NOTHING, db_column='Person_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customer'


class Delivarysatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    delivarysatusen = models.CharField(db_column='DelivarySatusEn', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    delivarysatusar = models.CharField(db_column='DelivarySatusAR', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DelivarySatus'


class Invoice(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    invoicenumber = models.CharField(db_column='InvoiceNumber', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    invoiceamount = models.FloatField(db_column='InvoiceAmount', blank=True, null=True)  # Field name made lowercase.
    paidamount = models.FloatField(db_column='PaidAmount', blank=True, null=True)  # Field name made lowercase.
    order = models.ForeignKey('Order', models.DO_NOTHING, db_column='Order_ID')  # Field name made lowercase.
    ispaid = models.BooleanField(db_column='IsPaid', blank=True, null=True)  # Field name made lowercase.
    invoicestatus = models.IntegerField(db_column='InvoiceStatus', blank=True, null=True)  # Field name made lowercase.
    status = models.ForeignKey('Invoicestatus', models.DO_NOTHING, db_column='Status_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Invoice'


class Invoicestatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    statusnameen = models.CharField(db_column='StatusNameEn', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    statusnamear = models.CharField(db_column='StatusNameAr', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvoiceStatus'


class Lookup(models.Model):
    sysid = models.AutoField(db_column='SysId', primary_key=True)  # Field name made lowercase.
    tablenameen = models.CharField(db_column='TableNameEn', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tablenamear = models.CharField(db_column='TableNameAr', max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lookup'


class Order(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orderqty = models.IntegerField(db_column='OrderQty', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    orderamount = models.FloatField(db_column='OrderAmount', blank=True, null=True)  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='Product_ID')  # Field name made lowercase.
    ordertotalamount = models.FloatField(db_column='OrderTotalAmount', blank=True, null=True)  # Field name made lowercase.
    vatamount = models.FloatField(db_column='VatAmount', blank=True, null=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer_ID')  # Field name made lowercase.
    qrcode = models.CharField(db_column='QRCode', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Order'


class Payment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    receiptno = models.CharField(db_column='ReceiptNo', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    receiptamount = models.FloatField(db_column='ReceiptAmount', blank=True, null=True)  # Field name made lowercase.
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING, db_column='Invoice_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment'


class Person(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mname = models.CharField(db_column='MName', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    age = models.SmallIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    citycode = models.ForeignKey(City, models.DO_NOTHING, db_column='CityCode')  # Field name made lowercase.
    mobileno = models.CharField(db_column='MobileNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    socialid = models.CharField(db_column='SocialId', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailId', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person'


class Plandelivary(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    plandate = models.DateTimeField(db_column='PlanDate', blank=True, null=True)  # Field name made lowercase.
    expecteddelivary = models.DateTimeField(db_column='ExpectedDelivary', blank=True, null=True)  # Field name made lowercase.
    order = models.ForeignKey(Order, models.DO_NOTHING, db_column='Order_ID')  # Field name made lowercase.
    collectionagent = models.ForeignKey(Collectionagent, models.DO_NOTHING, db_column='CollectionAgent_ID')  # Field name made lowercase.
    delivarysatus = models.ForeignKey(Delivarysatus, models.DO_NOTHING, db_column='DelivarySatus_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlanDelivary'


class Product(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productnameen = models.CharField(db_column='ProductNameEn', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    productnamear = models.CharField(db_column='ProductNameAr', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    productprice = models.IntegerField(db_column='ProductPrice', blank=True, null=True)  # Field name made lowercase.
    productsize = models.SmallIntegerField(db_column='ProductSize', blank=True, null=True)  # Field name made lowercase.
    sizeunit = models.CharField(db_column='SizeUnit', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    productdiscriptionen = models.CharField(db_column='ProductDiscriptionEn', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    productdiscriptionar = models.CharField(db_column='ProductDiscriptionAr', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.SmallIntegerField(db_column='VATPercentage', blank=True, null=True)  # Field name made lowercase.
    hcmcode = models.CharField(db_column='HCMCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product'


class Seller(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    person = models.ForeignKey(Person, models.DO_NOTHING, db_column='Person_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Seller'


class Shipment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    vendorname = models.CharField(db_column='VendorName', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vendoraddr1 = models.CharField(db_column='VendorAddr1', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    plandelivary = models.ForeignKey(Plandelivary, models.DO_NOTHING, db_column='PlanDelivary_ID')  # Field name made lowercase.
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='City_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Shipment'


class Userinfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=75, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='PersonID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserInfo'


class Usertype(models.Model):
    sysid = models.AutoField(db_column='SysId', primary_key=True)  # Field name made lowercase.
    usertypenameen = models.CharField(db_column='UserTypeNameEn', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usertypenamear = models.CharField(db_column='UserTypeNameAr', max_length=400, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserType'


class AccountCustomgroup(models.Model):
    group_ptr = models.OneToOneField('AuthGroup', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'account_customgroup'


class AccountCustompermission(models.Model):
    permission_ptr = models.OneToOneField('AuthPermission', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'account_custompermission'


class AccountUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    tc = models.BooleanField()
    is_active = models.BooleanField()
    is_admin = models.BooleanField()
    is_superuser = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    mobile_number = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'account_user'


class AccountUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_user_groups'
        unique_together = (('user', 'group'),)


class AccountUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    created = models.DateTimeField()
    user = models.OneToOneField(AccountUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
