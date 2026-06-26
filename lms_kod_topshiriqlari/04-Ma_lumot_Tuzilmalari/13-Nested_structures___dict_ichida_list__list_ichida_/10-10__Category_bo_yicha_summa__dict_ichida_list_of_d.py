n = int(input().strip())
items = []
for _ in range(n):
    cat, name, price, qty = input().split()
    items.append({'cat': cat, 'name': name, 'price': int(price), 'qty': int(qty)})

totals = {}
for item in items:
    cat = item['cat']
    value = item['price'] * item['qty']
    if cat in totals:
        totals[cat] += value
    else:
        totals[cat] = value
for cat in sorted(totals):
    print(cat, totals[cat])