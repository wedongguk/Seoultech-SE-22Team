import pygame
from uno_Const import * # const
import uno_ChkCon # Check Condition

class Card(pygame.sprite.Sprite): # 카드 클래스 생성
    ## 카드의 오리지널 데이터 ##    
    color = NO_COLOR # 0: red, 1: green, 2: yellow, 3: blue, -1: none_color_card
    number = NO_NUMBER # -1: special_card
    effectCode = NO_EFFECT # 카드가 가진 효과의 종류
    attackNumber = -1
    
    ## 카드가 게임에서 실제로 적용되는 데이터 ##
    applyColor = NO_COLOR
    applyNumber = NO_NUMBER
    
    def __init__(self, color = NO_COLOR, number = NO_NUMBER, effectCode = NO_EFFECT, attackNumber = -1): # card 클래스 생성자
        super().__init__()
        self.color = color
        self.number = number
        self.effectCode = effectCode
        self.attackNumber = attackNumber
        self.applyNumber = self.number # applyNumber 는 cardNumber 로 초기값 설정
        self.applyColor = self.color # applyColor 는 cardColor 로 초기값 설정
        self.screen_size = (1280, 720)
        self.default_image = pygame.transform.smoothscale(pygame.image.load(f"images/back.png"), (self.screen_size[0] / 10, self.screen_size[1] / 5))
        self.rect = self.default_image.get_rect()
        
            
    def __del__(self): # card class 소멸자
        pass
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return True
        else : 
            return False

    def cardEffect(self, game): # 특수 카드의 효과를 처리하기 위한 메서드.
        eCode = self.effectCode
        if eCode & EFFECT_DRAW == EFFECT_DRAW: # 다음 상대에게 카드를 주는 효과
            game.playerList[(game.turnPlayer+1)%len(game.playerList)].draw(game, self.attackNumber)
        
        if eCode & EFFECT_SKIP == EFFECT_SKIP: # 다음 플레이어를 스킵하는 효과
            self.jumpNumber += 1

        if eCode & EFFECT_REVERSE == EFFECT_REVERSE: # 턴의 진행 방향을 반대로 바꾸는 효과
            tp = game.turnPlayer
            tmp_Lst = []

            for _ in range(len(game.playerList)):
                tp -= 1
                tmp_Lst.append(game.playerList[tp])

        if eCode & EFFECT_COLOR == EFFECT_COLOR: # 카드의 색을 바꾸는 효과
            applyColor = int(input())
            
        if eCode & EFFECT_NUMBER == EFFECT_NUMBER: # 카드의 숫자를 바꾸는 효과
            applyColor = int(input())
        
    def canUse(self, game):
        top = game.openCard.cardList[-1]
        result = uno_ChkCon.canUse(top.number, top.color, top.applyColor, top.applyNumber, self.number, self.color)

        return result

    def info(self): # 카드 정보 출력용 함수
        colorDict = {NO_COLOR:'None', RED:'red', GREEN:'green', YELLOW:'yellow', BLUE:'blue'}
        return colorDict[self.color] + ' ' + str(self.number)
    
    def imgColor(self): # 카드에 연결될 이미지의 스트링에 대한 데이터를 반환
        result = COLOR_TABLE[self.color]
        return result
    
    def imgValue(self):
        result = ''
        temp = ''
        if self.number != NO_NUMBER:
            temp = str(self.number)
        else:
            if self.effectCode & EFFECT_DRAW == EFFECT_DRAW:
                temp += '+' + str(self.attackNumber)
            if self.effectCode & EFFECT_SKIP == EFFECT_SKIP:
                temp += 'skip'
            if self.effectCode & EFFECT_REVERSE == EFFECT_REVERSE:
                temp += 'reverse'
            if self.effectCode & EFFECT_COLOR == EFFECT_COLOR:
                temp += 'wildColor'
            if self.effectCode & EFFECT_NUMBER == EFFECT_NUMBER:
                temp += 'wildNumber'
        result += temp
        
        return result
    
    def data(self): # Front에서 card instance의 정보를 dictionary로 확인하기 위한 메서드
        o_Col = self.color
        o_Num = self.number
        e_Code = self.effectCode
        atk_Num = self.attackNumber
        
        a_Col = self.applyColor
        a_Num = self.applyNumber
        
        result = {'orignColor': o_Col, 'orignNumber': o_Num, 'effctCode': e_Code, 'attackNumber': atk_Num, 'applyColor': a_Col,'applyNumber': a_Num}
        
        return result
    
#test code#

#c1 = Card(RED, 2)
#c2 = Card(RED, effectCode = EFFECT_DRAW+EFFECT_REVERSE, attackNumber = 2)
#c3 = Card(NO_COLOR, effectCode = EFFECT_DRAW, attackNumber = 4)

#print(c1.imgName(), c2.imgName(), c3.imgName())