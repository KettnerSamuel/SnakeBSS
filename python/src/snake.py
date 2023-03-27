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
    #
    # SEM UMISTUJTE SVUJ KOD
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
    #
    
    # pro ukazku se vraci nahodny smer
    
