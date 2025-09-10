from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI application
app = FastAPI(
    title="FastAPI Magic Explained",
    description="A simple API to demonstrate how FastAPI automatically generates documentation from code.",
    version="1.0.0"
)

# PILLAR 2: Pydantic Model
# This defines the structure of the data for the request body.
# FastAPI uses this to generate the JSON schema for the docs.
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None  # This makes the field optional

# PILLAR 3: Decorator & PILLAR 1: Type Hints
# The decorator tells FastAPI this is a GET endpoint at the root path.
@app.get("/")
async def read_root():
    """Root endpoint that returns a simple greeting."""
    return {"Hello": "World"}

# PILLAR 3: Decorator & PILLAR 1: Type Hints
# The `item_id: int` type hint tells FastAPI to validate and document it as an integer.
# The `q: str = None` defines an optional query parameter.
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    """
    Read an item by its ID.

    - **item_id**: The unique ID of the item (path parameter)
    - **q**: An optional query string for filtering
    """
    return {"item_id": item_id, "q": q}

# PILLAR 3: Decorator & PILLAR 1: Type Hints & PILLAR 2: Pydantic Model
# This endpoint uses all three pillars together.
# - The decorator defines the PUT method and path
# - `item_id: int` is a path parameter
# - `item: Item` is a request body validated against the Pydantic model
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """
    Update an existing item.

    - **item_id**: The ID of the item to update (path parameter)
    - **item**: The new item data (request body)
    """
    return {"item_name": item.name, "item_id": item_id, "updated_price": item.price}
