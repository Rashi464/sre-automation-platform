from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from .database import Base, engine, get_db
from .models import Order
from .schemas import OrderCreate, OrderResponse


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Real-Time E-Commerce Order Processing Service",
    description="Cloud-native order processing platform with SRE and DevOps automation",
    version="1.0.0",
)
Instrumentator().instrument(app).expose(app)

@app.get("/")
def root():
    return {
        "service": "Order Processing Service",
        "status": "running",
        "version": "1.0.0"
    }


@app.get("/health")
def health(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "service": "order-service",
            "database": "healthy"
        }

    except Exception:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "unhealthy",
                "service": "order-service",
                "database": "unhealthy"
            }
        )


@app.post("/orders", response_model=OrderResponse)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db)
):
    new_order = Order(
        customer_name=order.customer_name,
        product=order.product,
        quantity=order.quantity,
        amount=order.amount,
        status="PLACED"
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order


@app.get("/orders", response_model=list[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()


@app.get("/orders/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order