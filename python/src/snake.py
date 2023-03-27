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
    if game["head"]["x"] == 0:
        moveRightPossible = False
    if game["head"]["x"] == game["board"]["width"] - 1:
        moveLeftPossible = False
    if game["head"]["y"] == 0:
        moveDownPossible = False
    if game["head"]["y"] == game["board"]["height"] - 1:
        moveUpPossible = False
        
    ### Kontrola těla
    if game["snakes"]["body"] != {}
        for telo in game["snakes"]["body"]:
            if game["head"]["x"] == telo["x"] - 1:
                moveRightPossible = False
            if game["head"]["x"] == telo["x"] + 1:
                moveLeftPossible = False
            if game["head"]["y"] == telo["y"] - 1:
                moveDownPossible = False
            if game["head"]["y"] == telo["y"] + 1:
                moveUpPossible = False
    else:
        pass
            
    ### Kontrola překážek
    if game["obstacles"] != {}:
        for prekazka in game["obstacles"]:
            if game["head"]["x"] == prekazka["x"] - 1:
                moveRightPossible = False
            if game["head"]["x"] == prekazka["x"] + 1:
                moveLeftPossible = False
            if game["head"]["y"] == prekazka["y"] - 1:
                moveDownPossible = False
            if game["head"]["y"] == prekazka["y"] + 1:
                moveUpPossible = False
    else:
        pass
    
    return {'direction': result}
