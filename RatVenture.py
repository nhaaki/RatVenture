#Ratventure, an Action RPG python game. The player plays as a Hero, who seeks to kill the Rat King as the main objective. 
# Nur Hakimi B Mohd Yasman
# P12 PRG1 Class of IT12
# Project started on 27 July, submitted on 17 August.

# This program works perfectly fine when ran in Visual Studio 2019, but when using IDLE, it sometimes does not respond(?). As an example, typing '1' at the game menu
# will not return or display any feedback as it was supposed to. I don't experience this issue using VS though.

from random import randint
from sys import exit


# |================|
# |GLOBAL VARIABLES|
# |================|


# (All of the data relating to the player saved into the file.)
playerStats = {"Name": "The Hero", "MinDamage": 2, "MaxDamage": 4,\
               "Defence": 1, "HP": 20, "Inventory": [], "fought": False, "Day": 1,\
               "Location": "T", "yValue": 0, "xValue": 0, "orbLocation": "0,0", "town1": "0,0", "town2": "0,0",\
               "town3": "0,0", "town4": "0,0"}

# (Variables relating to main opponents.)
rat = {"Name": "Rat", "MinDamage": 1, "MaxDamage": 3, "Defence": 1, "HP": 10}
ratKing = {"Name": "Rat King", "MinDamage": 6, "MaxDamage": 8, "Defence": 5, "HP": 25}


# (This is a list constantly being used to determine status of the game, such as battles, location of orb, etc.)
world_map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]

# |=========|
# |FUNCTIONS|
# |=========|

