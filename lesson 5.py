import datetime
name = input("what is your name")
current_hour = datetime.datetime.now().hour
if current_hour < 12:
    greetings = "good morning"
elif 12 <= current_hour < 18:
    greetings = "good afternoon"
else:
    greetings = "good evening"
    print(f"{greetings}, {name}")