
from chatbot import get_response

def run_chat():
    print("TravelBot 🌍 (type 'exit' to quit)\n")
    history = []

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("TravelBot: Goodbye! Safe travels! 🌏")
            break

        response, history = get_response(user_input, history)
        print(f"TravelBot: {response}\n")

if __name__ == "__main__":
    run_chat()
