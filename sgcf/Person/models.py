from django.db import models
from City.models import mdlCity

# Create your models here.
class mdlPerson(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mname = models.CharField(db_column='MName', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    age = models.SmallIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    citycode = models.ForeignKey(mdlCity, models.DO_NOTHING, db_column='CityCode')  # Field name made lowercase.
    mobileno = models.CharField(db_column='MobileNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    socialid = models.CharField(db_column='SocialId', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailId', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person'
        