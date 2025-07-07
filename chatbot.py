

from openai_chat import ask_gpt
from planner import suggest_itinerary
from travel_data import show_budget_chart, show_weather_forecast, show_expense_comparison

conversation_history = []

def get_response(user_input, history=None):
    return ask_gpt(user_input, history)

    
    if message.lower() == "show budget graph":
        budget = {1: 3000, 2: 5800, 3: 7500, 4: 10000, 5: 12800}
        show_budget_chart(budget)
        return "Displayed your estimated travel budget graph."
    
    elif message.lower() == "show weather forecast":
        forecast = {"Mon": 30, "Tue": 31, "Wed": 32, "Thu": 29, "Fri": 30}
        show_weather_forecast(forecast)
        return "Displayed the 5-day weather forecast line graph."


    elif message.lower() == "show expense chart":
        expenses = {
            "Day 1": (2000, 800, 300),
            "Day 2": (2200, 850, 400),
            "Day 3": (1800, 900, 450),
            "Day 4": (2500, 1000, 500)
        }
        show_expense_comparison(expenses)
        return "Displayed daily expense comparison with bar and line chart."

    
    elif message.lower().startswith("itinerary"):
        try:
            days = int(message.split(" ")[1])
            plan = suggest_itinerary(days)
            return "Here’s your plan:\n" + "\n".join(f"- {item}" for item in plan)
        except:
            return "Please enter like: itinerary 3"
        
    reply, conversation_history = ask_gpt(message, conversation_history)
    return reply
