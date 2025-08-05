print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
#scene 1 Forest Fork
scene_1 = input("You walk through a dense forest and find a mysterious cave entrance. It's dark inside. Type 'enter' to go inside or 'walk' to keep walking along the forest path \n")
if scene_1 == "enter":
    #scene 2a Inside the cave
    scene_2a = input("You light a torch and step into the cave. You see two tunnels: one to the left, echoing with strange noises, and one to the right, glowing faintly. Type 'left' or 'right' to choose a tunnel \n")
    if scene_2a == "left":
        print("You stumble into a pit of snakes. Game Over!")
    elif scene_2a == "right":
        #scene 3a Crystal chamber
        scene_3a = input("You enter a glowing chamber filled with crystals. In the center, there's a pedestal with a glowing gem and a warning sign. Type 'take' to take the gem or 'leave' to walk past it. \n")
        if scene_3a == "take":
            print(" The cave shakes and collapses. You're buried. Game Over!")
        elif scene_3a == "leave":
            #scene 4a Hidden Vault
            scene_4a = input("You find a hidden door behind the crystals leading to a vault. Inside is a chest. Type 'open' to open the chest or 'ignore' to leave it alone. \n")
            if scene_4a == "open":
                print("You found ancient treasure! You Win!")
            else:
                print("You walk away and the vault door shuts forever. Game Over!")
elif scene_1 == "walk":
    #scene 2b Forest path
    scene_2b = input("You continue walking and suddenly hear growling behind you. A wild wolf appears! Type 'run' to run away or 'climb' to climb a nearby tree. \n")
    if scene_2b == "run":
        print("You trip on a root and the wolf catches you. Game Over!")
    elif scene_2b == "climb":
        #scene 3b Tree Escape
        scene_3b = input("You safely watch the wolf lose interest and wander off. From the treetop, you spot a cabin in the distance. Type 'go' to go to the cabin or 'stay' to wait. \n")
        if scene_3b == "stay":
            print("You fall asleep and fall from the tree. Game Over!")
        elif scene_3b == "go":
            #scene 4b The cabin
            scene_4b = input("You arrive at the cabin. A kind old woman offers you soup and shows you a hidden map. Type 'accept' to take the map or 'decline' to refuse \n")
            if scene_4b == "accept":
                print("You follow the map and find the lost treasure of the forest. You Win!")
            else:
                print("You get lost on your way back. Game Over.")
