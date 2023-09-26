"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""


# This program is timer that counts down


import time # The time library has a sleep function that will pause the script for a specifized amount of time
import snaps # the snaps library makes it easy to display images and make sounds

# ask user to enter desired countdown time
set_time = int(input("Please set your timer in seconds: "))

time.sleep(set_time)

snaps.display_message("Time's up!!")

