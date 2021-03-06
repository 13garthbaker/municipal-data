
from django.db import models

from django.contrib.auth.models import User


def upload_to(path):
    def get_file_path(instance, filename):
        ext = filename.split(".")[-1]
        timestamp = instance.datetime.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{path}{timestamp}.{ext}"
        return filename
    return get_file_path


class BaseUpdate(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    datetime = models.DateTimeField(auto_now_add=True)
    deleted = models.BigIntegerField(null=True)
    inserted = models.BigIntegerField(null=True)

    class Meta:
        abstract = True


class MunicipalStaffContactsUpdate(BaseUpdate):
    file = models.FileField(
        upload_to=upload_to('updates/municipal_staff_contacts/'),
        max_length=255,
    )

    class Meta:
        db_table = 'municipal_staff_contacts_update'


class IncomeExpenditureV2Update(BaseUpdate):
    file = models.FileField(
        upload_to=upload_to('updates/income_expenditure_v2/'),
        max_length=255,
    )

    class Meta:
        db_table = 'income_expenditure_v2_update'


class CashFlowV2Update(BaseUpdate):
    file = models.FileField(
        upload_to=upload_to('updates/cash_flow_v2/'),
        max_length=255,
    )

    class Meta:
        db_table = 'cash_flow_v2_update'


class RepairsMaintenanceV2Update(BaseUpdate):
    file = models.FileField(
        upload_to=upload_to('updates/repairs_maintenance_v2/'),
        max_length=255,
    )

    class Meta:
        db_table = 'repairs_maintenance_v2_update'
