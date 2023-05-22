import pytest
from Data.GAME_LOGIC.uno_Const import * # const
from Data.GAME_LOGIC.uno_Card import *
from Data.GAME_LOGIC.unoCore import *
from Data.GAME_LOGIC.uno_Player import *

@pytest.fixture
def card():
    return Card()

@pytest.fixture
def game():
    p1 = Player('', True)
    p2 = Player('', False)
    g = Game([p1, p2],MODE_NORMAL)
    return g

def test_init(card):
    assert card.color == NO_COLOR
    assert card.number == NO_NUMBER
    assert card.effectCode == NO_EFFECT
    assert card.attackNumber == -1
    assert card.applyNumber == NO_NUMBER
    assert card.applyColor == NO_COLOR

def test_reset(card):
    card.applyColor = 1
    card.applyNumber = 2
    card.reset()
    assert card.applyColor == card.color
    assert card.applyNumber == card.number

def test_imgName(card):
    card.color = RED
    card.number = 3
    assert card.imgName() == "red_3"
    
    card.color = GREEN
    card.number = NO_NUMBER
    card.effectCode = EFFECT_SKIP
    assert card.imgName() == "green_skip"
    
    card.color = YELLOW
    card.effectCode = EFFECT_REVERSE
    assert card.imgName() == "yellow_reverse"
    
    card.color = BLUE
    card.attackNumber = 2
    card.effectCode = EFFECT_DRAW
    assert card.imgName() == "blue_+2"
    
    card.effectCode = EFFECT_DRAW+EFFECT_REVERSE
    assert card.imgName() == "blue_+2reverse"
    
    card.color = NO_COLOR
    card.effectCode = EFFECT_DRAW+EFFECT_COLOR
    card.attackNumber = 4
    assert card.imgName() == "black_+4wildColor"
    
    card.color = NO_COLOR
    card.effectCode = EFFECT_COLOR
    card.attackNumber = -1
    assert card.imgName() == "black_wildColor"
    
def test_canUse(game):
    c1 = Card(RED, 8)
    c2 = Card(GREEN, 7)
    game.openCard.cardList.append(c1)
    assert c2.canUse(game) == False
    
    c1 = Card(RED, 7)
    c2 = Card(GREEN, 7)
    game.openCard.cardList.append(c1)
    assert c2.canUse(game) == True
    
    c1 = Card(RED, NO_NUMBER, EFFECT_DRAW, 2)
    c2 = Card(GREEN, NO_NUMBER, EFFECT_DRAW+EFFECT_REVERSE, 2)
    game.openCard.cardList.append(c1)
    assert c2.canUse(game) == True
    
    c1 = Card(RED, NO_NUMBER, EFFECT_SKIP)
    c2 = Card(GREEN, NO_NUMBER, EFFECT_REVERSE)
    game.openCard.cardList.append(c1)
    assert c2.canUse(game) == False
    
def test_imgColor(card):
    card.color = RED
    assert card.imgColor() == "red"
    card.color = BLUE
    assert card.imgColor() == "blue"
    card.color = NO_COLOR
    assert card.imgColor() == "black"

def test_imgValue(card):
    card.number = 3
    assert card.imgValue() == "3"
    
    card.number = NO_NUMBER
    card.effectCode = EFFECT_DRAW
    card.attackNumber = 2
    assert card.imgValue() == "+2"
    
    card.effectCode = EFFECT_SKIP
    assert card.imgValue() == "skip"
    
    card.effectCode = EFFECT_REVERSE
    assert card.imgValue() == "reverse"
    
    card.effectCode = EFFECT_DRAW+EFFECT_REVERSE
    assert card.imgValue() == "+2reverse"
    
    card.effectCode = EFFECT_COLOR
    assert card.imgValue() == "wildColor"
    
    card.effectCode = EFFECT_DRAW+EFFECT_COLOR
    card.attackNumber = 4
    assert card.imgValue() == "+4wildColor"

def test_data(card):
    card.color = 1
    card.number = 4
    card.effectCode = EFFECT_SKIP
    card.attackNumber = 2
    card.applyColor = 2
    card.applyNumber = 7
    assert card.data() == {'orignColor': 1, 'orignNumber': 4, 'effctCode': 0B100, 'attackNumber': 2, 'applyColor': 2, 'applyNumber': 7}

