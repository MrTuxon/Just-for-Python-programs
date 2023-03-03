# Программа для вывода таблицы соотношения температур, выраженных в градусах Цельсия и Фаренгейта

print("Celsius\Fahrenheit")

# Цикл для всех температур от 0 до 100 градусов Цельсия, кратных 10
for celsius in range(0, 101, 10):
  fahrenheit = celsius * (9/5) + 32
  print(celsius, "\t", round(fahrenheit,2))