from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp
from routes.tree import tree_bp

app = Flask(__name__)
CORS(app)

# Replace with your actual MongoDB URI
app.config['MONGO_URI'] = "mongodb+srv://prashid:pranusim0@cluster0.ha6azez.mongodb.net/"

app.register_blueprint(auth_bp)
app.register_blueprint(tree_bp)

if __name__ == '__main__':
    app.run(debug=True)