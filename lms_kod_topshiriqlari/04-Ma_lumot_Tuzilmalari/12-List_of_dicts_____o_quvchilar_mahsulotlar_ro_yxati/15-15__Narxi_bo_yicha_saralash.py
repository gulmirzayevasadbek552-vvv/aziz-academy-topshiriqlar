n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
products_sorted = sorted(products, key=lambda p: p['price'])
for product in products_sorted:
    print(product['name'], product['price'])