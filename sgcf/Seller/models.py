from django.db import models
from Person.models import mdlPerson


# Create your models here.
class mdlSeller(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    person = models.ForeignKey(mdlPerson, models.DO_NOTHING, db_column='Person_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Seller'
