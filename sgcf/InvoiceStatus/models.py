from django.db import models

# Create your models here.
class mdlInvoiceStatus(models.Model):
    sysid = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    nameen = models.CharField(db_column='StatusNameEn', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    namear = models.CharField(db_column='StatusNameAr', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvoiceStatus'
