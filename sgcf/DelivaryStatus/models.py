from django.db import models

# Create your models here.
class mdlDelivarStatus(models.Model):
    sysid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nameen = models.CharField(db_column='DelivarySatusEn', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    namear = models.CharField(db_column='DelivarySatusAR', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DelivarySatus'
