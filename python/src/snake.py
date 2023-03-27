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
        
    
    if moveLeftPossible == True:
        if moveUpPossible == False:
            
        
    ### Kontrola těla
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
    else:
        pass
            
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
    else:
        pass
    
    
        
    ##### POHYB SMĚREM K JÍDLU #####
    if len(game["board"]["food"]) > 0:
        
        if game["you"]["head"]["x"] < game["board"]["food"][0]["x"]:
            if moveRightPossible == True:
                result = 'Right'
            elif game["you"]["head"]["y"] < game["board"]["food"][0]["y"]:
                if moveUpPossible == True:
                    result = 'Up'
            else:
                if moveDownPossible == True:
                    result = 'Down'
                    
        elif game["you"]["head"]["x"] > game["board"]["food"][0]["x"]:
            if moveLeftPossible == True:
                result = 'Left'
            elif game["you"]["head"]["y"] < game["board"]["food"][0]["y"]:
                if moveUpPossible == True:
                    result = 'Up'
            else:
                if moveDownPossible == True:
                    result = 'Down'
                    
        elif game["you"]["head"]["y"] < game["board"]["food"][0]["y"]:
            if moveUpPossible == True:
                result = 'Up'
            elif game["you"]["head"]["x"] < game["board"]["food"][0]["x"]:
                if moveRightPossible == True:
                    result = 'Right'
            else:
                if moveLeftPossible == True:
                    result = 'Left'
                    
        elif game["you"]["head"]["y"] > game["board"]["food"][0]["y"]:
            if moveLeftPossible == True:
                result = 'Left'
            elif game["you"]["head"]["x"] < game["board"]["food"][0]["x"]:
                if moveRightPossible == True:
                    result = 'Right'
            else:
                if moveLeftPossible == True:
                    result = 'Left'

    print(result)
    
    return {'direction': result}
