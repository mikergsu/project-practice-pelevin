# Работа с переменными и арифметическими операциями

rooms = 50
occupied_rooms = 38
price_per_room = 3500

occupancy_rate = occupied_rooms / rooms * 100
daily_revenue = occupied_rooms * price_per_room

print("Количество номеров:", rooms)
print("Занято номеров:", occupied_rooms)
print("Загрузка гостиницы:", round(occupancy_rate, 2), "%")
print("Дневная выручка:", daily_revenue, "руб.")
