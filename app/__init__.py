from flask import Flask
from app.models import db ## usingh the dot function . # using the absolute form. from app.models import db
from app.extensions import ma, limiter #using the absolute from
from app.blueprints.customers import customers_bp
from app.blueprints.service_tickets import service_tickets_bp
from app.blueprints.mechanics import mechanics_bp
from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = '/api/docs'

API_URL = '/static/swagger.yaml'

swagger_bp = get_swaggerui_blueprint(SWAGGER_URL, API_URL,  config={'app_name': "Library API"})

def create_app(config_name):

    app= Flask(__name__)
    app.config.from_object(f'config.{config_name}')


    #add extension
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)


    ## register blueprint
    app.register_blueprint(customers_bp, url_prefix = "/customers")
    app.register_blueprint(service_tickets_bp, url_prefix = "/servicetickets")
    app.register_blueprint(mechanics_bp, url_prefix = "/mechanics")
    app.register_blueprint(swagger_bp, url_prefix=SWAGGER_URL)

    return app