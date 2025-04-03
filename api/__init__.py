from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Permite chamadas de diferentes origens (Cross-Origin)

    # Registra as rotas
    from . import routes
    app.register_blueprint(routes.bp)

    return app
