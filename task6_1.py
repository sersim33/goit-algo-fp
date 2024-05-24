class Item:
    def __init__(self, name, calories, cost):
        self.name = name
        self.calories = calories
        self.cost = cost
        self.ratio = calories / cost

# Greedy algorithm to maximize the ratio of calories to cost without exceeding the budget
def greedy_algorithm(items: list[Item], budget: int) -> tuple[list[str], int]:
    # Sort items based on the ratio of calories to cost in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_cost = 0
    selected_items = []
    total_calories = 0

    for item in items:
        if total_cost + item.cost <= budget:
            total_cost += item.cost
            total_calories += item.calories
            selected_items.append(item)

    return selected_items, total_cost, total_calories

# Food data
item_data = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Create a list of Item objects
items = [Item(name, data["calories"], data["cost"]) for name, data in item_data.items()]

# Budget limit
budget = 70

# Call the function and get the result
selected_items, total_cost, total_calories = greedy_algorithm(items, budget)

# Print the result
print(f"Selected items:")
for item in selected_items:
    print(f"{item.name}: Calories = {item.calories}, Cost = {item.cost}, Ratio = {item.ratio:.2f}")
print(f"Total cost: {total_cost}")
print(f"Total calories: {total_calories}")