from rotas.clientes import clientes
from bancos.db_login import db_clientes
from bancos.models.clientes import Cliente


def configure_all(app):
    app.register_blueprint(clientes, url_prefix="/")
    config_db()
    
def config_db():
    db_clientes.connect()
    db_clientes.create_tables([Cliente])