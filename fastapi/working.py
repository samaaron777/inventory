from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None
    
class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float]
    brand: Optional[str] = None

inventory = {}

@app.get("/get-item/{item_id}")
def get_item_by_id(item_id: int = Path(..., description="The ID of the item you like to view", gt=0)):
    item = inventory.get(item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

@app.get("/get-item-by-name/")
def get_item_by_name(name: Optional[str] = None, test: Optional[int] = None):
    for _, item_info in inventory.items():
        if name and item_info["name"].lower() == name.lower():
            return item_info
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="ItemID already exists.")
    
    inventory[item_id] = item.dict()
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID does not exist.")
    
    inventory[item_id].update(item.dict(exclude_unset=True))
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of the item to delete")):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID does not exist.")
    del inventory[item_id]
    return {"Success": "Item deleted!"}
