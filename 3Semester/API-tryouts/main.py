from enum import Enum
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

app = FastAPI()

class Category (Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"
    
class Item(BaseModel):
    name: str
    price: float
    category: Category
    id: int 
    count: int

items = {
    0: Item(name="Screwdriver", price=10.0, category=Category.TOOLS, id=0, count=10),
    1: Item(name="Wrench", price=20.0, category=Category.TOOLS, id=1, count=5),
    2: Item(name="Nails", price=5.0, category=Category.CONSUMABLES, id=2, count=100),
}

@app.get ("/")
def index () -> dict [str, dict [int, Item]]:
    return {"items": items}

@app.get ("/items/{item_id}")
def query_item_by_id (item_id: int) -> Item:
    if item_id not in items:
        raise (HTTPException (status_code=404, detail=f"Item with the id {item_id} not found"))
    
    return items[item_id]



Selection = dict [str, str | float | Category | int | None]

@app.get ("/items/")
def query_item_by_paramenters(name: str | None = None,
                              price: float | None = None, 
                              category: Category | None = None
) -> dict [str, Selection]:
    def check_item (item: Item) -> bool:
        return all (
            (
                name is None or item.name == name,
                price is None or item.price == price,
                category is None or item.category == category
            )
        )
    selection = [item for item in items.values() if check_item(item)]
    return {
        "query": {"name": name, "price": price, "category": category},
        "selection": selection
    }