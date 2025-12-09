from pydantic import BaseModel
from datetime import date
from typing import List, Optional


class ItemPedidoSchema(BaseModel):
    produto: str
    quantidade: int
    preco: float


class PedidoCreateSchema(BaseModel):
    cliente: str
    itens: List[ItemPedidoSchema]


class PedidoUpdateSchema(BaseModel):
    cliente: Optional[str] = None
    data_pedido: Optional[date] = None


class ItemPedidoOutSchema(ItemPedidoSchema):
    id: int
    pedido_id: int

    class Config:
        from_attributes = True


class PedidoOutSchema(BaseModel):
    id: int
    cliente: str
    data_pedido: date
    itens: List[ItemPedidoOutSchema]

    class Config:
        from_attributes = True


class ClienteOutSchema(BaseModel):
    id: int
    nome: str
    idade: int

    class Config:
        from_attributes = True


class ClienteCreateSchema(BaseModel):
    nome: str
    idade: int


class ClienteUpdateSchema(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
