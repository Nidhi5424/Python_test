import uuid

orders = []

for i in range(5):
    order_id = uuid.uuid4()
    orders.append(order_id)

print("Generated Order IDs:")
for order in orders:
    print(order)
