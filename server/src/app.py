from flask import Flask, request
from flask_migrate import Migrate

from .config import DATABASE_URI
from .database import db
from .models import Todo, TodoSchema


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI

db.init_app(app)
migrate = Migrate(app, db)


@app.get("/todos")
def todos():
    return {
        "todos": TodoSchema().dump(Todo.query.all(), many=True),
    }


@app.post("/todos")
def create_todo():
    title = request.json.get("title")
    description = request.json.get("description")

    if title is None or description is None:
        return {"message": "Title and description fields are required"}, 422

    todo = Todo(title=title, description=description)
    db.session.add(todo)
    db.session.commit()

    response = {
        "message": f"Todo saved successfully",
        "todo": TodoSchema().dump(todo),
    }

    return response, 201


@app.delete("/todos/<int:id>")
def delete_todo(id: int):
    affected_rows = Todo.query.filter_by(id=id).delete()
    db.session.commit()

    if affected_rows == 0:
        return {"message": "Not found"}, 404

    return {"message": "Todo deleted successfully"}
