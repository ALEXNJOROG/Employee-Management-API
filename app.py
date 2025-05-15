from flask import Flask
from models import db
from schemas import ma
from routes import routes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
ma.init_app(app)
app.register_blueprint(routes)

@app.route('/')
def home():
    return "Welcome to the Employee Management API"


if __name__ == "__main__":
    # Create tables before the app starts
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=5000)
