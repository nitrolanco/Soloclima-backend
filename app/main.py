from fastapi import FastAPI, HTTPException
from bson import ObjectId
from typing import List
from .models import Product
from .database import MongoDBService
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/products", response_model=List[Product])
async def get_products():
    db = await MongoDBService.get_database()
    products = await db.Productos.find({}, {"_id": 0}).to_list(length=None)
    return products


@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: str):

    db = await MongoDBService.get_database()
    product = await db.products.find_one({"_id": ObjectId(product_id)})
    if product:
        product["_id"] = str(product["_id"])  # Convert ObjectId to string
        return Product(**product)
    raise HTTPException(status_code=404, detail="Product not found")
