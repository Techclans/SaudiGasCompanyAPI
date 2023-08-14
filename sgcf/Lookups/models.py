from django.db import models

# Create your models here.

class Lookup(models.Model):
    sysid = models.AutoField(db_column='SysId', primary_key=True)  # Field name made lowercase.
    nameen = models.CharField(db_column='TableNameEn', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    namear = models.CharField(db_column='TableNameAr', max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Lookup'
