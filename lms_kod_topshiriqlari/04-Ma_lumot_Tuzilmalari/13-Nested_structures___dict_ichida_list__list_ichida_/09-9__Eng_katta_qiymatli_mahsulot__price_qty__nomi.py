n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})

m_v = -1
m_n = ""
for item in items:
    value = item['price']   * item['qty']
    if value > m_v:
        m_v = value
        m_n = item['name']
print(m_n)