from .query import type_defs_list as query_type_defs_list, type_list as query_type_list
from .accounts import type_defs as account_type_defs, account
from .jobs import type_defs as job_type_defs, job

type_list = [
    *query_type_list,
    account,
    job
]


type_defs_list = [
    *query_type_defs_list,
    account_type_defs,
    job_type_defs
]

