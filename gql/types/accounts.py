from ariadne import ObjectType, gql

from django.contrib.auth import get_user_model

User = get_user_model()

type_defs = gql(
    """
        type User {
            id: UUID!
            email: String
            username: String
        }
    """
)

account = ObjectType("User")