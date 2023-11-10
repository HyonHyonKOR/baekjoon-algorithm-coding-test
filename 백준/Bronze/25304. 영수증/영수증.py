total_price = int(input())
total_items = int(input())
result_price = 0

for _ in range(total_items):
    item_price, item_quantity = map(int, input().split())
    result_price += (item_price * item_quantity)

if result_price == total_price:print("Yes")
else: print("No")