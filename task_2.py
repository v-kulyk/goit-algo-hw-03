import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def main():
    # Запитуємо користувача про рівень рекурсії
    try:
        recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    except ValueError:
        print("Будь ласка, введіть коректне число.")
        return

    # Ініціалізуємо вікно та черепаху
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Коха Сніжинка")

    t = turtle.Turtle()
    t.speed(0)  # Найвища швидкість

    # Переміщаємо черепаху у відповідне положення
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    # Викликаємо функцію для малювання сніжинки Коха
    for _ in range(3):
        koch_snowflake(t, recursion_level, 300)
        t.right(120)

    # Завершуємо програму при кліку на вікно
    screen.exitonclick()

if __name__ == "__main__":
    main()
