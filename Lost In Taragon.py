from time import sleep
import webbrowser
import os

delay = 5 # delay time between statements in seconds

print("Welcome User")

sleep(25)

print("What is the name for your male character? ")

name = input()

sleep(delay)

print(("Welcome ") + name)

sleep(10)

print("""
The midday matket in Taragon bustles with life; sellers marketing their wears, 
customers gawking at the commodities, the sly boy who just slipped an apple in his worn out tunic.
You glance up at your father, wonder glistening in your eyes
""")

sleep(delay)

print("""
What do you ask?
1. "Father, why have we never been here before?" 
2. Smile widely
""")

sleep(delay)

choice = int(input("Enter a number: "))

if choice == 1:
    webbrowser.open("https://www.youtube.com/watch?v=8oE5Z2GLhNc")
    sleep(delay)
    os.system("taskkill /im chrome.exe /f")
if choice == 2:
    print("""
    You glance up at your father smiling widely and focus your eyes back on the road
    """)

