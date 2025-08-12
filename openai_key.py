from openai import OpenAI
import json

client = OpenAI(

)

item={
  "name": "Book1",
  "description": "This is bad",
  "price": 0,
  "tax": "This is book1"
}

json_string = json.dumps(item)
message_payload_string = {
    "role": "user",
    "content": json_string
}

response = client.chat.completions.create(
    model="gpt-4o-mini", # The deployment ID of your model
    messages=[
        {"role": "system", "content": "You are a helpful assistant to summarize the text provided in json and return the summary back in json"},
        message_payload_string
    ],
    response_format={"type": "json_object"})

print(response.choices[0].message.content)
