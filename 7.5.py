prices = {
    "rice": 50,
    "wheat": 40,
    "oil": 120,
    "sugar": 30
}
quantities = {
    "rice": 2,
    "wheat": 3,
    "oil": 1,
    "sugar": 5
}
total_bill = 0
for item in prices:
    if item in quantities:
        total_bill += prices[item] * quantities[item]
print("Total Bill: ₹", total_bill)