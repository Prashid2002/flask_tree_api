from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp
from routes.tree import tree_bp
from dotenv import load_dotenv
import os

# Load variables from .env (important for local dev)
load_dotenv()

app = Flask(__name__)
CORS(app)

# Load Mongo URI from environment
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

# Register routes
app.register_blueprint(auth_bp)
app.register_blueprint(tree_bp)

# Add a homepage route to confirm deployment
@app.route('/')
def index():
    return '✅ Flask Tree API is live and running!'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=10000)
