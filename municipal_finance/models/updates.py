
from django.db import models

from django.contrib.auth.models import User


class BaseUpdate(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class MunicipalStaffContactsUpdate(BaseUpdate):
    file = models.FileField(
        upload_to='updates/municipal_staff_contacts/',
        max_length=255,
    )

    class Meta:
        db_table = 'municipal_staff_contacts_update'


class IncomeExpenditureV2Update(BaseUpdate):
    file = models.FileField(
        upload_to='updates/income_expenditure/',
        max_length=255,
    )
    deleted = models.BigIntegerField(null=True)
    inserted = models.BigIntegerField(null=True)

    class Meta:
        db_table = 'income_expenditure_update'
