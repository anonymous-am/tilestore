import requests
import json
import base64

URL = "http://127.0.0.1:8000/api/addProduct/"

# Open the image file and encode it in base64
image_path = "C:/Users/Abhishek Srivastav/Downloads/test.jpg"
with open(image_path, "rb") as image_file:
    base64_encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Create data in dictionary form
data = {
    "product_name": "Kitchen Tile",
    "size": "24 x 34",
    "product_id": "KITCH-111",
    "category": "Kitchen",
    "product_details": "asdfgg",
}

# Add the base64-encoded image to the dictionary
data["product_image"] = {
    "file": base64_encoded_image,
    "fileName": "test.jpg"
}

# Convert the dictionary into JSON
json_data = json.dumps(data)

# Send the request with the updated JSON data
headers = {'Content-Type': 'application/json'}
resp = requests.post(url=URL, data=json_data, headers=headers)

# Check the content of the response
try:
    py_resp = resp.json()
    print("Response:", py_resp)
except requests.exceptions.JSONDecodeError as e:
    print("--------------------------------------------------------------")
    print(f"JSON decoding error: {e}")
    # Handle the error case, maybe by setting py_resp to a default value or logging the issue.
