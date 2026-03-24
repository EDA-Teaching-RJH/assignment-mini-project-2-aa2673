import re
import time

def main():
    loading_screen()
    character_name()

def loading_screen():
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    print("Preps is shaping mountains...")
    time.sleep(1)
    print("Jonathan is fumbling...")
    time.sleep(1)
    print("Chia is sharing wisdom...")
    time.sleep(1)
    print("Ethan is gathering fighters...")
    time.sleep(1)
    print("ATERRA ONLINE")
    time.sleep(1)
    input("Press Enter to continue ")
    return



def character_name():
    name = input("\nWelcome to Aterra Online! Please enter a name for your adventurer: ").strip().title()
    return name
    



main()