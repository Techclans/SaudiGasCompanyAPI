from django.db import models

# Create your models here.
class UserType(models.Model):
    sysid = models.AutoField(db_column='SysId', primary_key=True)  # Field name made lowercase.
    nameen = models.CharField(db_column='UserTypeNameEn', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    namear = models.CharField(db_column='UserTypeNameAr', max_length=400, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'UserType'
