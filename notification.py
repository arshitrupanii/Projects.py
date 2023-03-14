from plyer import notification
import time


print('''1.Drink water  ''')

query = int(input("What you want notification "))

if query == 1:
    print("It will remind you Every 2 hours")

    def reminder():
        notification.notify(title = "Drink Water", message = "now" , timeout = 1)

    while True:  
        reminder()
        time.sleep(3600)