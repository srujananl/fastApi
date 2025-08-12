from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import json


# Initialize the FastAPI app
app = FastAPI()
# Define a Pydantic model for the data expected in the POST request body
# class Item(BaseModel):
#     name: Optional[str] = None
#     description: Optional[str] = None
#     price: Optional[float] = None
#     tax: Optional[str] = None

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

class ItemList(BaseModel):
    items: list[Item]
    



# Define a POST endpoint
@app.post("/notes/")
async def get_summary(item: ItemList):
    """
    Creates a new item based on the provided Item data.
    """
    # In a real application, you would save this item to a database
    # or perform other business logic here.
    #print(f"Received item: {item}")
    client = OpenAI(
    
)

    response = client.chat.completions.create(
    model="gpt-4o-mini", # The deployment ID of your model
    messages=[
        {"role": "system", "content": "You are a assistant to summarize the text provided in json of electronics and retun a combined summary back in json"},
        {"role": "user", "content": json.dumps(item.dict())}
    ],
    response_format={"type": "json_object"}
    
)

    print(response.choices[0].message.content)
    return (response.choices[0].message.content)

# To run this application:
# 1. Save the code as main.py
# 2. Open your terminal in the same directory and install FastAPI and Uvicorn:
#    pip install "fastapi[standard]" uvicorn
# 3. Run the application:
#    uvicorn main:app --reload
#
# You can then test this API using a tool like cURL or a client like Postman,
# sending a POST request to http://127.0.0.1:8000/items/ with a JSON body
# conforming to the Item model (e.g., {"name": "Book", "price": 12.99}).