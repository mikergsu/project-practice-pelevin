# Использование условий и циклов

occupied_rooms = 42
total_rooms = 50

occupancy = occupied_rooms / total_rooms * 100

if occupancy >= 80:
    print("Высокая загрузка гостиницы")
elif occupancy >= 50:
    print("Средняя загрузка гостиницы")
else:
    print("Низкая загрузка гостиницы")

print("Прогноз выручки на 7 дней:")

price = 3500

for day in range(1, 8):
    revenue = occupied_rooms * price
    print("День", day, "-", revenue, "руб.")
