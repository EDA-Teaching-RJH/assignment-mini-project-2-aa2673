import re
import time

def main():
    loading_screen()
    character_creation()

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


class Adventurer:
    def __init__(self,name,off,vit,agl):
        self.name = name
        self.off = off
        self.vit = vit
        self.agl = agl


def character_creation():
    while True:
        name = input("\nWelcome to Aterra Online! Please enter a first and last name for your adventurer: ").strip().title()
        if re.search(r"^[a-zA-Z]+\s+[a-zA-Z]", name):
            print(f"Nice to meet you {name}!")
            print("How would you like to allocate your stat points? You have 20 to spend.")
            offense = int(input("Offense: "))
            vitality = int(input("Vitality: "))
            agility = int(input("Agility: "))
            adventurer = Adventurer(name, offense, vitality, agility)
            print(f"\n---Adventurer Profile---\nName:{name}\nOffense:{offense}\nVitality:{vitality}\nAgility:{agility}")
            return adventurer
            break
        else:
            print("\nFirst and last names must only contain letters a-z and should have a space between them.")
        

        


    

        


#
# class Classes:
    
    




    


main()