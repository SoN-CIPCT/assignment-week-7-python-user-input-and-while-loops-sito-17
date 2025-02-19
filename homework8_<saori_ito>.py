pizza_orders = ['Margherita', 'Neapolitan', 'Chicago-style']
finished_pizzas = []

while pizza_orders:
    current_order = pizza_orders.pop()
    print(f"Your pizza pie {current_order.title()} is finished!")
    finished_pizzas.append(current_order)
for pizza in finished_pizzas:
    print(f"The pizza {pizza.title()} was made.")