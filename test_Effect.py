import pytest
from Data.GAME_LOGIC.uno_Card import *
from Data.GAME_LOGIC.unoCore import *
from Data.GAME_LOGIC.uno_Player import *
from Data.GAME_LOGIC.uno_Const import *
from Data.GAME_LOGIC.Effect import *

@pytest.fixture
def game():
    p1 = Player('', True)
    p2 = Player('', False)
    p3 = Player('', False)
    g = Game([p1, p2, p3], MODE_NORMAL)
    return g

def test_effect_skip(game):
    game.playerList.nextTurn()
    effect_skip(game)
    game.playerList.nextTurn()
    assert game.playerList.turnIdx == 2
    
    effect_reverse(game)
    effect_skip(game)
    game.playerList.nextTurn()
    assert game.playerList.turnIdx == 0

def test_effect_reverse(game):
    ## 3명 이상
    game.playerList.nextTurn()
    effect_reverse(game)
    game.playerList.nextTurn()
    assert game.playerList.turnIdx == 2
    assert game.playerList.direction == -1
    
    effect_reverse(game)
    game.playerList.nextTurn()
    assert game.playerList.turnIdx == 0
    assert game.playerList.direction == 1
    
    ## 2명
    game.playerList.playerList.pop()
    effect_reverse(game)
    game.playerList.nextTurn()
    assert game.playerList.turnIdx == 0
    assert game.playerList.direction == -1
    
    effect_reverse(game)
    game.playerList.nextTurn()
    assert game.playerList.turnIdx == 0
    assert game.playerList.direction == 1


def test_effect_draw(game):   
    game.ready((100,10))
    card1 = Card(0, -1,EFFECT_DRAW, 2)
    effect_draw(card1, game)
    
    assert len(game.playerList.nextPlayer().handCardList) == 7
    
def test_effect_change_color(game):
    
    effect_change_color(game)
    assert game.is_selectColor == True
    assert game.is_effctTime == True