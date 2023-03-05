import win32com.client as win

speaker = win.Dispatch("SAPI.SpVoice")

list = ["Rahul", "Nishant", "Harry"]

for i in list:
    print("shoutout to "+i)

for name in list:
  names = name.split()
  shoutout = f"Shoutout to {names[0]}"
  speaker.Speak(shoutout)

print("Shout out of all for guys")