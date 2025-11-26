from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Backend.database.banco import db


def crear_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'chave-super-secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@Welterson123@localhost:3306/sistema-advogado-cliente'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db = SQLAlchemy(app)


    from Backend.routes.routes import rota1_bp
    from Backend.routes.contatos import rota2_bp

    app.register_blueprint(rota1_bp)
    app.register_blueprint(rota2_bp)

    return app