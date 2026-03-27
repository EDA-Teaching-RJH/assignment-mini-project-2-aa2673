import re
import time
from AterraClasses import Barbarian, Rogue, Tank  
import csv

def main():
    loading_screen()
    adventurer = character_creation()
    save(adventurer)

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
        self.classAbility = "Hero's Luck" 
    
    def __str__(self):
        return(f"---Adventurer Profile---\nName: {self.name}\nClass: {type(self).__name__}\nOffense: {self.off}\nVitality: {self.vit}\nAgility: {self.agl}\nClass Ability: {self.classAbility}\n")


def character_creation():
    while True:
        name = input("\nWelcome to Aterra Online! Please enter a first and last name for your adventurer: ").strip().title()
        if re.search(r"^[a-zA-Z]+\s+[a-zA-Z]+$", name):
            print(f"Nice to meet you {name}!")
            break
        else:
            print("\nFirst and last names must only contain letters a-z and should have a space between them.")
    
    while True:
            print("How would you like to allocate your stat points? You have 20 to spend.")
            try:
                offense = int(input("Offense: "))
                vitality = int(input("Vitality: "))
                agility = int(input("Agility: "))
                try:
                    assert offense + vitality + agility == 20
                    if offense == 15 and vitality == 5:
                        adventurer = Barbarian(name,offense,vitality,agility)
                    elif vitality == 15 and offense == 5:
                        adventurer = Tank(name,offense,vitality,agility)
                    elif agility == 15 and offense == 5:
                        adventurer = Rogue(name,offense,vitality,agility)
                    else:
                        adventurer = Adventurer(name,offense,vitality,agility)
                    print(f"{adventurer}")
                    return adventurer
                except AssertionError:
                    print("You must allocate exactly 20 points.")
            except ValueError:
                 print("Please input numbers only")
           
def save(adventurer):
    with open("Assignment2.csv", "a", newline = "") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Class", "Offense", "Vitality", "Agility"])
        writer.writerow({"Name": adventurer.name, "Class": type(adventurer).__name__, "Offense": adventurer.off, "Vitality": adventurer.vit, "Agility": adventurer.agl})
    print("Character Saved.")




if __name__ == "__main__":
    main()