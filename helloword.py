import requests

url = "https://dummyjson.com/products"
response = requests.get(url)

for product in response.json().get("products", []):
    print(f"Product: {product['title']}, Price: {product['price']}")
    