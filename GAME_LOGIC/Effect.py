from Data.GAME_LOGIC.uno_Const import * # const

def effect(card, game):  # 특수 카드의 효과를 처리하기 위한 메서드.
    eCode = card.effectCode # eCode를 통해 어떤 종류인지 판단

    if eCode & EFFECT_SKIP == EFFECT_SKIP:  # 다음 플레이어를 스킵하는 효과
        effect_skip(game)

    if eCode & EFFECT_REVERSE == EFFECT_REVERSE:  # 턴의 진행 방향을 반대로 바꾸는 효과
        effect_reverse(game)
        
    if eCode & EFFECT_DRAW == EFFECT_DRAW:  # 다음 상대에게 카드를 주는 효과
        effect_draw(card, game)

    if eCode & EFFECT_COLOR == EFFECT_COLOR:  # 카드의 색을 바꾸는 효과
        effect_change_color(game)

    if eCode & EFFECT_NUMBER == EFFECT_NUMBER:  # 카드의 숫자를 바꾸는 효과
        effect_change_number(card)
        

def effect_draw(card, game):
    game.playerList.nextPlayer().draw(game, card.attackNumber)

def effect_skip(game):
    game.playerList.skip()

def effect_reverse(game):
    game.playerList.reverse()

def effect_change_color(game):
    time = None
    if game.playerList.turnPlayer().isUser == True:
        time = EFFECT_TIME
    else:
        time = BOT_EFFECT_TIME
        
    game.effectTimer.reset(time)
    game.is_selectColor = True
    game.is_effctTime = True

def effect_change_number(game):
    game.is_selectNumber = True
    game.is_effctTime = True