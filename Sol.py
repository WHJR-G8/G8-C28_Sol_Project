dict1 = {"Bread":20, "Cheese":30, "Tomato":20, "Onion":20, "Pickle":10}

sum = 0

for cost in dict1.values():
    sum += cost
    
print("The total cost for preparing a Sandwich is : Rs.",sum)
