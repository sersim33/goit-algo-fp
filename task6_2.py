class Item:
    def __init__(self, name, calories, cost):
        self.name = name
        self.calories = calories
        self.cost = cost
        self.ratio = calories / cost

def dynamic_programming(items: list[Item], budget: int) -> tuple[list[Item], int]:
    # Initialize DP table
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Build the table dp[][]
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if items[i - 1].cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1].cost] + items[i - 1].calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Traceback to find the items to include
    selected_items = []
    total_cost = 0
    total_calories = dp[n][budget]
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1].cost
            total_cost += items[i - 1].cost

    selected_items.reverse()  # To maintain the order of selection
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
selected_items, total_cost, total_calories = dynamic_programming(items, budget)

# Print the result
print(f"Selected items:")
for item in selected_items:
    print(f"{item.name}: Calories = {item.calories}, Cost = {item.cost}, Ratio = {item.ratio:.2f}")
print(f"Total cost: {total_cost}")
print(f"Total calories: {total_calories}")