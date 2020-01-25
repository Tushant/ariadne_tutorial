from ariadne import make_executable_schema

from gql.types import type_defs_list, type_list
from gql.scalars import type_defs as scalar_type_defs, scalar_types


schema = make_executable_schema(
    [scalar_type_defs, *type_defs_list], [*scalar_types, *type_list]
)

