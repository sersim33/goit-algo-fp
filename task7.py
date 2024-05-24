import random
import matplotlib.pyplot as plt

def roll_dice():
    """Функція, що симулює кидок кубика."""
    return random.randint(1, 6)

def monte_carlo_simulation(num_points):
    """Метод Монте-Карло для симуляції кидків двох кубиків та підрахунку ймовірностей сум."""
    sum_count = {i: 0 for i in range(2, 13)}  # Ініціалізуємо лічильник сум
    for _ in range(num_points):
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2
        sum_count[total] += 1

    # Обчислюємо ймовірності для кожної суми
    probability = {key: (value / num_points) * 100 for key, value in sum_count.items()}
    return probability

# Кількість точок для симуляції
num_points = 100000

# Обчислення ймовірностей за допомогою методу Монте-Карло
probability = monte_carlo_simulation(num_points)

# Виведення результатів у вигляді таблиці
print("Сума на кубиках - Ймовірність випадіння (%)")
for key, value in probability.items():
    print(f"{key} - {value:.2f}%")

# Побудова графіку
plt.bar(probability.keys(), probability.values(), color='skyblue')
plt.xlabel('Сума на кубиках')
plt.ylabel('Ймовірність випадіння (%)')
plt.title('Ймовірності сум на кубиках за методом Монте-Карло')
plt.xticks(range(2, 13))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

