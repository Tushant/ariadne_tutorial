from ariadne import gql

from jobs.models import Job
from gql.types.query.query_type import query

type_defs = gql(
    """
    extend type Query {
        getJobs: Jobs
    }

    type Jobs {
        data: [Job]!
    }
"""
)


@query.field("getJobs")
async def resolve_get_jobs(obj, info, id):
    jobs = Job.objects.all()
    return jobs
