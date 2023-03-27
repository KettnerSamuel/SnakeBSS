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
    
    ### Kontrola hran hracího pole
    if game["you"]["head"]["x"] == 0:
        moveLeftPossible = False
    if game["you"]["head"]["x"] == game["board"]["width"] - 1:
        moveRightPossible = False
    if game["you"]["head"]["y"] == 0:
        moveDownPossible = False
    if game["you"]["head"]["y"] == game["board"]["height"] - 1:
        moveUpPossible = False
        
    ### Kontrola našeho těla
    if not len(game["you"]["body"]) == 0:
        for telo in game["you"]["body"]:
            if game["you"]["head"]["x"] == telo["x"] - 1:
                moveRightPossible = False
            if game["you"]["head"]["x"] == telo["x"] + 1:
                moveLeftPossible = False
            if game["you"]["head"]["y"] == telo["y"] - 1:
                moveDownPossible = False
            if game["you"]["head"]["y"] == telo["y"] + 1:
                moveUpPossible = False
            
    ### Kontrola překážek
    if not len(game["board"]["obstacles"]) == 0:
        for prekazka in game["obstacles"]:
            if game["you"]["head"]["x"] == prekazka["x"] - 1:
                moveRightPossible = False
            if game["you"]["head"]["x"] == prekazka["x"] + 1:
                moveLeftPossible = False
            if game["you"]["head"]["y"] == prekazka["y"] - 1:
                moveDownPossible = False
            if game["you"]["head"]["y"] == prekazka["y"] + 1:
                moveUpPossible = False
                
    ##### JDE PO JIDLE #####
    if not len(game["board"]["food"]) == 0:
        ### Pokud je jídlo v levo od hlavy
        if game["board"]["food"][0]["x"] < game["you"]["head"]["x"]:
            if moveLeftPossible:
                result = "Left"
            elif moveUpPossible:
                result = "Up"
            elif moveDownPossible:
                result = "Down"
            elif moveRightPossible:
                result = "Right"
                    
        ### Pokud je jídlo v pravo od hlavy
        elif game["board"]["food"][0]["x"] > game["you"]["head"]["x"]:
            if moveRightPossible:
                result = "Right"
            elif moveUpPossible:
               result = "Up"
            elif moveDownPossible:
                result = "Down"
            elif moveLeftPossible:
                result = "Left"
                        
        ### Pokud je jídlo pod hlavou
        elif game["board"]["food"][0]["y"] < game["you"]["head"]["y"]:
            if moveDownPossible:
                result = "Down"
            elif moveLeftPossible:
               result = "Left"
            elif moveRightPossible:
                result = "Right"
            elif moveUpPossible:
                result = "Up"
                  
        ### Pokud je jídlo nad hlavou
        elif game["board"]["food"][0]["x"] > game["you"]["head"]["x"]:
            if moveUpPossible:
                result = "Up"
            elif moveLeftPossible:
               result = "Left"
            elif moveRightPossible:
                result = "Right"
            elif moveDownPossible:
                result = "Down"
        
    else:
        if moveRightPossible:
            result = "Right"
        if moveLeftPossible:
            result = "Left"
        if moveUpPossible:
            result = "Up"
        if moveDownPossible:
            result = "Down"
            
    print(moveRightPossible)
    print(moveLeftPossible)
    print(moveUpPossible)
    print(moveDownPossible)
    print(result)
    return {'direction': result}
