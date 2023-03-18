# import tkinter
import tkinter as tk
import random
import datetime
import webbrowser
from PIL import Image, ImageTk


# Bible verses to choose from
verses = [
    "For God so loved the world that He gave His one and only Son, that whoever believes in Him shall not perish but have eternal life. - John 3:16",
    "Trust in the Lord with all your heart and lean not on your own understanding; in all your ways submit to Him, and He will make your paths straight. - Proverbs 3:5-6",
    "But He was pierced for our transgressions, He was crushed for our iniquities; the punishment that brought us peace was on Him, and by His wounds we are healed. - Isaiah 53:5",
    "The Lord is my shepherd, I shall not want. - Psalm 23:1",
    "I can do all this through Him who gives me strength. - Philippians 4:13",
    "Jesus wept. - John 11:35",
    "For God has not given us a spirit of fear, but of love and of power and of a sound mind - 2 Timothy1:7",
    "The LORD is close to the brokenhearted; he rescues those whose spirits are crushed. - Psalm 34.18",
    "He will wipe every tear from their eyes, and there will be no more death or sorrow or crying or pain. All these things are gone forever. - Revelation 21:4",
    "Long ago the Lord said to Israel: “I have loved you, my people, with an everlasting love. With unfailing love I have drawn you to myself. - Jeremiah 31:3",
    "Thank you for making me so wonderfully complex! Your workmanship is marvelous—how well I know it. - Psalm 139:14",
    "He will cover you with his feathers. He will shelter you with his wings. His faithful promises are your armor and protection. - Psalm 91:4",
    "So whether you eat or drink, or whatever you do, do it all for the glory of God. - 1 Corithians 10:31",
    "Though a thousand fall at your side, though ten thousand are dying around you, these evils will not touch you. - Psalm 91:7",
    "Even though you walk through the valley of the shadow of death, you shall not fear for He is with you. - Psalm 23:4",
    "Don’t be afraid, for I am with you. Don’t be discouraged, for I am your God. I will strengthen you and help you. I will hold you up with my victorious right hand. - Isaiah 41:10",
    "For I am not ashamed of this Good News about Christ. It is the power of God at work, saving everyone who believes—the Jew first and also the Gentile. - Romans 1:16",
    "Fools vent their anger, but the wise quietly hold it back. - Proverbs 29:11",
    "Work hard and become a leader; be lazy and become a slave. - Proverbs 12:24",
    "But as for you, be strong and courageous, for your work will be rewarded. - 2 Chronicles 15:7",
    "The Lord protects all those who love him, but he destroys the wicked. - Psalms 145:20",
    "If you think you are too important to help someone, you are only fooling yourself. You are not that important. - Galatians 6:3",

]

# Choose a random verse for the day
today = datetime.datetime.today().strftime("%Y-%m-%d")
random.seed(today)
todays_verse = random.choice(verses)
# little easter egg
favorite_verse = "For God has not given us a spirit of fear, but of love and of power and of a sound mind - 2 Timothy1:7"


# Function to update the date and time label
def update_date_time():
    now = datetime.datetime.now()
    date_time_label.config(text=now.strftime("%B %d, %Y %I:%M %p"))
    window.after(1000, update_date_time)  # Call this function again in 1 second
    date_time_label.config(text = "Today is " + datetime.datetime.today().strftime("%B %d, %Y") + " and it is currently " + datetime.datetime.now().strftime("%I:%M %p"))

# function to display user name when they enter it
def display_greeting():
    name = user_entry.get()
    greeting.config(text = "Hello " + name + "!" )
    # so it will remove the "what is your name?" line when submit button is clicked
    user_name_call.grid_forget()
    user_entry.grid_forget()
    submit_button.grid_forget()
    # show the Bible verse and link
    Bible_phrase.grid()
    verse_label.grid()
    Bible_button.grid()


window = tk.Tk()
# title of widget
window.title("Bible Verse Widget")

# set the window background color and make it non-resizable
window.configure(bg = "#242526")
window.resizable(False, False)

# make the window stay on top of other windows
window.attributes('-topmost', True)
# make the window at the top center of the screen
window.geometry("+0+0")

# Display the date and time
date_time_label = tk.Label(
    text = "Date/time",
    font = ("Comic-sans", 10),
    bg = "#242526",
    fg = "white",
    width = 136,
    height = 3,
)
date_time_label.grid(row = 1, column = 0, columnspan = 2)

# Call the update_date_time function to start updating the label
update_date_time()

greeting = tk.Label(
    text = "Hello User",
    font = ("Arial", 9, "bold"),
    fg = "white",
    bg = "#242526",
    width = 155,
    height = 10)
# print greeting to screen
greeting.grid(row = 0, column = 0, columnspan = 2)

image = Image.open("Bible verse widget.png")
# Create a PhotoImage object of the image
photo = ImageTk.PhotoImage(image)
# Create a label with the PhotoImage object as its image
label = tk.Label(window, 
    image = photo, 
    bg = "#242526", 
    )
# Add the label to the window
label.grid(row = 0, column = 1, columnspan = 1)


user_name_call = tk.Label(
    text = "What is your name?",
    fg = "white",
    bg = "#242526",
    width = 55)
user_name_call.grid(row = 2, column = 0)

user_entry = tk.Entry(fg = "white", bg = "#242526", width = 50)
user_entry.grid(row = 2, column = 1)

submit_button = tk.Button(
    text = "Submit",
    width = 15,
    height = 1,
    bg = "#242526",
    fg = "#B399D4",
    command = display_greeting,
    # changes appearance of button
    relief=tk.GROOVE
)
submit_button.grid(row = 2, column = 2)


Bible_phrase = tk.Label(
    text = "The Bible verse for the day:",
    width = 155,
    height = 3,
    bg = "#242526",
    fg = "white"
)
Bible_phrase.grid(row = 3, column = 0, columnspan = 2)
Bible_phrase.grid_remove()

# Create a label to display the verse
verse_label = tk.Label(
    text = todays_verse,
    font = ("Times new roman", 12, "italic"),
    bg = "#242526",
    fg = "white",
    width = 130,
    heigh = 5
)
verse_label.grid(row = 4, column = 0, columnspan = 2)
verse_label.grid_remove()

# Check if the current verse is the favorite verse
if todays_verse == favorite_verse:
    verse_label.config(text="The verse is " + favorite_verse + "!!!")

def on_button_click():
    # Close the window
    window.destroy()

# Function to open a Bible website
def open_Bible():
    webbrowser.open("https://www.bible.com/bible/116/GEN.1.NLT")

# Function to open Bible website and close the window
def open_Bible_and_close_window():
    open_Bible()
    on_button_click()

# button that will link to Bible on website if user wants
Bible_button = tk.Button(
    text = "Read the Bible",
    width = 155,
    height = 3,
    bg = "#242526",
    fg = "#B399D4",
    command = open_Bible_and_close_window,
    # changes appearance of button
    relief = tk.GROOVE
)
Bible_button.grid(row = 5, column = 0, columnspan = 2)
Bible_button.grid_remove()

# customize size of screen
# window.geometry("500x300")

# open / show the window
window.mainloop()
