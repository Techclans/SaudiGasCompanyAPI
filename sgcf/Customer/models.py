from django.db import models
from City.models import mdlCity
from Person.models import mdlPerson

# Create your models here.

class mdlCustomer(models.Model):
    sysid = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    addrline1 = models.CharField(db_column='AddrLine1', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    addrline2 = models.CharField(db_column='AddrLine2', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coordinates = models.CharField(db_column='Coordinates', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.ForeignKey(mdlCity, models.DO_NOTHING, db_column='City_ID')  # Field name made lowercase.
    person = models.ForeignKey(mdlPerson, models.DO_NOTHING, db_column='Person_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customer'

        
