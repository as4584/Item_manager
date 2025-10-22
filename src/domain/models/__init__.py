from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Product:
	sku: str
	name: str
	qty_on_hand: int = 0
	qty_sold: int = 0
	category: Optional[str] = None
	retail_price: Optional[float] = None


@dataclass
class Sale:
	sku: str
	quantity: int
	date: datetime
	unit_price: Optional[float] = None
	sale_hash: Optional[str] = None
