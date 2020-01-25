from ariadne import gql

from django.contrib.auth import get_user_model
from gql.types.query.query_type import query

User = get_user_model()

type_defs = gql(
    """
    extend type Query {
        getUsers: Users
    }

    type Users {
        data: [User]!
    }
"""
)


@query.field("getUsers")
async def resolve_get_users(obj, info, id):
    users = User.objects.all()
    return users
