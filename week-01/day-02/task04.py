price = 45
quantity = 7
budget = 500

# total cost of 7 notebooks
total_cost = price * quantity

#max notebooks we can buy 
notebooks = budget // price

remaining_money = budget % price

print("Total cost of 7 notebooks:", total_cost, "rupees")
print("Notebooks we can buy:", notebooks)
print("Remaining money:", remaining_money, "rupees")