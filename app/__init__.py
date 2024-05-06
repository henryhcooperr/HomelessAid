from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import the blueprint object from the routes module
    from .routes import bp as routes_bp
    # Register the blueprint with the Flask application
    app.register_blueprint(routes_bp)

    return app