# (Start-up menu for players.)
def startingMenu():
        print("|  |                                     |  |")
        print("|  |                                     |  |")
        print("|xx|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|xx|")
        print('|         W   E   L   C   O   M   E         |')
        print("|                                           |")
        print("|                  T   O                    |")
        print("|                                           |")
        print("|  R    A    T   V   E   N   T   U   R   E  |")
        print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
        menuChoices = ['New Game', 'Resume Game', 'View Highscores', 'Exit Game']
        for x in range(len(menuChoices)):
                print("{}) {}".format(x+1, menuChoices[x]))
        try:
            menuChoose = int(input("Enter Choice: ").strip())
            
        # (If player inputs anything other than a string, it will issue an error. This will then trigger the except function.)
        except ValueError:
            print()
            print("=-=-=-=-=-=-=-=-=-=-=-=-INVALID OPTION=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print()
            startingMenu()

        try:
            # (Makes new text file containing new player stats)
            if menuChoose == 1:
                    currentLocation = "T"
                    file = open("saveFile.txt", 'w')
                    file.write("The Hero\n")
                    file.write("2\n")
                    file.write("4\n")
                    file.write("1\n")
                    file.write("20\n")
                    file.write("List()\n")
                    file.write("False\n")
                    file.write("1\n")
                    file.write("T\n")
                    file.write("0\n")
                    file.write("0\n")
                    
                    # (A loop to randomise orb location and ensure it's placement\
                    #  is not too close to the starting position.)

                    while True:
                        randOrb1 = randint(0, 7)
                        randOrb2 = randint(0, 7)
                        if randOrb1 <= 3 or randOrb2 <= 3:
                            continue
                        else:
                            # (Ensure that orb placement is not the same as Rat King position.)
                            if randOrb1 == 7 and randOrb2 == 7:
                                continue
                            else:
                                orbLocation = str(randOrb1) + "," + str(randOrb2)
                                playerStats["orbLocation"] = orbLocation
                                break
                    file.write(orbLocation + "\n")

                    #--------------------------------------------------------------------------------------------------------
                    # (This whole section is code solely for randomising town locations and ensuring they are not too close - three spaces apart.)
                    # (This section was admittedly rushed. There was room for function usage, better operator usage such as AND, OR and elifs.)

                    while True:
                        xtown1 = randint(0,7)
                        ytown1 = randint(0,7)
                        total1 = xtown1 + ytown1
                        town1 = "{},{}".format(ytown1, xtown1)
                        if xtown1 == 0 and ytown1 == 0:
                            continue
                        elif xtown1==7 and ytown1 == 7:
                            continue
                        elif town1 == orbLocation:
                                continue
                        
                        elif xtown1-0<=3 and ytown1-0<=3 and xtown1+ytown1<4:
                            continue
                        else:
                            break
                       
                    while True:    
                        xtown2 = randint(0,7)
                        ytown2 = randint(0,7)
                        total2 = xtown2 + ytown2
                        town2 = "{},{}".format(ytown2, xtown2)
                       
                        if xtown2==xtown1 and ytown2==ytown1:
                            continue
                        elif town2 == orbLocation:
                                continue
                        elif xtown2 == 0 and ytown2 == 0:
                            continue
                        elif xtown2==7 and ytown2 == 7:
                            continue
                        elif abs(xtown2-0)<=3 and abs(ytown2-0)<=3 and xtown2+ytown2<4:
                            continue
                        
                        else:
                            if abs(xtown1 - xtown2) <=3:
                                    if abs(ytown1 - ytown2) <=3:
                                        if (xtown1 - xtown2)+(ytown1 - ytown2)<4:
                                            continue
                                        else:
                                            break
                                    else:
                                        break
                            else:
                                break
                        
                    while True: 
                        xtown3 = randint(0,7)
                        ytown3 = randint(0,7)
                        total3 = xtown3 + ytown3
                        town3 = "{},{}".format(ytown3, xtown3)
                      
                        if xtown2==xtown3 and ytown2==ytown3:
                            continue
                        elif town3 == orbLocation:
                                continue
   
                        elif xtown3 == 0 and ytown3 == 0:
                            continue
                        elif xtown3==7 and ytown3 == 7:
                            continue
                        elif abs(xtown3-0)<=3 and abs(ytown3-0)<=3 and xtown3+ytown3<4:
                            continue
    
                        else:
                            if abs(xtown3 - xtown1) <=3:
                                if abs(ytown3 - ytown1) <=3:
                                    if (xtown3 - xtown1)+(ytown3 - ytown1)<4:
                                            continue
                                    else:
                                        break
                                else:   
                                    if abs(xtown3 - xtown2) <=3:
                                        if abs(ytown3 - ytown2) <=3:
                                            if (xtown3 - xtown2)+(ytown3 - ytown2)<4:
                                                continue
                                            else:
                                                break      
                                        else:
                                            break
                                    else:
                                        break
                            else:
                                if abs(xtown3 - xtown2) <=3:
                                        if abs(ytown3 - ytown2) <=3:
                                            if (xtown3 - xtown2)+(ytown3 - ytown2)<4:
                                                continue
                                            else:
                                                break
                                            
                                        else:
                                            break
                                else:
                                    break
                        

                    while True:   
                        xtown4 = randint(0,7)
                        ytown4 = randint(0,7)
                        total4 = xtown4 + ytown4
                        town4 = "{},{}".format(ytown4, xtown4)
                                
                        if xtown3==xtown4 and ytown3==ytown4:
                            continue
                        elif town4 == orbLocation:
                                continue

                        elif xtown4 == 0 and ytown4 == 0:
                            continue
                        elif xtown4==7 and ytown4 == 7:
                            continue
                        elif abs(xtown4-0)<=3 and abs(ytown4-0)<=3 and xtown4+ytown4<4:
                            continue
                
                        else:
            
                                if abs(xtown1 - xtown4) <=3:
                                    if abs(ytown1 - ytown4) <=3:
                                        if (xtown1 - xtown4)+(ytown1 - ytown4)<4:
                                            continue
                                        else:
                                            if abs(xtown4 - xtown2) <=3:
                                                if abs(ytown4 - ytown2) <=3:
                                                    if (xtown4 - xtown2)+(ytown4 - ytown2)<4:
                                                        continue
                                                else:
                                                    if abs(xtown4 - xtown3) <=3:
                                                        if abs(ytown4 - ytown3) <=3:
                                                            if (xtown4 - xtown3)+(ytown4 - ytown3)<4:
                                                                continue
                                                            else:
                                                                break
                                                        else:
                                                            break
                                                    else:
                                                        break
                                            else:
                                                if abs(xtown4 - xtown3) <=3:
                                                        if abs(ytown4 - ytown3) <=3:
                                                            if (xtown4 - xtown3)+(ytown4 - ytown3)<4:
                                                                continue
                                                            else:
                                                                break
                                                        else:
                                                            break
                                                else:
                                                    break
                                                
                                        
                                    else:
                    
                                        if abs(xtown4 - xtown2) <=3:
                                            if abs(ytown4 - ytown2) <=3:
                                                if (xtown4 - xtown2)+(ytown4 - ytown2)<4:
                                                    continue
                                                else:
                                                    if abs(xtown4 - xtown3) <=3:
                                                        if abs(ytown4 - ytown3) <=3:
                                                            if (xtown4 - xtown3)+(ytown4 - ytown3)<4:
                                                                continue
                                                        else:
                                                            break
                                                    else:
                                                        break
                                                        
                                                    
                                            else:
                            
                                                if abs(xtown4 - xtown3) <=3:
                                                    if abs(ytown4 - ytown3) <=3:
                                                        if (xtown4 - xtown3)+(ytown4 - ytown3)<4:
                                                            continue
                                                        else:
                                                            break
                                                    else:
                                                        break
                                                        
                                                else:
                                                    break
                                        else:
                                            if abs(xtown4 - xtown2) <=3:
                                                if abs(ytown4 - ytown2) <=3:
                                                    if (xtown4 - xtown2)+(ytown4 - ytown2)<4:
                                                        continue
                                                    else:
                                                        break
                                                    
                                                else:
                            
                                                    if abs(xtown4 - xtown3) <=3:
                                                        if abs(ytown4 - ytown3) <=3:
                                                            if (xtown4 - xtown3)+(ytown4 - ytown3)<4:
                                                                continue
                                                            else:
                                                                break
                                                        else:
                                                            break
                                                            
                                                    else:
                                                        break
                                            else:
                                                if abs(xtown4 - xtown3) <=3:
                                                    if abs(ytown4 - ytown3) <=3:
                                                        if (xtown4 - xtown3)+(ytown4 - ytown3)<4:
                                                            continue
                                                        else:
                                                            break
                                                    else:
                                                        break
                                                else:
                                                    break
                                                    
                                                
                                else:
                                    if abs(xtown4 - xtown3) <=3:
                                        if abs(ytown4 - ytown3) <=3:
                                            if (xtown4 - xtown3)+(ytown4 - ytown3)<4:
                                                continue
                                            else:
                                                if abs(xtown4 - xtown2) <=3:
                                                    if abs(ytown4 - ytown2) <=3:
                                                        if (xtown4 - xtown2)+(ytown4 - ytown2)<4:
                                                            continue
                                                        else:
                                                            break
                                                    else:
                                                        break
                                                else:
                                                    break
                                            
                                        else:
                                            if abs(xtown4 - xtown2) <=3:
                                                if abs(ytown4 - ytown2) <=3:
                                                    if (xtown4 - xtown2)+(ytown4 - ytown2)<4:
                                                        continue
                                                    else:
                                                        break
                                                else:
                                                    break
                                            else:
                                                break
                                    else:
                                        if abs(xtown4 - xtown2) <=3:
                                                if abs(ytown4 - ytown2) <=3:
                                                    if (xtown4 - xtown2)+(ytown4 - ytown2)<4:
                                                        continue
                                                    else:
                                                        break
                                                    
                                                else:
                                                    break
                                        else:
                                            break
                    #--------------------------------------------------------------------------------------------------------


                    # (This notes the newly-generated town placement such that it can be saved and loaded in properly later on.)
                    file.write(town1 + "\n")
                    file.write(town2 + "\n")
                    file.write(town3 + "\n")
                    file.write(town4 + "\n")
                    file.close()

                    # (This section just ensures the towns are assigned in the currently empty world_list.)
                    playerStats["town1"] = town1
                    splt = town1.split(",")
                    world_map[int(splt[0])][int(splt[1])] = 'T'
                    playerStats["town2"] = town2
                    splt = town2.split(",")
                    world_map[int(splt[0])][int(splt[1])] = 'T'
                    playerStats["town3"] = town3
                    splt = town3.split(",")
                    world_map[int(splt[0])][int(splt[1])] = 'T'
                    playerStats["town4"] = town4
                    splt = town4.split(",")
                    world_map[int(splt[0])][int(splt[1])] = 'T'

                
                    gameMenu1()
                
            # (Read lines from saveFile.txt and put into dictionary - playerStats.)
            elif menuChoose == 2:
                try:
                        file = open("saveFile.txt", "r")
                        for x in playerStats:
                                currentLine = file.readline().rstrip()
                                if currentLine == "List()":
                                        playerStats[x] = list()
                            
                                elif currentLine == "OrbOfPower":
                                        playerStats[x] = ["OrbOfPower"]
                                elif type(currentLine) == bool:
                                        playerStats[x] = bool(currentLine)
                                else:
                                        try:
                                                playerStats[x] = int(currentLine)
                                        except:
                                            if currentLine == "":
                                                playerStats[x] = " "
                                            else:
                                                playerStats[x] = currentLine
                        file.close()
                    

                        print()
                        print("Save game loaded.")

                        gameMenu1()
                except:
                    print()
                    print("No save data.")
                    print()
                    startingMenu()

                # (Reads highscore.txt and prints it.)
            elif menuChoose == 3:
                try:
                    file = open('highscores.txt', 'r')
                    print("Player Name|Total Days")
                    print("-----------|-----------")
                    
                    highscores = {}
                    for line in file:
                        data = line.split(',')
                        highscores[data[0]] = data[1]
                        
                    for y in range(len(highscores)):
                        currentHigh = min(highscores, key=highscores.get)
                        print("{:<11}|{:<10}".format(currentHigh, highscores[currentHigh]))
                        
                        del highscores[currentHigh]
                    startingMenu()
                except:
                    print()
                    print("No highscores yet!")
                    print()
                    startingMenu()

            # (Leave game by not taking action, which is feasible since no major loops are occuring.)                            
            elif menuChoose == 4:
                    print("Leaving game....")
            # (If player inputs anything other than the three int() numbers, this will initiate.)
            else:
                print()
                print("=-=-=-=-=-=-=-=-=-=-=-=-INVALID OPTION=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print()
                startingMenu()\
        # (In the case that a systemExit error is raised (usually due to picking the 'Leave Game' option), this ensures that the application closes properly.)
        except SystemExit:
           exit(0)

# (Display map alongside player position.)
def viewMap():
        
         # (This section just ensures the towns are assigned in the currently empty world_list.)
        splt = playerStats["town1"].split(",")
        world_map[int(splt[0])][int(splt[1])] = 'T'
        splt = playerStats["town2"].split(",")
        world_map[int(splt[0])][int(splt[1])] = 'T'
        splt = playerStats["town3"].split(",")
        world_map[int(splt[0])][int(splt[1])] = 'T'
        splt = playerStats["town4"].split(",")
        world_map[int(splt[0])][int(splt[1])] = 'T'
        
        # (This incorporates the hero's location into the world_map list.)
        if world_map[playerStats["yValue"]][playerStats["xValue"]] == "T":
                world_map[playerStats["yValue"]][playerStats["xValue"]] = "H/T"
        elif world_map[playerStats["yValue"]][playerStats["xValue"]] == "K":
                world_map[playerStats["yValue"]][playerStats["xValue"]] = "H/K"
        elif world_map[playerStats["yValue"]][playerStats["xValue"]] == " ":
            world_map[playerStats["yValue"]][playerStats["xValue"]] = "H"

        

        
        # (This is the main print function for displaying the map.)
        print()
        for x in world_map:
                print("+---+---+---+---+---+---+---+---+")
                print("+{:^3}+{:^3}+{:^3}+{:^3}+{:^3}+{:^3}+{:^3}+{:^3}+".format(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]))
        print("+---+---+---+---+---+---+---+---+")
    
# (This is for Menu1 (Main Game Menu), shown later in the code.)
def ascertainLocation(place):
        if place == "T":
                return "You are in a town."
        elif place == " ":
                return "You are out in the open."
        elif place == "K":
                return "You see the Rat King!"

# (This function is essential in the main Move function, to replace the values\
#   in world_map to its initial values after moving.)
def moveReplace():
    if world_map[playerStats["yValue"]][playerStats["xValue"]] == "H/T":
        world_map[playerStats["yValue"]][playerStats["xValue"]] = "T"
       
    elif world_map[playerStats["yValue"]][playerStats["xValue"]] == "H":
        world_map[playerStats["yValue"]][playerStats["xValue"]] = " "

    elif world_map[playerStats["yValue"]][playerStats["xValue"]] == "H/K":
        world_map[playerStats["yValue"]][playerStats["xValue"]] = "K"

# (Main function for moving around the world_map, taking into consideration the player's position and world_map's limit.)
def moveSys():
    while True:
        try:
            playerMove = str(input("Your move: "))

            # (Potential for function here.)
        
            if playerMove.upper() == "W":
                if playerStats["yValue"] == 0:
                    print()
                    print("You can't move out of the map!")
                    continue
                else:
                    moveReplace()
                    playerStats["yValue"] -= 1
                    playerStats["Location"] = world_map[playerStats["yValue"]][playerStats["xValue"]]
                    playerStats["Day"] += 1
                    playerStats["fought"] = False

                    break

            elif playerMove.upper() == "A":
                if playerStats["xValue"] == 0:
                    print()
                    print("You can't move out of the map!")
                    continue
                else:
                    moveReplace()
                    playerStats["xValue"] -= 1
                    playerStats["Location"] = world_map[playerStats["yValue"]][playerStats["xValue"]]
                    playerStats["Day"] += 1
                    playerStats["fought"] = False

                    break
            elif playerMove.upper() == "S":
                if playerStats["yValue"] == 7:
                    print()
                    print("You can't move out of the map!")
                    continue
                else:
                    moveReplace()
                    playerStats["yValue"] += 1
                    playerStats["Location"] = world_map[playerStats["yValue"]][playerStats["xValue"]]
                    playerStats["Day"] += 1
                    playerStats["fought"] = False

                    break
            elif playerMove.upper() == "D":
                if playerStats["xValue"] == 7:
                    print()
                    print("You can't move out of the map!")
                    continue
                else:
                    moveReplace()
                    playerStats["xValue"] += 1
                    playerStats["Location"] = world_map[playerStats["yValue"]][playerStats["xValue"]]
                    playerStats["Day"] += 1
                    playerStats["fought"] = False

                    break
            else:
                print()
                print("=-=-=-=-=-=-=-=-=-=-=-=-INVALID OPTION=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print()

        except TypeError:
            print()
            print("=-=-=-=-=-=-=-=-=-=-=-=-INVALID OPTION=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print()
      
# (Game Menu for in-game actions, pre move/ post sense orb)            
def gameMenu1():
    while True:
        try:
            gameChoices = ["View Character","View Map","Move",\
                           "Rest","Save Game","Exit Game"]
            print()
            print("Day {}: {}".format(playerStats["Day"], ascertainLocation(playerStats["Location"])))

            # (Triggers after moving into an empty space on world_map.)
            if playerStats["Location"] == " " and playerStats["fought"] == False:
                    rat["HP"] = 10
                    print(playerStats["Location"])
                    battleAlert(rat)
            # (Triggers after moving into the "K" space on world_map.)
            elif playerStats["fought"] == False and playerStats["Location"] == "K":
                ratKing["HP"] = 25
                battleAlert(ratKing)
            else:
                # (Triggers for town spaces/ post sense orb / post rest, players are shown the game menu.)
                for y in range(len(gameChoices)):
                    print("{}) {}".format(y+1, gameChoices[y]))
                gameAction = int(input("Enter choice: "))

                # (Calls the displayStats function shown in the code later.)
                if gameAction == 1:
                    displayStats()
                    continue
            
                # (Calls the viewMap function shown in the code earlier.)
                elif gameAction == 2:
                    viewMap()
                    continue

                # (Calls viewMap function, followed by the moveSys function. This then continues on with battleAlert and battleSys function.)
                elif gameAction == 3:
                    print()
                    viewMap()
                    print("W = up; A = left; S = down; D = right")
                    moveSys()       

                # (This is the rest option; it resets the player's health to full and adds one day.)
                elif gameAction == 4:
                    playerStats["HP"] = 20
                    playerStats["Day"] += 1
                    print()
                    print("You are fully healed.")
                # (Save function takes the values in the playerStats dictionary and transfers them into the txt file created earlier.)
                elif gameAction == 5:
                    file = open("saveFile.txt", 'w')
                    file.write(playerStats["Name"] + "\n")
                    file.write(str(playerStats["MinDamage"]) + "\n")
                    file.write(str(playerStats["MaxDamage"]) + "\n")
                    file.write(str(playerStats["Defence"]) + "\n")
                    file.write(str(playerStats["HP"]) + "\n")
                    if playerStats["Inventory"] == []:
                            file.write("List()\n")
                    else:
                            for x in playerStats["Inventory"]:
                                    file.write(x + "\n")
                    file.write(str(playerStats["fought"]) + "\n")
                    file.write(str(playerStats["Day"]) + "\n")
                    file.write(playerStats["Location"] + "\n")
                    file.write(str(playerStats["yValue"]) + "\n")
                    file.write(str(playerStats["xValue"]) + "\n")
                    file.write(playerStats["orbLocation"] + "\n")
                    file.write(playerStats["town1"] + "\n")
                    file.write(playerStats["town2"] + "\n")
                    file.write(playerStats["town3"] + "\n")
                    file.write(playerStats["town4"] + "\n")

                    file.close()
                    print()
                    print("Game has been saved.")

                    continue
                
                
                # (Leaves game by breaking the "while True" loop, using break function.)
                elif gameAction == 6:
                    print("Leaving game....")
                    break

                else:
                    print()
                    print("=-=-=-=-=-=-=-=-=-=-=-=-INVALID OPTION=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                    print()
        except ValueError:
            print()
            print("=-=-=-=-=-=-=-=-=-=-=-=-INVALID OPTION=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print()


# (Outdoor menu, displayed after beating the opponent OR running away.)
def gameMenu2(opp):

        # (This section ensures that the player, if they have not beaten the opponent, is only given the option to run or exit. Choosing anything will make them engage in battle again.)
        if playerStats["fought"] == False:
            try:
                gameChoices2 = ["View Character","View Map","Move",\
                           "Sense Orb","Exit Game"]
                for y in range(len(gameChoices2)):
                    print("{}) {}".format(y+1, gameChoices2[y]))
                gameAction = int(input("Enter choice: "))
            
                if gameAction == 3 or gameAction == 5:
                    if gameAction == 3:
                        viewMap()
                        moveSys()

                    if gameAction == 5:
                        print("Leaving game....")
                        raise SystemExit(0) 
                    
                elif gameAction == 1 or gameAction == 2 or gameAction == 4:
                    battleAlert(opp)

                else:
                    print()
                    print("=-=-=-=-=-=-=-=-=-=-=-=-INVALID OPTION=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                    print()

            except ValueError:
                print()
                print("=-=-=-=-=-=-=-=-=-=-=-=-INVALID OPTION=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print()
                gameMenu2(opp)
        
        # (If player has defeated the opponent, this section of code will then run.)
        elif playerStats["fought"] == True:
            while True:
                try:
                    gameChoices2 = ["View Character","View Map","Move",\
                           "Sense Orb","Exit Game"]
                    for y in range(len(gameChoices2)):
                        print("{}) {}".format(y+1, gameChoices2[y]))
                    gameAction = int(input("Enter choice: "))
                
                    # (This calls the displayStats function.)
                    if gameAction == 1:
                        displayStats()
                
                    # (This calls the viewMap function.)    
                    elif gameAction == 2:
                        viewMap()

                    # (This makes sure that the opponent's health goes back to full on the next encounter.) 
                    elif gameAction == 3:
                            viewMap()
                           
                            if opp == rat:
                                opp["HP"] = 10
                            elif opp == ratKing:
                                opp["HP"] = 25
                            moveSys()
                            break
                    # (This calls the senseOrb function, shown later in the code. It also adds one day.)
                    elif gameAction == 4:
                        senseOrb()
                        playerStats["Day"] += 1
                        break
                    
                    # (This raises a SystemError, that is handled by an except function earlier in the code for the first menu.)
                    elif gameAction == 5:
                        print("Leaving game....")
                        raise SystemExit(0)

                    else:
                        print()
                        print("=-=-=-=-=-=-=-=-=-=-=-=-INVALID OPTION=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                        print()

                except ValueError:
                    print()
                    print("=-=-=-=-=-=-=-=-=-=-=-=-INVALID OPTION=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                    print()


# (This function is for finding the location of the orb relative to the player's location, and also for picking it up.)
def senseOrb():

    # (Unloads the string from playerStats and makes it into a list, while converting them into integers.)
    orbLocation = playerStats["orbLocation"].split(",")
    for x in range(len(orbLocation)):
        orbLocation[x] = int(orbLocation[x])
    
    # (In the case that the player uses senseOrb at the space where the orb is located, this runs.)
    if orbLocation[0] == playerStats["yValue"] and orbLocation[1] == playerStats["xValue"]:
        playerStats["Inventory"] += ["OrbOfPower"]
        print()
        print("You found the Orb of Power!")
        print("Your attack increases by 5!")
        playerStats["MinDamage"] += 5
        playerStats["MaxDamage"] += 5
        print("Your defence increases by 5!")
        playerStats["Defence"] += 5

    # (This section takes the X and Y values of the player's location, compares it with the orb's location on the world_map\
    #  and gives a certain compass direction.)
    else:
        if playerStats["yValue"] < orbLocation[0]:
            if playerStats["xValue"] < orbLocation[1]:
                orbplace = "southeast"
            elif playerStats["xValue"] == orbLocation[1]:
                orbplace = "south"
            elif playerStats["xValue"] > orbLocation[1]:
                orbplace = "southwest"

        elif playerStats["yValue"] == orbLocation[0]:
            if playerStats["xValue"]< orbLocation[1]:
                orbplace = "east"
            elif playerStats["xValue"] > orbLocation[1]:
                orbplace = "west"

        if playerStats["yValue"] > orbLocation[0]:
            if playerStats["xValue"] < orbLocation[1]:
                orbplace = "northeast"
            elif playerStats["xValue"] == orbLocation[1]:
                orbplace = "north"
            elif playerStats["xValue"] > orbLocation[1]:
                orbplace = "northwest"
        print()
        print("You sense that the Orb Of Power is to the {}.".format(orbplace))


# (View Character option in Game Menu.)
def displayStats():
    print()
    print(playerStats["Name"])
    print("Damage: {}-{}".format(playerStats["MinDamage"],\
                                 playerStats["MaxDamage"]))
    print("Defence: {}".format(playerStats["Defence"]))
    print("HP: {}".format(playerStats["HP"]))
    if "OrbOfPower" in playerStats["Inventory"]:
        print("You are holding the Orb Of Power.")

# (Incoming battle alert.)
def battleAlert(opp):
     while playerStats["fought"] == False:
         if playerStats["Location"] == "T":
             break
         elif playerStats["Location"] == "K" and opp == rat:
             break
         else:
             print("Encounter! - {}".format(opp["Name"]))
             print("Damage: {}-{}".format(opp["MinDamage"], opp["MaxDamage"]))
             print("Defence: {}".format(opp["Defence"]))
             print("HP: {}".format(opp["HP"]))
             battleSystem(opp)
        
# (Main battle system.)
def battleSystem(opp):
  
   try: 
            print("(1) Fight")
            print("(2) Run")
            fightChoice = int(input("Enter choice: "))

            # (Generates random numbers based off min damage and max damage of player and opponent respectively, and substitutes it with their defence stats respectively as well.)
            if fightChoice == 1:
                damage = (randint(playerStats["MinDamage"], playerStats["MaxDamage"])) - opp["Defence"]

                # (In the situation where the opponent does negative damage, it is just equated to zero, since negative damage would mean adding health to the player/opponent.)
                if damage < 0:
                    damage = 0
                print()

                # (If player has not found the Orb Of Power yet, they will not do any damage to the ratKing.)
                if opp == ratKing and "OrbOfPower" not in playerStats["Inventory"]:
                    print("You do not have the Orb of Power - the Rat King is immune!")
                    damage = 0

                print("You deal {} damage to the {}".format(damage, opp["Name"]))
                opp["HP"] -= damage

                # (Since player attacks first, this code has to come first before taking into account the opponent's attack.)
                if opp["HP"] <= 0:
                    playerStats["fought"] = True
                    print("The {} is dead! You are victorious!".format(opp["Name"]))

                    # (If opponent is ratKing, killing him will result in a game end.)
                    if opp == ratKing:
                        print("Congratulations, you have defeated the Rat King!")
                        print("The world is")
                        print("S   A   V   E   D")
                        print()
                        print("Y   O   U       W   I   N!")
                        print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
                        print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
                        print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
                        print("Input your name to be placed into the scoreboards!")
                        name = str(input("Name: "))
                        try:
                            file = open("highscores.txt", "r")
                            allLines = file.read()
                            file.close()
                            file2 = open("highscores.txt", "w")
                            file2.write(allLines)
                            file2.write("{},{}\n".format(name, playerStats["Day"]))
                            file.close()
                            print("Leaving game...")

                        except:
                            file = open("highscores.txt", "w")
                            file.write("{},{}\n".format(name, playerStats["Day"]))
                            file.close()
                            print("Leaving game...")
                        
                        finally:
                            raise SystemExit(0)

                    gameMenu2(opp)
            
                # (Opponent's attack, randomised and subtracted by player's defence.)
                else:
                    oppDamage = (randint(opp["MinDamage"], opp["MaxDamage"])) - playerStats["Defence"]

                    # (Again, if damage is negative, it is equated to zero, same reasons as above.)
                    if oppDamage < 0:
                        oppDamage = 0

                    print("Ouch! The {} hit you for {} damage!".format(opp["Name"], oppDamage))
                    playerStats["HP"] -= oppDamage

                    # (In the chance that the player's HP reaches zero, the game will end.)
                    if playerStats["HP"] <= 0:
                        print()
                        print("Player has been slain by {}....".format(opp["Name"]))
                        print()
                        print("G   A   M   E")
                        print()
                        print("O   V   E   R")
                        raise SystemExit(0)

                    # (Added a warning message, for when the player's health gets low.)
                    elif playerStats["HP"] <= 5 :
                        print("Beware! Critical health!")

            # (This runs when the player decides to run.)
            elif fightChoice == 2:

                # (Resets opponent's health, and runs the outdoor menu.)
                if opp == rat:
                            opp["HP"] = 10

                elif opp == ratKing:
                    opp["HP"] = 25

                print()
                print("You run and hide.")
                gameMenu2(opp)
                
            
            else:
                print()
                print("=-=-=-=-=-=-=-=-=-=-=-=-INVALID OPTION=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print() 
                    
   except ValueError:
                print()
                print("=-=-=-=-=-=-=-=-=-=-=-=-INVALID OPTION=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print()

# |==============|
# |MAIN PROCESSES|
# |==============|

startingMenu()



