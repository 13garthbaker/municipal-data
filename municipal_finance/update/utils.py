import re

from itertools import groupby, zip_longest
from functools import reduce

from django.db.models import Q


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
