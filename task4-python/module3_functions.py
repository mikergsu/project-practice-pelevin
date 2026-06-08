# Пользовательские функции

def calculate_revenue(occupied_rooms, price):
    return occupied_rooms * price

def calculate_month_revenue(daily_revenue, days):
    return daily_revenue * days

occupied_rooms = 40
price = 3500

daily = calculate_revenue(occupied_rooms, price)
monthly = calculate_month_revenue(daily, 30)

print("Дневная выручка:", daily, "руб.")
print("Месячная выручка:", monthly, "руб.")
