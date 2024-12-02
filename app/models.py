from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    SKU: str
    product_name: str
    Category: str
    Brand: str
    Currency: str
    Price: str
    date_of_load: str
    reference_link: str
    Image: Optional[str] = None
