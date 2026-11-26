prices = [100,250,300,150,500,700,200,450,600,350]

total = sum(prices)
avrage = total / len(prices)

above_avrage = [p for p in prices if p > avrage]

print("Product Prices:", prices)
print("Average Price:", avrage)
print("Prices Above Average:", above_avrage)