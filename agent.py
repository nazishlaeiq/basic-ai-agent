import webbrowser
import datetime
import requests

def greet_user():
    print("🤖 Hello Nazish! I'm your basic PC assistant. How can I help you today?")

def get_command():
    return input("👉 Your command: ").lower()

def open_website(site_name):
    webbrowser.open(f"https://www.{site_name}.com")

def show_time():
    now = datetime.datetime.now()
    print("🕒 Current Time:", now.strftime("%H:%M:%S"))

def get_weather(city="Aligarh"):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    print("🌤️", response.text)

def main():
    greet_user()
    while True:
        cmd = get_command()

        if "open" in cmd:
            site = cmd.replace("open ", "")
            open_website(site)
        elif "time" in cmd:
            show_time()
        elif "weather" in cmd:
            get_weather()
        elif "exit" in cmd or "quit" in cmd:
            print("👋 Bye Nazish!")
            break
        else:
            print("❓ I didn't understand that. Try 'open youtube', 'time', 'weather', or 'exit'.")

if __name__ == "__main__":
    main()
