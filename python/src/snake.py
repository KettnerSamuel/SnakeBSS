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
    
    result = "Right"
    
    moveRightPossible = True
    moveLeftPossible = True
    moveUpPossible = True
    moveDownPossible = True
    
    ##### KONTROLY MOŽNÝCH POHYBŮ #####
    
    ### Kontrola hran hracího pole
    if game["you"]["head"]["x"] == 0:
        moveRightPossible = False
    if game["you"]["head"]["x"] == game["board"]["width"] - 1:
        moveLeftPossible = False
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
    else:
        pass
    
    ### Kontrola nepřátelského hada
    if not len(game["board"]["snakes"]) == 0:
        for had in game["board"]["snakes"]:
            ### Kontrola hlavy nepřátelského hada
            if game["you"]["head"]["x"] == had["head"]["x"] - 1:
                moveRightPossible = False
            if game["you"]["head"]["x"] == had["head"]["x"] + 1:
                moveLeftPossible = False
            if game["you"]["head"]["y"] == had["head"]["y"] - 1:
                moveDownPossible = False
            if game["you"]["head"]["y"] == had["head"]["y"] + 1:
                moveUpPossible = False
                
            ### Kontrola těla nepřátelského hada
            for teloHada in had["body"]:
                if game["you"]["head"]["x"] == teloHada["x"] - 1:
                    moveRightPossible = False
                if game["you"]["head"]["x"] == teloHada["x"] + 1:
                    moveLeftPossible = False
                if game["you"]["head"]["y"] == teloHada["y"] - 1:
                    moveDownPossible = False
                if game["you"]["head"]["y"] == teloHada["y"] + 1:
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
    else:
        pass
        
    ##### POHYB SMĚREM K JÍDLU #####
    if game["you"]["head"]["x"] + game["board"]["food"]["x"] > game["you"]["head"]["y"] + game["board"]["food"]["y"]:
        if game["you"]["head"]["x"] < game["board"]["food"]["x"]:
            if moveLefttPossible == True:
                result = 'Left'
            else:
                if game["you"]["head"]["y"] < game["board"]["food"]["y"]:
                    if moveUpPossible == True:
                        result = 'Up'
                elif game["you"]["head"]["y"] > game["board"]["food"]["y"]:
                    if moveDownPossible == True:
                        result = 'Down'
                else:
                    pass
                
        if game["you"]["head"]["x"] > game["board"]["food"]["x"]:
            if moveRightPossible == True:
                result = 'Right'
            else:
                if game["you"]["head"]["y"] < game["board"]["food"]["y"]:
                    if moveUpPossible == True:
                        result = 'Up'
                elif game["you"]["head"]["y"] > game["board"]["food"]["y"]:
                    if moveDownPossible == True:
                        result = 'Down'
                else:
                    pass
                
    elif game["you"]["head"]["x"] - game["board"]["food"]["x"] < game["you"]["head"]["y"] - game["board"]["food"]["y"]:
        if game["you"]["head"]["y"] < game["board"]["food"]["y"]:
            if moveUpPossible == True:
                result = 'Up'
            else:
                if game["you"]["head"]["x"] > game["board"]["food"]["x"]:
                    if moveRightPossible == True:
                        result = 'Right'
                elif game["you"]["head"]["x"] < game["board"]["food"]["x"]:
                    if moveLefttPossible == True:
                        result = 'Left'
                else:
                    pass
                        
        elif game["you"]["head"]["y"] > game["board"]["food"]["y"]:
            if moveDownPossible == True:
                result = 'Down'
            else:
                if game["you"]["head"]["x"] > game["board"]["food"]["x"]:
                    if moveRightPossible == True:
                        result = 'Right'
                elif game["you"]["head"]["x"] < game["board"]["food"]["x"]:
                    if moveLefttPossible == True:
                        result = 'Left'
                else:
                    pass
    elif game["you"]["head"]["x"] + game["board"]["food"]["x"] == game["you"]["head"]["y"] + game["board"]["food"]["y"]:
        pass

    print(result)
    
    return {'direction': result}
