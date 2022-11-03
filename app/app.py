from api import app, db
from ariadne import (
    load_schema_from_path, 
    make_executable_schema,
    graphql_sync, 
    snake_case_fallback_resolvers, 
    ObjectType)
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import list_users_resolver, get_user_resolver
from api.mutations import (
    create_user_resolver, 
    update_user_resolver, 
    delete_user_resolver)

# Flask application context
app.app_context().push()


query = ObjectType("Query")
query.set_field("list_users", list_users_resolver)
query.set_field("get_user", get_user_resolver)

mutation = ObjectType("Mutation")
mutation.set_field("create_user", create_user_resolver)
mutation.set_field("update_user", update_user_resolver)
mutation.set_field("delete_user", delete_user_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs,
    query,
    mutation,
    snake_case_fallback_resolvers)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

