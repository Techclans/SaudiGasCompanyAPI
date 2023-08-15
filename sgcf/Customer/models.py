from django.db import models

# Create your models here.

class mdlCustomer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
   # agent = models.ForeignKey(Collectionagent, models.DO_NOTHING, db_column='Agent_ID')  # Field name made lowercase.
    person = models.ForeignKey('Person', models.DO_NOTHING, db_column='Person_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customer'
