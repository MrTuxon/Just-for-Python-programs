
# Инициализируйте переменную для хранения суммы чисел
total = 0

# Инициализируйте переменную для хранения количества чисел
count = 0

# Прочтитать первое число
num = int(input("Enter a number (0 to end): "))

# Проверьте, равно ли первое число нулю
if num == 0:
    print("Error: You cannot enter 0 as the first number!")

# Если число не равно нулю, продолжайте цикл
while num != 0:
    # Добавьте это число к общему количеству
    total += num
    # Увеличьте количество
    count += 1
    # Прочтите следующий номер
    num = int(input("Enter a number (0 to end): "))

# Рассчитайте среднее значение
avg = total / count

# Выведите среднее значение
print("The average is:", avg)