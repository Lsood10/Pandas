
import matplotlib.pyplot as plt

# 1. Budget Line Chart
def show_budget_chart(data):
    days = list(data.keys())
    cost = list(data.values())

    plt.figure(figsize=(8, 4))
    plt.plot(days, cost, marker='o', linestyle='-', color='teal')
    plt.title("📊 Estimated Travel Budget Over Days")
    plt.xlabel("Days")
    plt.ylabel("Budget (INR)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 2. Weather Forecast Line Graph
def show_weather_forecast(temp_data):
    days = list(temp_data.keys())
    temps = list(temp_data.values())

    plt.figure(figsize=(8, 4))
    plt.plot(days, temps, color='orange', linestyle='--', marker='s')
    plt.title("🌤 5-Day Temperature Forecast")
    plt.xlabel("Day")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 3. Daily Expenses: Line + Bar Chart
def show_expense_comparison(data):
    days = list(data.keys())
    hotels = [v[0] for v in data.values()]
    food = [v[1] for v in data.values()]
    shopping = [v[2] for v in data.values()]

    plt.figure(figsize=(10, 5))

    # Bar chart
    plt.bar(days, hotels, color='skyblue', label='Hotel')
    plt.bar(days, food, bottom=hotels, color='lightgreen', label='Food')
    plt.bar(days, shopping, bottom=[h+f for h, f in zip(hotels, food)], color='salmon', label='Shopping')

    # Line chart overlaid
    total = [h+f+s for h, f, s in zip(hotels, food, shopping)]
    plt.plot(days, total, color='black', marker='o', linewidth=2, label='Total Spent')

    plt.title("🧾 Daily Travel Expense Breakdown")
    plt.xlabel("Day")
    plt.ylabel("Cost (INR)")
    plt.legend()
    plt.tight_layout()
    plt.show()
