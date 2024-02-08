"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""


# This program is the Nerve of Steel Game. The last person to sit down before the timer runs out wins

import random
import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images 

im = Image.open("times-up.jpeg")

while True:
    ready_prompt = input("Are you ready to play Nerve of Steel? Y or N?")

    if ready_prompt.upper() == "Y":
        print("All players stand! Be the last person to sit down before the timer ends.")
    
        # random time between 5 to 25 seconds
        set_time = random.randint(5,25)

        time.sleep(set_time)
        im.show()
        print("Times Up! Players still standing are eliminated. The last person to sit down wins!")

    else: 
        print("Prepare for Nerve of Steel.")
    
    play_again_prompt = input("Do you want to play Nerve of Steel again? Y or N")
    if play_again_prompt.upper() != "Y":
        break


    
