import time 
import random
wild_animal =["Bear", "tiger", "dinosaur", "Fox"]
creature = random.choice(wild_animal)



def print_pause(slow):
    print(slow)
    time.sleep(1)
    
def print_pause1(slow1):
    print(slow1)
    time.sleep(1)

def play_adventure():
    intro()

def intro():
    print_pause("Welcome to Adventure of **Death_island**")
    print_pause("You find yourself in an unconsious state on a huge island, " 
    "\nSlowly you come out of unconsciousness..")
    print_pause1("You find your boat but your boat is swept away by the waves, "
    "it has gone off shore.")
    print_pause("There is a huge island in front of you and the giant sea around it.")
    condition()
    
def condition():
    print_pause("Enter 1 to [(go inside the island)].")
    print_pause("Enter 2 to [(repair your boat)].")
    print_pause("what would you like to do?") 
    
    choice()
    
def island():
     print_pause("Your approach to go inside, now you are in middle of island.")
     print_pause1("Now, you make a dagger to protect yourself from wild animals.")
     print_pause("you move to forward..")
     print_pause1("ohh! You see a polar in front of you, They would have seen you")
     print_pause1("You feel unprepared for this,  what with only having a small dagger.")
    
     while True:
        action = input("Would you like to (1) fight or (2) run away?\nplz(enter 1 or 2)\n").lower()
        global wild_animal
        if "1" in action:
              print_pause("You do your best...")
              print_pause(f"but your dagger is no match for the {creature}")
              print_pause("You have been DEFEATED!")
              print_pause('"GAME OVER"')
              lets_play_again()
              break    
        elif "2" in action:
            print_pause("You run out of island.")
            print_pause("Luckily, you don't seem to have been followed.")
            condition()
            break
        else:
            plz_type_correct()
            
def boat():
    print_pause("Your deside to repair your boat.")
    print_pause1("you collect some woodens with strong natural ropes to bind your boat.")
    print_pause1("finally you crosses the sea and reched to an edge of a village.")
    print_pause("you save you life \nhurray! You **Won** this Adventure")
    
    lets_play_again()
    
def choice():
    response = input("(Plz enter 1 or 2.)\n").lower()
    while True:
         if "1" == response:
             island()
             break
         
         elif "2" == response:
             boat()
             break
         
         else:
             choice()
             
            
             
def lets_play_again():
    reply = input("Would you like to play again? (y/n)\n").lower()
    while True:
         if "n" in reply:
            print_pause("Thanks for playing!")
            print_pause("See you next time.")
            exit()
            break
         elif "y" in reply:
            global creature
            creature = random.choice(wild_animal)
            play_adventure()
         else:
             plz_type_correct()
             lets_play_again()
            
             
         
def plz_type_correct():
    print_pause("You have typed a wrong input.")
    print_pause("Please type again")
    
         
play_adventure()