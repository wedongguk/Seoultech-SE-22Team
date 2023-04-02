from uno_Const import * # const
from uno_Card import Card


class Effect:
    effectCode = NO_EFFECT  # 카드가 가진 효과의 종류
    jumpNumber = 0
    color = -1
    number = -1


    def __init__(self): # uno_Effect 클래스 생성자
        self.jumpNumber = 0
        self.effectCode = NO_EFFECT

    def __del__(self): # uno_Effect 클래스 소멸자
        pass



    def cardEffect(self, game):  # 특수 카드의 효과를 처리하기 위한 메서드.
        eCode = self.effectCode # eCode를 통해 어떤 종류인지 판단

        if eCode & EFFECT_DRAW == EFFECT_DRAW:  # 다음 상대에게 카드를 주는 효과
            self.draw(game)

        if eCode & EFFECT_SKIP == EFFECT_SKIP:  # 다음 플레이어를 스킵하는 효과
            self.skip()

        if eCode & EFFECT_REVERSE == EFFECT_REVERSE:  # 턴의 진행 방향을 반대로 바꾸는 효과
            game.playerList = self.reverse(game)

        if eCode & EFFECT_COLOR == EFFECT_COLOR:  # 카드의 색을 바꾸는 효과
            self.change_color(game, self.color) # Uno_Effect.number 를 통해 원하는 숫자를 특정한다

        if eCode & EFFECT_NUMBER == EFFECT_NUMBER:  # 카드의 숫자를 바꾸는 효과
            self.change_number(game, self.number) # Uno_Effect.color 를 통해 원하는 컬러를 특정한다




    def draw(self, game):
        game.playerList[(game.turnPlayer+1)%len(game.playerList)].draw(game, 2)

    def skip(self):
        self.jumpNumber += 1

    def reverse(self, game):
        tp = game.turnPlayer  # 현재 턴 플레이어
        tmp_Lst = []

        for _ in range(len(game.playerList)):
            tp -= 1  # -1씩 순서를 바꿔주어
            tmp_Lst.append(game.playerList[tp])  # tmp_Lst에 바뀐 리스트를 변경해준다

        return tmp_Lst

    def change_color(self, game, color):
        game.openCard.pop() # 오픈 카드 리스트의 가장 위 카드를 삭제한다. 삭제하는게 맞을까 ?
        applycard = Card(color, NO_NUMBER, EFFECT_COLOR)

        game.openCard.append(applycard)  # 오픈 카드의 가장 윗 부분에 적용한 컬러 카드를 넣어준다.



    def change_number(self, game, number):
        game.openCard.pop()  # 가장 위 카드를 삭제한다.
        applycard = Card(NO_COLOR, number, EFFECT_NUMBER)

        game.openCard.append(applycard)  # 오픈 카드의 가장 윗 부분에 적용한 컬러 카드를 넣어준다.