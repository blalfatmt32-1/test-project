products = [
    [12, "Americano"],
    [15, "Cappuccino"],
    [18, "Latte"],
    [20, "Spanish Latte"],
    [22, "Turkish Coffee"]
]

print("Coffee Menu:")
for i in range(len(products)):
    print(i+1, products[i][1])

x = input("Enter the number: ")

if x.isdigit():
    x = int(x)
    if x >= 1 and x <= len(products):
        price = products[x-1][0]
        total = price + price * 0.15
        print("Selected:", products[x-1][1])
        print("Price with tax:", total)
    else:
        print("Number not found")
else:
    print("Please enter a number only")