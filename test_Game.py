import pytest
from Data.GAME_LOGIC.uno_PlayerList import PlayerList
from Data.GAME_LOGIC.uno_Player import Player
from Data.GAME_LOGIC.unoCore import Game
from Data.GAME_LOGIC.uno_Const import * # const

@pytest.fixture
def game():
    p1 = Player('', True)
    p2 = Player('', False)
    g = Game([p1, p2],MODE_NORMAL)
    return g

@pytest.fixture
def game_M():
    p1 = Player('', True, 100)
    p2 = Player('', True, 1000)
    g = Game([p1, p2],MODE_NORMAL)
    return g

def test_actList(game):
    game.playerList.nextTurn()
    assert game.actList()['drawBtn'] == True
    assert game.actList()['unoBtn'] == False
    assert game.actList()['colorBtn'] == False
    
    game.state = UNO
    assert game.actList()['drawBtn'] == True
    assert game.actList()['unoBtn'] == True
    assert game.actList()['colorBtn'] == False
    
    game.state = NORM
    game.playerList.nextTurn()
    assert game.actList()['drawBtn'] == False
    assert game.actList()['unoBtn'] == False
    assert game.actList()['colorBtn'] == False
    
    game.state = UNO
    assert game.actList()['drawBtn'] == False
    assert game.actList()['unoBtn'] == True
    assert game.actList()['colorBtn'] == False
    
    game.state = NORM
    game.is_effctTime = True
    game.is_selectColor = True
    assert game.actList()['drawBtn'] == False
    assert game.actList()['unoBtn'] == False
    assert game.actList()['colorBtn'] == True

'''    
def test_actList_M(game):
    game.playerList.nextTurn()
    assert game.actList()['drawBtn'] == True
    assert game.actList()['unoBtn'] == False
    assert game.actList()['colorBtn'] == False
    
    game.state = UNO
    assert game.actList()['drawBtn'] == True
    assert game.actList()['unoBtn'] == True
    assert game.actList()['colorBtn'] == False
    
    game.state = NORM
    game.playerList.nextTurn()
    assert game.actList()['drawBtn'] == False
    assert game.actList()['unoBtn'] == False
    assert game.actList()['colorBtn'] == False
    
    game.state = UNO
    assert game.actList()['drawBtn'] == False
    assert game.actList()['unoBtn'] == True
    assert game.actList()['colorBtn'] == False
    
    game.state = NORM
    game.is_effctTime = True
    game.is_selectColor = True
    assert game.actList()['drawBtn'] == False
    assert game.actList()['unoBtn'] == False
    assert game.actList()['colorBtn'] == True
'''