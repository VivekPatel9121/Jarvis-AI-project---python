from openai import OpenAI
import webbrowser
import datetime

# Add your OpenAI API key here
client = OpenAI(api_key="YOUR_API_KEY_HERE")

def ask_jarvis(prompt):
    response = client.responses.create(
        model="gpt-5.4",
        input=f"You are Jarvis, a helpful and short AI desktop assistant. User: {prompt}"
    )
    return response.output_text

def run_jarvis(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    elif "time" in command:
        return "Current time is " + datetime.datetime.now().strftime("%I:%M %p")

    elif "date" in command:
        return "Today's date is " + datetime.datetime.now().strftime("%d %B %Y")

    elif "exit" in command:
        return "exit"

    else:
        return ask_jarvis(command)

print("Jarvis AI Assistant Started")
print("Type 'exit' to stop")

while True:
    user_input = input("You: ")
    result = run_jarvis(user_input)

    if result == "exit":
        print("Jarvis: Goodbye!")
        break

    print("Jarvis:", result)