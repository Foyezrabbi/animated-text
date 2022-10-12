
import os
import time


def animate_text(text):
    number_of_characters = 1
    while True:
        print("\n")
        print(text[0:number_of_characters])
        number_of_characters += 1
        if number_of_characters > len(text):
            number_of_characters = 0
        time.sleep(0.2)
        os.system('clear')

    # Main Program Starts Here....


animate_text("Hello World!")

