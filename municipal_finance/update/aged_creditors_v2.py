
import csv

from collections import namedtuple

from ..models import (
    AgedCreditorItemsV2,
    AgedCreditorFactsV2,
    AmountTypeV2,
)

from .utils import Updater, period_code_details


AgedCreditorRow = namedtuple(
    "AgedCreditorRow",
    (
        "demarcation_code",
        "period_code",
        "item_code",
        "amount",
    ),
)


class AgedCreditorReader(object):

    def __init__(self, data):
        self._reader = csv.reader(data)

    def __iter__(self):
        for row in map(AgedCreditorRow._make, self._reader):
            yield row


class AgedCreditorUpdater(Updater):
    facts_cls = AgedCreditorFactsV2
    reader_lcs = AgedCreditorReader
    references_cls = {
        'items': AgedCreditorItemsV2,
        'amount_types': AmountTypeV2,
    }

    def row_to_obj(self, row):
        (
            financial_year,
            amount_type_code,
            period_length,
            financial_period
        ) = period_code_details(row.period_code)
        amount = int(row.amount) if row.amount else None
        item = self.references["items"][row.item_code]
        amount_type = self.references["amount_types"][amount_type_code]
        return self.facts_cls(
            demarcation_code=row.demarcation_code,
            period_code=row.period_code,
            financial_year=financial_year,
            financial_period=financial_period,
            period_length=period_length,
            amount=amount,
            amount_type=amount_type,
            item=item,
        )


def update_aged_creditors_v2(update_obj, batch_size):
    updater = AgedCreditorUpdater(update_obj, batch_size)
    updater.update()
