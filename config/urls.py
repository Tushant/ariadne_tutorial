from django.contrib import admin
from django.urls import path
from ariadne.contrib.django.views import GraphQLView

from gql.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
     path('graphql/', GraphQLView.as_view(schema=schema), name='graphql'),
]
