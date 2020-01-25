from ariadne import ObjectType, gql

from jobs.models import Job

type_defs = gql(
    """
        type Job {
            id: UUID!
            summary: String
            budget: Int
            deadline: Date
            taken: Boolean
            done: Boolean
            timestamp: DateTime
        }
    """
)

job = ObjectType("Job")