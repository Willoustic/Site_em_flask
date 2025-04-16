from peewee import Model, CharField, IntegerField, DateTimeField
from bancos.db_login import db_clientes
import datetime

class Cliente(Model):
    nome = CharField()
    usuario = CharField(unique=True)
    email = CharField(unique=True)
    telefone = CharField(unique=True)
    senha = CharField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        # Validação da senha antes de salvar
        if len(self.senha) < 8:
            raise ValueError("A senha deve ter pelo menos 8 caracteres.")
        return super(Cliente, self).save(*args, **kwargs)
    
    class Meta:
        database = db_clientes
