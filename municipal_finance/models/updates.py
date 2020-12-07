
from django.db import models

from django.contrib.auth.models import User


class BaseUpdate(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class MunicipalStaffContactsUpdate(BaseUpdate):
    file = models.FileField(upload_to='uploads/municipal_staff_contacts/')

    class Meta:
        db_table = 'municipal_staff_contacts_update'
