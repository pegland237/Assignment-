sandwich_orders = ["Pastrami","sardine sandwich","Pastrami","Mayo sandwich","Pastrami","Ham burger","Sharwama"]
print("The deli has run out of Pastrami")
finished_sandwiches = []
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove('Pastrami')
for sandwich in sandwich_orders :
    print(f"I made your {sandwich}")
    finished_sandwiches.append(sandwich)
for sandwich in finished_sandwiches:
    print(f"{sandwich}, was made")