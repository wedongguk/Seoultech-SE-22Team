import pytest
from Data.GAME_LOGIC.uno_Card import Card
from Data.GAME_LOGIC.uno_Pile import Pile
from Data.GAME_LOGIC.uno_Const import * # const

def test_init():
    # 카드 리스트가 비어있는 Pile 인스턴스를 생성합니다.
    pile = Pile()
    assert pile.cardList == []

    # 카드 리스트를 포함하는 Pile 인스턴스를 생성합니다.
    card1 = Card(RED, 1)
    card2 = Card(GREEN, 2)
    clst = [card1, card2]
    pile = Pile(clst)
    assert pile.cardList == [card1, card2]

def test_shuffle():
    # 카드 리스트를 섞기 전과 후의 순서가 다르면 성공합니다.
    clist = []
    for i in range(4):
        for j in range(10):
            clist.append(Card(i, j))

    pile = Pile(clist)
    original_order = pile.cardList.copy()
    pile.shuffle()
    assert pile.cardList != original_order

def test_takeTopCard():
    # 가장 위의 카드를 가져오는 메서드가 정상적으로 작동하면 성공합니다.
    card1 = Card(RED, 1)
    card2 = Card(GREEN, 2)
    card3 = Card(BLUE, 3)
    pile = Pile([card1, card2, card3])
    
    top_card = pile.takeTopCard()
    assert top_card == card3
    assert pile.cardList == [card1, card2]

def test_takeIdxCard():
    # 주어진 인덱스의 카드를 가져오는 메서드가 정상적으로 작동하면 성공합니다.
    card1 = Card(RED, 1)
    card2 = Card(GREEN, 2)
    card3 = Card(BLUE, 3)
    pile = Pile([card1, card2, card3])
    
    idx_card = pile.takeIdxCard(1)
    assert idx_card == card2
    assert pile.cardList == [card1, card3]

def test_add():
    # Pile 인스턴스끼리 더하는 메서드가 정상적으로 작동하면 성공합니다.
    card1 = Card(RED, 1)
    card2 = Card(GREEN, 2)
    card3 = Card(BLUE, 3)
    pile1 = Pile([card1, card2])
    lst = [card3]
    
    pile1 + lst
    assert pile1.cardList == [card1, card2, card3]
    assert lst == []

def test_printlist():
    # 카드 리스트의 정보를 출력하는 메서드가 정상적으로 작동하면 성공합니다.
    card1 = Card(RED, 1)
    card2 = Card(GREEN, 2)
    pile = Pile([card1, card2])
    assert pile.printlist() == [card1.info(), card2.info()]

def test_data():
    card1 = Card(RED, 1)
    card2 = Card(GREEN, 2)
    pile = Pile([card1, card2])
    assert pile.data()['cardList'] == [card1, card2]