from ariadne import QueryType, gql

# Most of the fields for the query type are spread through files in the query module
type_defs = gql(
    """
    type Query
"""
)

query = QueryType()
