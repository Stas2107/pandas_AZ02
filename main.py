import pandas as pd
import numpy as np

# Создание DataFrame с данными об учениках и их оценках по 5 предметам
data = {
    'Имя': ['Алексей', 'Борис', 'Василиса', 'Георгий', 'Дарья', 'Елена', 'Жанна', 'Иван', 'Ксения', 'Леонид'],
    'Математика': [5, 5, 4, 5, 4, 3, 4, 5, 4, 5],
    'Физика': [4, 4, 4, 4, 4, 3, 4, 5, 4, 4],
    'Химия': [3, 3, 5, 3, 3, 5, 5, 4, 5, 3],
    'Литература': [5, 5, 5, 5, 5, 2, 5, 5, 3, 5],
    'История': [5, 2, 2, 2, 2, 2, 3, 2, 2, 5]
}

df = pd.DataFrame(data)

# Вывод первых нескольких строк DataFrame
print("Первые несколько строк DataFrame:")
print(df.head())

# Вычисление средней оценки по каждому предмету
mean_grades = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_grades)

# Вычисление медианной оценки по каждому предмету
median_grades = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_grades)

# Вычисление Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print(f"\nQ1 для оценок по математике: {Q1_math}")
print(f"Q3 для оценок по математике: {Q3_math}")
print(f"IQR для оценок по математике: {IQR_math}")

# Вычисление стандартного отклонения
std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)