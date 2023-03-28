# jmeno hada z konfiguracniho souboru config.py
from config import NAME

import random

# povolene smery pohybu hada
DIRECTIONS = ('Right', 'Left', 'Up', 'Down')

# nedostane data hry, vraci jmeno hada
def index():
    return NAME

# dostane data hry, vraci prazdnou odpoved
def init(game):
    return ''

# dostane data hry, vraci smer pohybu hada
def move(game):
    
    result = None
    
    moveRightPossible = True
    moveLeftPossible = True
    moveUpPossible = True
    moveDownPossible = True
    
    ##### KONTROLY MOŽNÝCH POHYBŮ #####
    
    def moveCheck(game, head):
            if head["x"] == 0:
                moveLeftPossible = False
                print("Nejde doleva")
            if head["x"] == game["board"]["width"] - 1:
                moveRightPossible = False
                print("Nejde doprava")
            if head["y"] == 0:
                moveDownPossible = False
                print("Nejde dolu")
            if head["y"] == game["board"]["height"] - 1:
                moveUpPossible = False
                print("Nejde nahoru")
                
            ### Kontrola našeho těla
            if not len(game["you"]["body"]) == 0:
                for segmentTela in game["you"]["body"]:
                    if head["x"] - 1 == segmentTela["x"] and head["y"] == segmentTela["y"]:
                        moveLeftPossible = False
                        print("vlevo je telo", segmentTela["x"], segmentTela["y"])
                    if head["x"] + 1 == segmentTela["x"] and head["y"] == segmentTela["y"]:
                        moveRightPossible = False
                        print("vpravo je telo", segmentTela["x"], segmentTela["y"])
                    if head["y"] - 1 == segmentTela["y"] and head["x"] == segmentTela["x"]:
                        moveDownPossible = False
                        print("dole je telo", segmentTela["x"], segmentTela["y"])
                    if head["y"] + 1 == segmentTela["y"] and head["x"] == segmentTela["x"]:
                        moveUpPossible = False
                        print("nahore je telo", segmentTela["x"], segmentTela["y"])
                    
            ### Kontrola překážek
            if not len(game["board"]["obstacles"]) == 0:
                for prekazka in game["board"]["obstacles"]:
                    if head["x"] + 1 == prekazka["x"] and head["y"] == prekazka["y"]:
                        moveRightPossible = False
                    if head["x"] - 1 == prekazka["x"] and head["y"] == prekazka["y"]:
                        moveLeftPossible = False
                    if head["y"] - 1 == prekazka["y"] and head["x"] == prekazka["x"]:
                        moveDownPossible = False
                    if head["y"] + 1 == prekazka["y"] and head["x"] == prekazka["x"]:
                        moveUpPossible = False
                        
            return moveUpPossible, moveDownPossible, moveLeftPossible, moveRightPossible
    
    ### Kontrola hran hracího pole
    if game["you"]["head"]["x"] == 0:
        moveLeftPossible = False
        print("Nejde doleva")
    if game["you"]["head"]["x"] == game["board"]["width"] - 1:
        moveRightPossible = False
        print("Nejde doprava")
    if game["you"]["head"]["y"] == 0:
        moveDownPossible = False
        print("Nejde dolu")
    if game["you"]["head"]["y"] == game["board"]["height"] - 1:
        moveUpPossible = False
        print("Nejde nahoru")
        
    ### Kontrola našeho těla
    if not len(game["you"]["body"]) == 0:
        for segmentTela in game["you"]["body"]:
            if game["you"]["head"]["x"] - 1 == segmentTela["x"] and game["you"]["head"]["y"] == segmentTela["y"]:
                moveLeftPossible = False
                print("vlevo je telo", segmentTela["x"], segmentTela["y"])
            if game["you"]["head"]["x"] + 1 == segmentTela["x"] and game["you"]["head"]["y"] == segmentTela["y"]:
                moveRightPossible = False
                print("vpravo je telo", segmentTela["x"], segmentTela["y"])
            if game["you"]["head"]["y"] - 1 == segmentTela["y"] and game["you"]["head"]["x"] == segmentTela["x"]:
                moveDownPossible = False
                print("dole je telo", segmentTela["x"], segmentTela["y"])
            if game["you"]["head"]["y"] + 1 == segmentTela["y"] and game["you"]["head"]["x"] == segmentTela["x"]:
                moveUpPossible = False
                print("nahore je telo", segmentTela["x"], segmentTela["y"])
            
    ### Kontrola překážek
    if not len(game["board"]["obstacles"]) == 0:
        for prekazka in game["board"]["obstacles"]:
            if game["you"]["head"]["x"] + 1 == prekazka["x"] and game["you"]["head"]["y"] == prekazka["y"]:
                moveRightPossible = False
            if game["you"]["head"]["x"] - 1 == prekazka["x"] and game["you"]["head"]["y"] == prekazka["y"]:
                moveLeftPossible = False
            if game["you"]["head"]["y"] - 1 == prekazka["y"] and game["you"]["head"]["x"] == prekazka["x"]:
                moveDownPossible = False
            if game["you"]["head"]["y"] + 1 == prekazka["y"] and game["you"]["head"]["x"] == prekazka["x"]:
                moveUpPossible = False
    
    ##### JDE PO JIDLE #####
    if not len(game["board"]["food"]) == 0:
        print("JE JIDLO")
        ### Pokud je jídlo v levo od hlavy
        i=0
        dalsiJidlo = game["board"]["food"][0]
        for jidlo in game["board"]["food"]:
            i += 1
            if jidlo["x"] <= dalsiJidlo["x"] and jidlo["y"] <= dalsiJidlo["y"]:
                dalsiJidlo = jidlo
            blizkeJidlo = dalsiJidlo
                
        if not len(game["you"]["body"]) == 0:
            if blizkeJidlo["x"] < game["you"]["head"]["x"]:
                if moveLeftPossible:
                    for segmentTela in game["you"]["body"]:
                        if segmentTela["x"] <= game["you"]["head"]["x"]:
                            print("SEGMENT NEKDE VLEVO!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["x"] > segmentTela["x"]:
                                head["x"] -= ind
                                possible = moveCheck(game, head)[2]
                                ind += 1
                            if possible == True:
                                result = "Left"
                            else:
                                pass
                        else:
                            result = "Left"
                elif moveUpPossible:
                    for segmentTela in game["you"]["body"]:
                        if segmentTela["y"] >= game["you"]["head"]["y"]:
                            print("SEGMENT NEKDE NAHORE!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["y"] < segmentTela["y"]:
                                head["y"] += ind
                                possible = moveCheck(game, head)[0]
                                ind += 1
                            if possible == True:
                                result = "Up"
                            else:
                                pass
                        else:
                            result = "Up"
                elif moveDownPossible:
                    for segmentTela in game["you"]["body"]:
                        if segmentTela["y"] <= game["you"]["head"]["y"]:
                            print("SEGMENT NEKDE DOLE!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["y"] > segmentTela["y"]:
                                head["y"] -= ind
                                possible = moveCheck(game, head)[1]
                                ind += 1
                            if possible == True:
                                result = "Down"
                            else:
                                pass
                        else:
                            result = "Down"
                elif moveRightPossible:
                    for segmentTela in game["you"]["body"]:
                        if segmentTela["x"] >= game["you"]["head"]["x"]:
                            print("SEGMENT NEKDE VPRAVO!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["x"] < segmentTela["x"]:
                                head["x"] += ind
                                possible = moveCheck(game, head)[3]
                                ind += 1
                            if possible == True:
                                result = "Right"
                            else:
                                pass
                        else:
                            result = "Right"                    
                print("JIDLO VLEVO")
                        
            ### Pokud je jídlo v pravo od hlavy
            elif blizkeJidlo["x"] > game["you"]["head"]["x"]:
                if moveRightPossible:
                    for segmentTela in game["you"]["body"]:
                        if segmentTela["x"] >= game["you"]["head"]["x"]:
                            print("SEGMENT NEKDE VPRAVO!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["x"] < segmentTela["x"]:
                                head["x"] += ind
                                possible = moveCheck(game, head)[3]
                                ind += 1
                            if possible == True:
                                result = "Right"
                            else:
                                pass
                        else:
                            result = "Right"
                elif moveUpPossible:
                   for segmentTela in game["you"]["body"]:
                        if segmentTela["y"] >= game["you"]["head"]["y"]:
                            print("SEGMENT NEKDE NAHORE!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["y"] < segmentTela["y"]:
                                head["y"] += ind
                                possible = moveCheck(game, head)[0]
                                ind += 1
                            if possible == True:
                                result = "Up"
                            else:
                                pass
                        else:
                            result = "Up"
                elif moveDownPossible:
                    for segmentTela in game["you"]["body"]:
                        if segmentTela["y"] <= game["you"]["head"]["y"]:
                            print("SEGMENT NEKDE DOLE!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["y"] > segmentTela["y"]:
                                head["y"] -= ind
                                possible = moveCheck(game, head)[1]
                                ind += 1
                            if possible == True:
                                result = "Down"
                            else:
                                pass
                        else:
                            result = "Down"
                elif moveLeftPossible:
                    for segmentTela in game["you"]["body"]:
                        if segmentTela["x"] <= game["you"]["head"]["x"]:
                            print("SEGMENT NEKDE VLEVO!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["x"] > segmentTela["x"]:
                                head["x"] -= ind
                                possible = moveCheck(game, head)[2]
                                ind += 1
                            if possible == True:
                                result = "Left"
                            else:
                                pass
                        else:
                            result = "Left"
                            
                print("JIDLO VPRAVO")
                            
            ### Pokud je jídlo pod hlavou
            elif blizkeJidlo["y"] < game["you"]["head"]["y"]:
                if moveDownPossible:
                    for segmentTela in game["you"]["body"]:
                        if segmentTela["y"] <= game["you"]["head"]["y"]:
                            print("SEGMENT NEKDE DOLE!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["y"] > segmentTela["y"]:
                                head["y"] -= ind
                                possible = moveCheck(game, head)[1]
                                ind += 1
                            if possible == True:
                                result = "Down"
                            else:
                                pass
                        else:
                            result = "Down"
                elif moveLeftPossible:
                   for segmentTela in game["you"]["body"]:
                        if segmentTela["x"] <= game["you"]["head"]["x"]:
                            print("SEGMENT NEKDE VLEVO!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["x"] > segmentTela["x"]:
                                head["x"] -= ind
                                possible = moveCheck(game, head)[2]
                                ind += 1
                            if possible == True:
                                result = "Left"
                            else:
                                pass
                        else:
                            result = "Left"
                elif moveRightPossible:
                    for segmentTela in game["you"]["body"]:
                        if segmentTela["x"] >= game["you"]["head"]["x"]:
                            print("SEGMENT NEKDE VPRAVO!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["x"] < segmentTela["x"]:
                                head["x"] += ind
                                possible = moveCheck(game, head)[3]
                                ind += 1
                            if possible == True:
                                result = "Right"
                            else:
                                pass
                        else:
                            result = "Right"
                elif moveUpPossible:
                    for segmentTela in game["you"]["body"]:
                        if segmentTela["y"] >= game["you"]["head"]["y"]:
                            print("SEGMENT NEKDE NAHORE!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["y"] < segmentTela["y"]:
                                head["y"] += ind
                                possible = moveCheck(game, head)[0]
                                ind += 1
                            if possible == True:
                                result = "Up"
                            else:
                                pass
                        else:
                            result = "Up"
                    
                print("JIDLO POD HLAVOU")
                    
            ### Pokud je jídlo nad hlavou
            elif blizkeJidlo["y"] > game["you"]["head"]["y"]:
                if moveUpPossible:
                    for segmentTela in game["you"]["body"]:
                        if segmentTela["y"] >= game["you"]["head"]["y"]:
                            print("SEGMENT NEKDE NAHORE!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["y"] < segmentTela["y"]:
                                head["y"] += ind
                                possible = moveCheck(game, head)[0]
                                ind += 1
                            if possible == True:
                                result = "Up"
                            else:
                                pass
                        else:
                            result = "Up"
                elif moveLeftPossible:
                   for segmentTela in game["you"]["body"]:
                        if segmentTela["x"] <= game["you"]["head"]["x"]:
                            print("SEGMENT NEKDE VLEVO!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["x"] > segmentTela["x"]:
                                head["x"] -= ind
                                possible = moveCheck(game, head)[2]
                                ind += 1
                            if possible == True:
                                result = "Left"
                            else:
                                pass
                        else:
                            result = "Left"
                elif moveRightPossible:
                    for segmentTela in game["you"]["body"]:
                        if segmentTela["x"] >= game["you"]["head"]["x"]:
                            print("SEGMENT NEKDE VPRAVO!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["x"] < segmentTela["x"]:
                                head["x"] += ind
                                possible = moveCheck(game, head)[3]
                                ind += 1
                            if possible == True:
                                result = "Right"
                            else:
                                pass
                        else:
                            result = "Right"
                elif moveDownPossible:
                    for segmentTela in game["you"]["body"]:
                        if segmentTela["y"] <= game["you"]["head"]["y"]:
                            print("SEGMENT NEKDE DOLE!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["y"] > segmentTela["y"]:
                                head["y"] -= ind
                                possible = moveCheck(game, head)[1]
                                ind += 1
                            if possible == True:
                                result = "Down"
                            else:
                                pass
                        else:
                            result = "Down"
                    
                print("JIDLO NAD HLAVOU")
        else:
            if blizkeJidlo["x"] < game["you"]["head"]["x"]:
                if moveLeftPossible:
                    result = "Left"
                elif moveUpPossible:
                    result = "Up"
                elif moveDownPossible:
                    result = "Down"
                elif moveRightPossible:
                    result = "Right"
                        
                print("JIDLO VLEVO")
                        
            ### Pokud je jídlo v pravo od hlavy
            elif blizkeJidlo["x"] > game["you"]["head"]["x"]:
                if moveRightPossible:
                    result = "Right"
                elif moveUpPossible:
                   result = "Up"
                elif moveDownPossible:
                    result = "Down"
                elif moveLeftPossible:
                    result = "Left"
                            
                print("JIDLO VPRAVO")
                            
            ### Pokud je jídlo pod hlavou
            elif blizkeJidlo["y"] < game["you"]["head"]["y"]:
                if moveDownPossible:
                    result = "Down"
                elif moveLeftPossible:
                   result = "Left"
                elif moveRightPossible:
                    result = "Right"
                elif moveUpPossible:
                    result = "Up"
                    
                print("JIDLO POD HLAVOU")
                    
            ### Pokud je jídlo nad hlavou
            elif blizkeJidlo["y"] > game["you"]["head"]["y"]:
                if moveUpPossible:
                    result = "Up"
                elif moveLeftPossible:
                   result = "Left"
                elif moveRightPossible:
                    result = "Right"
                elif moveDownPossible:
                    result = "Down"
                    
                print("JIDLO NAD HLAVOU")
    else:
        if not len(game["you"]["body"]) == 0:
            if moveRightPossible:
                for segmentTela in game["you"]["body"]:
                        if segmentTela["x"] >= game["you"]["head"]["x"]:
                            print("SEGMENT NEKDE VPRAVO!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["x"] < segmentTela["x"]:
                                head["x"] += ind
                                possible = moveCheck(game, head)[3]
                                ind += 1
                            if possible == True:
                                result = "Right"
                            else:
                                pass
                        else:
                            result = "Right"
            if moveLeftPossible:
                for segmentTela in game["you"]["body"]:
                        if segmentTela["x"] <= game["you"]["head"]["x"]:
                            print("SEGMENT NEKDE VLEVO!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["x"] > segmentTela["x"]:
                                head["x"] -= ind
                                possible = moveCheck(game, head)[2]
                                ind += 1
                            if possible == True:
                                result = "Left"
                            else:
                                pass
                        else:
                            result = "Left"
            if moveUpPossible:
                for segmentTela in game["you"]["body"]:
                        if segmentTela["y"] >= game["you"]["head"]["y"]:
                            print("SEGMENT NEKDE NAHORE!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["y"] < segmentTela["y"]:
                                head["y"] += ind
                                possible = moveCheck(game, head)[0]
                                ind += 1
                            if possible == True:
                                result = "Up"
                            else:
                                pass
                        else:
                            result = "Up"
            if moveDownPossible:
                for segmentTela in game["you"]["body"]:
                        if segmentTela["y"] <= game["you"]["head"]["y"]:
                            print("SEGMENT NEKDE DOLE!!!")
                            head = game["you"]["head"]
                            ind = 1
                            while head["y"] > segmentTela["y"]:
                                head["y"] -= ind
                                possible = moveCheck(game, head)[1]
                                ind += 1
                            if possible == True:
                                result = "Down"
                            else:
                                pass
                        else:
                            result = "Down"
                            
        else:
            if moveRightPossible:
                result = "Right"
            elif moveLeftPossible:
                result = "Left"
            elif moveUpPossible:
                result = "Up"
            elif moveDownPossible:
                result = "Down"
        print("ZADNE JIDLO")
            
    print(moveRightPossible , "mozno do prava")
    print(moveLeftPossible , "mozno do leva")
    print(moveUpPossible  , "mozno nahoru")
    print(moveDownPossible  , "mozno dolu")
    print(result)
    return {'direction': result}
