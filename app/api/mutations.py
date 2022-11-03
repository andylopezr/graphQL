from datetime import datetime
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import User

@convert_kwargs_to_snake_case
def create_user_resolver(obj, info, first_name, last_name, address, recommended):
    try:
        current_date = datetime.today().date()
        user = User(
            first_name=first_name, 
            last_name=last_name, 
            address=address, 
            recommended=recommended
        )
        db.session.add(user)
        db.session.commit()
        payload = {
            "success": True,
            "user": user.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload

@convert_kwargs_to_snake_case
def update_user_resolver(obj, info, id, first_name, last_name, address, recommended):
    try:
        user = User.query.get(id)
        if user:
            user.first_name = first_name
            user.last_name = last_name
            user.address = address
            user.recommended = recommended
        db.session.add(user)
        db.session.commit()
        payload = {
            "success": True,
            "user": user.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def delete_user_resolver(obj, info, id):
    try:
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        payload = {"success": True, "user": user.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["ID Not found"]
        }
    return payload