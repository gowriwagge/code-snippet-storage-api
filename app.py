from flask import Flask
from models import db
from database.db_setup import init_db
from routes.snippet_routes import snippet_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///snippets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)
app.register_blueprint(snippet_bp)

@app.route("/")
def home():
    return {"message": "Code Snippet Storage API is running!"}

if __name__ == '__main__':
    app.run(debug=True)
