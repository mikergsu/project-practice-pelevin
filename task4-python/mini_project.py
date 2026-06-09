# Мини-проект расчета дохода гостиницы

rooms = 50
occupied_rooms = int(input("Введите количество занятых номеров: "))
price = 3500

daily_revenue = occupied_rooms * price
monthly_revenue = daily_revenue * 30

occupancy = occupied_rooms / rooms * 100

print()
print("Загрузка гостиницы:", round(occupancy, 2), "%")
print("Дневная выручка:", daily_revenue, "руб.")
print("Месячная выручка:", monthly_revenue, "руб.")

if occupancy >= 80:
    print("Высокий уровень загрузки")
elif occupancy >= 50:
    print("Средний уровень загрузки")
else:
    print("Низкий уровень загрузки")
