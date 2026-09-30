from pydantic import BaseModel


class OrderCreate(BaseModel):
    customer_name: str
    product: str
    quantity: int
    amount: float


class OrderResponse(BaseModel):
    id: int
    customer_name: str
    product: str
    quantity: int
    amount: float
    status: str

    class Config:
        from_attributes = True