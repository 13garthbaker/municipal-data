from import_export import resources

from .models import (
    AmountType,
    AmountTypeV2,
    CflowItemsV1,
    CflowItemsV2,
    CflowFactsV1,
    CflowFactsV2,
    GovernmentFunctionsV1,
    GovernmentFunctionsV2,
    IncexpItemsV1,
    IncexpItemsV2,
    IncexpFactsV1,
    IncexpFactsV2,
    BsheetItemsV1,
    BsheetItemsV2,
    CapitalTypeV2,
    CapitalItemsV1,
    CapitalItemsV2,
    ConditionalGrantTypesV1,
    GrantTypesV2,
    RepairsMaintenanceItemsV1,
    RepairsMaintenanceItemsV2,
    RepairsMaintenanceFactsV2,
    AgedDebtorItemsV1,
    AgedDebtorItemsV2,
    AgedCreditorItemsV1,
    AgedCreditorItemsV2,
)


class AmountTypeV1Resource(resources.ModelResource):
    class Meta:
        model = AmountType
        import_id_fields = ['code']


class AmountTypeV2Resource(resources.ModelResource):
    class Meta:
        model = AmountTypeV2
        import_id_fields = ['code']


class CashflowItemsV1Resource(resources.ModelResource):
    class Meta:
        model = CflowItemsV1
        import_id_fields = ['code']


class CashflowItemsV2Resource(resources.ModelResource):
    class Meta:
        model = CflowItemsV2
        import_id_fields = ['code']


class GovernmentFunctionsV1Resource(resources.ModelResource):
    class Meta:
        model = GovernmentFunctionsV1
        import_id_fields = ['code']


class GovernmentFunctionsV2Resource(resources.ModelResource):
    class Meta:
        model = GovernmentFunctionsV2
        import_id_fields = ['code']


class IncexpItemsV1Resource(resources.ModelResource):
    class Meta:
        model = IncexpItemsV1
        import_id_fields = ['code']


class IncexpItemsV2Resource(resources.ModelResource):
    class Meta:
        model = IncexpItemsV2
        import_id_fields = ['code']


class BsheetItemsV1Resource(resources.ModelResource):
    class Meta:
        model = BsheetItemsV1
        import_id_fields = ['code']


class FinancialPositionItemsV2Resource(resources.ModelResource):
    class Meta:
        model = BsheetItemsV2
        import_id_fields = ['code']


class CapitalTypeV2Resource(resources.ModelResource):
    class Meta:
        model = CapitalTypeV2
        import_id_fields = ['code']


class CapitalItemsV1Resource(resources.ModelResource):
    class Meta:
        model = CapitalItemsV1
        import_id_fields = ['code']


class CapitalItemsV2Resource(resources.ModelResource):
    class Meta:
        model = CapitalItemsV2
        import_id_fields = ['code']


class ConditionalGrantTypesV1Resource(resources.ModelResource):
    class Meta:
        model = ConditionalGrantTypesV1
        import_id_fields = ['code']


class GrantTypesV2Resource(resources.ModelResource):
    class Meta:
        model = GrantTypesV2
        import_id_fields = ['code']


class RepairsMaintenanceItemsV1Resource(resources.ModelResource):
    class Meta:
        model = RepairsMaintenanceItemsV1
        import_id_fields = ['code']


class RepairsMaintenanceItemsV2Resource(resources.ModelResource):
    class Meta:
        model = RepairsMaintenanceItemsV2
        import_id_fields = ['code']


class AgedDebtorItemsV1Resource(resources.ModelResource):
    class Meta:
        model = AgedDebtorItemsV1
        import_id_fields = ['code']


class AgedDebtorItemsV2Resource(resources.ModelResource):
    class Meta:
        model = AgedDebtorItemsV2
        import_id_fields = ['code']


class AgedCreditorItemsV1Resource(resources.ModelResource):
    class Meta:
        model = AgedCreditorItemsV1
        import_id_fields = ['code']


class AgedCreditorItemsV2Resource(resources.ModelResource):
    class Meta:
        model = AgedCreditorItemsV2
        import_id_fields = ['code']


class IncexpFactsV1Resource(resources.ModelResource):
    class Meta:
        model = IncexpFactsV1
        import_id_fields = [
            'demarcation_code',
            'period_code',
            'item_code',
            'function_code',
        ]


class IncexpFactsV2Resource(resources.ModelResource):
    class Meta:
        model = IncexpFactsV2
        import_id_fields = [
            'demarcation_code',
            'period_code',
            'item',
            'function',
        ]


class CashFlowFactsV1Resource(resources.ModelResource):
    class Meta:
        model = CflowFactsV1
        import_id_fields = [
            'demarcation_code',
            'period_code',
            'item_code',
        ]


class CashFlowFactsV2Resource(resources.ModelResource):
    class Meta:
        model = CflowFactsV2
        import_id_fields = [
            'demarcation_code',
            'period_code',
            'item',
        ]


class RepairsMaintenanceFactsV2Resource(resources.ModelResource):
    class Meta:
        model = RepairsMaintenanceFactsV2
        import_id_fields = [
            'demarcation_code',
            'period_code',
            'item',
        ]
