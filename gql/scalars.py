from uuid import UUID
from ariadne import ScalarType
from ariadne.contrib.django.scalars import date_scalar, datetime_scalar


type_defs = """
    scalar Date
    scalar DateTime
    scalar UUID
"""

uuid_scalar = ScalarType("UUID")


@datetime_scalar.serializer
def serialize_datetime(value):
    return value.isoformat()


@uuid_scalar.value_parser
def parse_uuid(value):
    return UUID(value)


@uuid_scalar.serializer
def serialize_uuid(value):
    return str(value)



scalar_types = [date_scalar, datetime_scalar, uuid_scalar]
