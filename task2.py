import turtle

def draw_pyt_tree(t, trunk_len, level):
    if level == 0:
        return
    else:
        t.forward(trunk_len)
        t.left(45)
        draw_pyt_tree(t, trunk_len * 0.7, level-1)
        t.right(90)
        draw_pyt_tree(t, trunk_len * 0.7, level-1)
        t.left(45)
        t.backward(trunk_len)

def main():
    while True:
        user_input = input("Введіть рівень рекурсії для створення фрактала 'дерево Піфагора' (ціле число): ")
        try:
            level = int(user_input)
            break
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    # Налаштування 
    pyt_turtle = turtle.Turtle()
    pyt_turtle.color("green")
    pyt_turtle.width(2)
    pyt_turtle.left(90)
    pyt_turtle.speed(0)  # Найвища швидкість

    # Початкові координати та довжина стовбура
    pyt_turtle.penup()
    pyt_turtle.goto(0, -200)
    pyt_turtle.pendown()

    # Виклик функції для малювання дерева Піфагора з введеним рівнем рекурсії
    draw_pyt_tree(pyt_turtle, 150, level)

    # Закрити вікно при кліку
    turtle.done()

if __name__ == "__main__":
    main()


