import pytest
from Data.GAME_LOGIC.uno_Const import * # const
from Data.GAME_LOGIC.uno_Card import *
from Data.GAME_LOGIC.unoCore import *
from Data.GAME_LOGIC.uno_ChkCon import *

def test_canUse():
    # 숫자가 같음
    top_card = Card(RED, 5)
    chk_card = Card(BLUE, 5)
    assert canUse(top_card, chk_card) == True

    # 색깔이 같음
    top_card = Card(YELLOW, 6)
    chk_card = Card(YELLOW, 2)
    assert canUse(top_card, chk_card) == True

    # top의 applyColor와 chk의 Color와 같음
    top_card = Card(NO_COLOR, NO_NUMBER, EFFECT_COLOR)
    top_card.applyColor = GREEN
    chk_card = Card(GREEN, 2)
    assert canUse(top_card, chk_card) == True

    # chk가 NO_COLOR라면 언제든지 낼 수 있음 
    top_card = Card(GREEN, 4)
    chk_card = Card(NO_COLOR, NO_NUMBER, EFFECT_COLOR)
    assert canUse(top_card, chk_card) == True

    # chk_eCode를 통과한 카드라면 낼 수 있음
    top_card = Card(RED, NO_NUMBER, EFFECT_SKIP)
    chk_card = Card(YELLOW, NO_NUMBER, EFFECT_SKIP)
    assert canUse(top_card, chk_card) == True

    # 모든 조건을 통과하지 못한 코드는 내지 못함
    top_card = Card(RED, 5)
    chk_card = Card(BLUE, 7)
    assert canUse(top_card, chk_card) == False
    
    top_card = Card(RED, NO_NUMBER, EFFECT_SKIP)
    chk_card = Card(YELLOW, NO_NUMBER, EFFECT_REVERSE)
    assert canUse(top_card, chk_card) == False

def test_chk_eCode():
    # EFFECT_DRAW의 경우 chk의 atkNum이 top과 같거나 크면 낼 수 있다.
    top_card = Card(GREEN, NO_NUMBER, EFFECT_DRAW, 2)
    chk_card = Card(YELLOW, NO_NUMBER, EFFECT_DRAW, 2)
    assert chk_eCode(top_card, chk_card) == True
    
    top_card = Card(GREEN, NO_NUMBER, EFFECT_DRAW, 2)
    chk_card = Card(YELLOW, NO_NUMBER, EFFECT_DRAW, 4)
    assert chk_eCode(top_card, chk_card) == True
    
    # EFFECT_DRAW의 경우 chk의 atkNum이 top과 작으면 낼 수 없다.
    top_card = Card(GREEN, NO_NUMBER, EFFECT_DRAW, 4)
    chk_card = Card(YELLOW, NO_NUMBER, EFFECT_DRAW, 2)
    assert chk_eCode(top_card, chk_card) == False
    
    # EFFECT_DRAW 이외의 경우, effectCode의 1의 자리를 제외하고 겹치는 부분이 있다면 무조건 True
    top_card = Card(GREEN, NO_NUMBER, EFFECT_SKIP)
    chk_card = Card(YELLOW, NO_NUMBER, EFFECT_SKIP, 2)
    assert chk_eCode(top_card, chk_card) == True
    
    top_card = Card(GREEN, NO_NUMBER, EFFECT_REVERSE)
    chk_card = Card(YELLOW, NO_NUMBER, EFFECT_REVERSE+EFFECT_DRAW, 2)
    assert chk_eCode(top_card, chk_card) == True
    
    # effectCode의 1의 자리를 제외하고 겹치는 부분이 없다면 낼 수 없다.
    top_card = Card(GREEN, NO_NUMBER, EFFECT_SKIP)
    chk_card = Card(YELLOW, NO_NUMBER, EFFECT_REVERSE)
    assert chk_eCode(top_card, chk_card) == False
    
    top_card = Card(GREEN, NO_NUMBER, EFFECT_REVERSE)
    chk_card = Card(YELLOW, NO_NUMBER, EFFECT_DRAW, 2)
    assert chk_eCode(top_card, chk_card) == False
