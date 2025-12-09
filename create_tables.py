from config.database import engine
from models.base import Base

# IMPORTA TODOS OS MODELOS PARA O SQLALCHEMY CONHECER AS TABELAS
from models.pedido import Pedido
from models.item_pedido import ItemPedido
from models.cliente import Cliente

print("Criando tabelas no banco de dados...")

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")

