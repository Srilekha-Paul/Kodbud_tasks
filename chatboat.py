# Simple CLI Chatbot
print("🤖 Hello! I’m ChatBot. Type 'bye' or 'exit' to end the chat.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        print("ChatBot: Hello there! How can I help you today?")
    
    elif "how are you" in user_input:
        print("ChatBot: I'm doing great! Thanks for asking. How about you?")
    
    elif "your name" in user_input:
        print("ChatBot: I'm ChatBot — your friendly Python assistant 🤖")
    
    elif "weather" in user_input:
        print("ChatBot: I can’t check weather yet, but you can use your Weather App for that 🌤️")
    
    elif "time" in user_input:
        from datetime import datetime
        print("ChatBot:", datetime.now().strftime("Current time is %I:%M %p"))
    
    elif "date" in user_input:
        from datetime import date
        print("ChatBot:", date.today().strftime("Today's date is %B %d, %Y"))
    
    elif "bye" in user_input or "exit" in user_input:
        print("ChatBot: Goodbye! Have a nice day 😊")
        break
    
    else:
        print("ChatBot: Sorry, I didn’t understand that. Could you rephrase?")
