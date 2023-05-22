import pytest
from Data.GAME_LOGIC.uno_Const import *
from Data.GAME_LOGIC.uno_Card import Card
from Data.GAME_LOGIC.unoCore import Game
from Data.GAME_LOGIC.uno_Player import Player
from Data.GAME_LOGIC.uno_Const import *


@pytest.fixture
def game():
    p1 = Player('', True)
    p2 = Player('', False)
    g = Game([p1, p2],MODE_NORMAL)
    g.ready((100, 50))
    return g

def test_drawOneCard(game):
    
    card1 = Card(RED, 1)
    card2 = Card(GREEN, 2)
    card3 = Card(BLUE, 3)
    clist = [card1, card2, card3]
    
    game.deckList.cardList = clist
    p1 = Player('', True)
    p1.drawOneCard(game)
    
    assert p1.handCardList == [card3]
    assert game.deckList.cardList == [card1, card2]
    
    game.deckList.cardList = []
    p1 = Player('', True)
    p1.drawOneCard(game)
    
    assert p1.handCardList == []
    assert game.deckList.cardList == []
    
def test_draw(game):
    
    # deck 10, open 10에서 7장 뽑음
    game.deckList.cardList = [Card(RED, x) for x in range(0, 10)]
    game.openCard.cardList = [Card(RED, x) for x in range(0, 10)]
    p1 = Player('', True)
    
    p1.draw(game, 7)
    assert len(game.deckList.cardList) == 3
    assert len(game.openCard.cardList) == 10
    assert len(p1.handCardList) == 7
    
    # deck 3, open 10에서 5장 뽑음
    p1.draw(game, 5)
    assert len(game.deckList.cardList) == 7
    assert len(game.openCard.cardList) == 1
    assert len(p1.handCardList) == 12
    
    # deck 8, open 0에서 10장 뽑음
    p1.draw(game, 10)
    assert len(game.deckList.cardList) == 0
    assert len(game.openCard.cardList) == 1
    assert len(p1.handCardList) == 19
    
    # deck 0, open 0에서 2장 뽑음
    p1.draw(game, 2)
    assert len(game.deckList.cardList) == 0
    assert len(game.openCard.cardList) == 1
    assert len(p1.handCardList) == 19
    
def test_allHand(game):
    
    p1 = Player('', True)
    card1 = Card(RED, 1)
    card2 = Card(GREEN, 2)
    card3 = Card(BLUE, 3)
    clist = [card1, card2, card3]
    p1.handCardList = clist
    
    assert p1.allHand() == ['red_1', 'green_2', 'blue_3']
    
def test_delCard():
    
    p1 = Player('', True)
    card1 = Card(RED, 1)
    card2 = Card(GREEN, 2)
    card3 = Card(BLUE, 3)
    clist = [card1, card2, card3]
    p1.handCardList = clist
    p1.delCard(1)
    
    assert p1.handCardList == [card1, card3]
       
def test_data():
    p1 = Player('user', True)
    card1 = Card(RED, 1)
    card2 = Card(GREEN, 2)
    card3 = Card(BLUE, 3)
    clist = [card1, card2, card3]
    p1.handCardList = clist
    
    assert p1.data()['playerName'] == 'user'
    assert p1.data()['isUser'] == True
    assert p1.data()['handCardList'] == clist
    
    p2 = Player('bot', False)
    card1 = Card(RED, 3)
    card2 = Card(GREEN, 2)
    card3 = Card(BLUE, 1)
    clist = [card1, card2, card3]
    p2.handCardList = clist
    
    assert p2.data()['playerName'] == 'bot'
    assert p2.data()['isUser'] == False
    assert p2.data()['handCardList'] == clist


def test_UnoAndWinnerChecker(game):
    
    p1 = Player('', True)
    card1 = Card(RED, 1)
    p1.handCardList = [card1]
    
    p1.UnoAndWinnerChecker(game)
    
    assert game.state == UNO
    assert game.botCompeteList != []
    
    p2 = Player('', True)
    game.state == NORM
    p2.UnoAndWinnerChecker(game)
    
    assert game.winner != None
    
    
def test_drawOneCardW(game):
    
    selected = [0, 0]
    
    for i in range(500):
        game.deckList.cardList = [Card(RED, 1) for x in range(10)]
        game.deckList+ [Card(RED, -1, EFFECT_DRAW, 2) for x in range(10)]
        game.deckList.shuffle()
        
        p1 = Player('', True)
        p1.drawOneCardW(game)
        if p1.handCardList[-1].effectCode == EFFECT_DRAW:
            selected[0] += 1
        else:
            selected[1] += 1
    
    rate = selected[0]/(selected[0]+selected[1])
    testValue = False
    if (rate > 0.5) and (rate < 0.7):
        testValue = True
    
    assert testValue == True
    
## def weighted_draw와 def drawOneCardW에 대한 테스트 코드를 작성할 것
## printCurSta는 단순 프린트 함수이므로 테스트 코드를 작성하지 않아도 됨

    
## 해당 함수는 test_drawOneCardW에서 나오는 수치를 보기 위해서 만든 함수입니다.
"""
def printRate():    
    p1 = Player('', True)
    p2 = Player('', False)
    game = Game([p1, p2],MODE_NORMAL)
    game.ready((100, 50))
    
    selected = [0, 0]
    
    for i in range(500):
        game.deckList.cardList = [Card(RED, 1) for x in range(10)]
        game.deckList+ [Card(RED, -1, EFFECT_DRAW, 2) for x in range(10)]
        game.deckList.shuffle()
        
        p1 = Player('', True)
        p1.drawOneCardW(game)
        if p1.handCardList[-1].effectCode == EFFECT_DRAW:
            selected[0] += 1
        else:
            selected[1] += 1
        if (selected[0] > 0) and (selected[1] > 0):
            print(i,": ",selected[0]/(selected[0]+selected[1]))
            
    
    rate = selected[0]/(selected[0]+selected[1])
    print(rate)
    testValue = False
    if (rate > 0.5) and (rate < 0.7):
        testValue = True
"""    
#printRate()
        
    
