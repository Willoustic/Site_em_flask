from peewee import Model, CharField, IntegerField, DateTimeField
from bancos.db_login import db_clientes
import datetime

class Cliente(Model):
    nome = CharField()
    email = CharField(unique=True)
    telefone = CharField(unique=True)
    senha = CharField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db_clientes
