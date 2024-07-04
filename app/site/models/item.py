from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


class RequestProducts(BaseModel):
    empresa_id: str


class Product(BaseModel):
    description: str
    image: str


class ResponseProducts(BaseModel):
    products: list[Product]



