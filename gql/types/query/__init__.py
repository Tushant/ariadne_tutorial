from .jobs.get_jobs import type_defs as get_jobs_type_defs
from .accounts.get_users import type_defs as get_users_type_defs

from .query_type import query

type_defs_list = [
    get_jobs_type_defs,
    get_users_type_defs
]

type_list = [query]