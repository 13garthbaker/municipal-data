import re

from abc import abstractmethod, ABC
from itertools import groupby, zip_longest
from functools import reduce
from contextlib import closing

from django.db.models import Q
from django.db import transaction


MONTH_TYPE_RE = re.compile(r"^M\d{2}$")

PERIOD_CODE_RE = re.compile(
    r"^(?P<year>\d{4})"
    r"(?P<type>IBY1|IBY2|ADJB|ORGB|AUDA|PAUD|ITY1|ITY2|TABB)?"
    r"(M(?P<month>\d{2}))?$"
)


def group_rows(rows, size):
    args = [iter(rows)] * size
    return zip_longest(*args)


def unique_records(rows):
    return set(
        map(
            lambda o: o[0],
            groupby(
                filter(None, rows),
                lambda o: (o.demarcation_code, o.period_code)
            ),
        )
    )


def period_code_details(code):
    match = PERIOD_CODE_RE.match(code)
    if match:
        details = match.groupdict()
        return (
            details["year"],
            details["type"] or "ACT",
            "month" if details["month"] else "year",
            details["month"] or details["year"],
        )
    else:
        return None


def all_to_code_dict(model):
    return dict(map(
        lambda o: (o.code, o),
        model.objects.all(),
    ))


def build_unique_query_params(keys):
    query_params = map(
        lambda k: Q(demarcation_code=k[0]) & Q(period_code=k[1]),
        keys,
    )
    query_params = reduce(
        lambda r, q: r | q,
        query_params,
        Q(),
    )
    return query_params


def delete_existing(update_obj, facts_cls, reader_cls, batch_size):
    """ Delete the existing matching records """
    deleted = 0
    update_obj.file.open('r')
    with closing(update_obj.file) as file:
        lines = iter(file)
        next(lines)  # Skip header
        reader = reader_cls(lines)
        for rows in group_rows(reader, batch_size):
            unique_keys = unique_records(rows)
            count, _ = facts_cls.objects.filter(
                build_unique_query_params(unique_keys)
            ).delete()
            deleted += count
    return deleted


class Updater(ABC):
    facts_cls = None
    reader_cls = None
    references_cls = {}

    def __init__(self, update_obj, batch_size):
        self.update_obj = update_obj
        self.batch_size = batch_size
        self.references = dict(
            map(
                lambda k, v: (k, all_to_code_dict(v)),
                self.references_cls.items(),
            )
        )

    @abstractmethod
    def row_to_obj(self, row):
        pass

    def update(self):
        with transaction.atomic():
            # Delete the existing matching records
            self.update_obj.deleted = 0
            self.update_obj.file.open('r')
            with closing(self.update_obj.file) as file:
                lines = iter(file)
                next(lines)  # Skip header
                reader = self.reader_cls(lines)
                for rows in group_rows(reader, self.batch_size):
                    unique_keys = unique_records(rows)
                    count, _ = self.facts_cls.objects.filter(
                        build_unique_query_params(unique_keys)
                    ).delete()
                    self.update_obj.deleted += count
            # Add the records from the dataset
            self.update_obj.inserted = 0
            self.update_obj.file.open('r')
            with closing(self.update_obj.file) as file:
                lines = iter(file)
                next(lines)  # Skip header
                reader = self.reader_cls(lines)
                for rows in group_rows(reader, self.batch_size):
                    objects = map(
                        self.row_to_obj,
                        filter(None, rows),
                    )
                    objects = self.facts_cls.objects.bulk_create(objects)
                    self.update_obj.inserted += len(objects)
            # Save the status of the update
            self.update_obj.save()
