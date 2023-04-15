import random

from Timer import Timer2
from uno_Const import * # const
from uno_Pile import * # Pile Class
from uno_Player import * # Player Class
from uno_Card import * # Card Class
import uno_ChkCon # Check Condition

class Game: # game 클래스 생성
    deckList = [] # 남은 덱
    openCard = [] # 공개된 카드
    playerList = [] # 플레이어 목록
    turnPlayer = -1 # 현재 턴 플레이어
    attackCard = 0 # 공격 카드 매수
    step = 1 # 턴 종료시, 플레이어를 넘기는 정도
    state = NORM
    botCompeteList = []
    winner = [] # 게임이 진행중이라면 빈 테이블, winner player가 존재한다면 0번 인덱스에 넣는다.
    
    is_effctTime = False
    timer2 = Timer2(30)
    effectTimer2 = Timer2(10)

    def __init__(self, player_list): # game 클래스 생성자
        self.playerList = player_list
        self.deckList = Pile()
        self.openCard = Pile()
        state = NORM
        turnPlayer = -1
        attackCard = 0
        step = 1
        botCompeteList = []
        winner = []
        
    def __del__(self): # game class 소멸자
        del self.deckList
        del self.openCard
        if self.playerList != []: # playerList의 player instance들을 모두 del 합니다.
            for i in self.playerList:
                del i
            self.playerList = []

    def ready(self, screen_size): #게임을 준비하는 메서드
        deckPreset = self.setDeck(screen_size) # 사전에 정의한 덱 리스트
        
        self.deckList + deckPreset # 덱에 deckPreset을 넣는다.
        self.deckList.shuffle()
        
        for i in range(0, len(self.playerList)): # 각 플레이어들에게 카드를 나눠줍니다.
            self.playerList[i].draw(self, 5) # 나눠줄 카드의 개수 : 임의로 5로 설정했음
            print(self.playerList[i].playerName + ": ", self.playerList[i].allHand(),"\n")
            
        self.placeOpenCardZone(self.deckList.takeTopCard()) # 덱 맨 위에서 카드를 1장 오픈합니다.
        print("TopCard" +": " + self.openCard.cardList[-1].info()+"\n")

    def placeOpenCardZone(self, Card): #OpenCardList에 카드를 놓습니다.
        lst = []
        lst.append(Card)
        self.openCard + lst
    
        # self.openCard.cardList.append(Card)
        Card.cardEffect(self)

    def setDeck(self, screen_size): # 게임에 사용할 덱의 CardList를 반환합니다.
        tempList = []
        for i in range(0, 4): # 0~9까지의 4색 카드를 임시 리스트에 넣습니다.
            for j in range(0, 10):
                card = Card(i, j, NO_EFFECT)
                card.default_image = pygame.transform.smoothscale(pygame.image.load(f"images/{Card.imgColor(card)}_{Card.imgValue(card)}.png"), (screen_size[0] / 12.5, screen_size[0] / 8.333))
                tempList.append(card)

        for i in range(0, 4): # 색상이 필요한 특수 카드
            for j in [0B10, 0B100, 0B1000]:
                if j == 0B10 :
                    card = Card(i, NO_NUMBER, j , attackNumber=2)
                else :
                    card = Card(i, NO_NUMBER, j)
                card.default_image = pygame.transform.smoothscale(pygame.image.load(f"images/{Card.imgColor(card)}_{Card.imgValue(card)}.png"), (screen_size[0] / 12.5, screen_size[0] / 8.333))
                tempList.append(card)

        for _ in range(0, 2): # 색상이 불필요한 특수카드
            for j in [0B10000, 0B100000]:
                card = Card(NO_COLOR, NO_NUMBER, j)
                card.default_image = pygame.transform.smoothscale(pygame.image.load(f"images/{Card.imgColor(card)}_{Card.imgValue(card)}.png"), (screen_size[0] / 12.5, screen_size[0] / 8.333))
                tempList.append(card)
                
        return tempList
    
    def executeTurn(self): # 현재는 쓰지 않음
        
        if self.playerList[self.turnPlayer].isUser == True: # 턴 플레이어가 유저
                self.mainPhase()
                #print("User",self.playerList[self.turnPlayer].playerName, "의 턴")
        else: # 턴 플레이어가 봇
            self.unoBot()
        
        result = self.endPhase()
        return result # 게임이 끝났는지, 승자는 누구인지
    
    def mainPhase(self): ## 현재는 쓰지 않음
        if self.attackCard > 0: # 공격 처리
            self.playerList[self.turnPlayer].draw(self, self.attackCard)
            self.attackCard = 0 # attactCard 리셋
        
        cond = True
        while cond:
            print("TopCard" +": " + self.openCard.cardList[-1].info()+"\n")
            print(self.playerList[self.turnPlayer].playerName + ": ", self.playerList[self.turnPlayer].allHand())
            print("카드 내기: p, 카드 뽑기: d")
            input_act = input()
            if input_act == 'p':
                print("낼 카드의 인덱스를 입력하세요")
                input_num = int(input())
                '''
                turn flow
                카드 사용 여부 체크
                True
                    특수카드 여부 체크
                    True
                        0. effect 타이머 업데이트
                        1. 해당 카드 플레이어 리스트에서 삭제
                        2. 해당 카드 OpenZone에 넣기
                        3. 특수 카드 효과 실행
                        4. cond 속성 False 변경
                    False
                        0. 일반 타이머 업데이트
                        1. 2. 4 실행
                False
                    1. 낼 수 없습니다 출력
                    2. 카드 한장을 덱에서 뽑음
                    3. cond 속성 False 변경
                
                다시 반복  
                '''
                if self.playerList[self.turnPlayer].handCardList[input_num].canUse(self): # 사용 가능 여부 체크
                    if self.playerList[self.turnPlayer].handCardList[input_num].checkEffect(self): #Effect 카드 인지 판단
                        self.effectTimer2.update() # effect 타이머 업데이트
                        useCard = self.playerList[self.turnPlayer].delCard(input_num) # 사용한 카드 삭제
                        self.placeOpenCardZone(useCard) #OpenZome 에 카드 넣기
                        useCard.effect.cardEffect(self) # 특수 카드 효과 실행
                        cond = False
                    else:
                        self.timer2.update() # 일반 타이머 업데이트
                        if self.playerList[self.turnPlayer].handCardList[input_num].canUse(self):  # 사용 가능 여부 체크
                            useCard = self.playerList[self.turnPlayer].delCard(input_num)  # 사용한 카드 삭제
                            self.placeOpenCardZone(useCard)  # OpenZome 에 카드 넣기
                            cond = False
                else:
                    print("그 카드는 낼 수 없습니다.")
            if input_act == 'd':
                print("카드를 1장 뽑습니다.")
                self.playerList[self.turnPlayer].draw(self, 1)
                cond = False
            else:
                pass
            
            print(self.playerList[self.turnPlayer].playerName + ": ", self.playerList[self.turnPlayer].allHand())
        
        print()
    
    def actList(self): # 현재 활성화야햐하는 버튼의 딕셔너리를 반환
        result = {'drawBtn': True,'unoBtn': True} # 'drawBtn': 드로우 버튼, 'unoBtn': 우노 버튼
        if (self.playerList[self.turnPlayer].isUser == False):
            result['drawBtn'] = False
            
        if (self.state == NORM):
            result['unoBtn'] = False
            
        return result
    
    def eventCardBtn(self, idx): # 카드 클릭시 이벤트
        if self.playerList[self.turnPlayer].isUser == True:
            if self.playerList[self.turnPlayer].handCardList[idx].canUse(self) == True:
                useCard = self.playerList[self.turnPlayer].delCard(idx)
                self.placeOpenCardZone(useCard)
            else:
                print("그 카드는 낼 수 없어요")
        else:
            print("아직 당신의 턴이 아니에요")
        
        if len(self.playerList[self.turnPlayer].handCardList) == 0: # 카드를 내서 0장이 되면 게임이 끝난다.
            self.winner = [self.playerList[self.turnPlayer]]
            
        if len(self.playerList[self.turnPlayer].handCardList) == 1: # 카드를 내서 1장이 되면 우노 경쟁을 위한 처리를 시작한다.
            pass # 봇간 우노 경쟁 메서드
        
        self.endPhase()
    
    def eventDrawBtn(self): # 드로우 버튼 클릭시 이벤트
        self.playerList[self.turnPlayer].draw(self, 1)
        self.endPhase()
    
    def eventUnoBtn(self): # 우노 버튼 클릭시 이벤트
        self.state == NORM
        if self.playerList[self.turnPlayer-1].isUser == True: # 나의 우노가
            pass # 저지당하지 않았다.
        else: # 다른 사람의 우노를
            self.playerList[self.turnPlayer-1].draw(self, 1) # 저지했다.
    
    def endPhase(self): # endPhase를 실행
        self.turnPlayer = (self.turnPlayer+self.jumpNumber)%len(self.playerList) # 점프 처리
        self.step = 1 # jumpNumber 리셋
    
    def update(self): # timer2, effectimer2 갱신용
        if (self.is_effctTime == False): # 기본 타이머
            self.timer2.update()
            self.timeEvent()
        else: # 기술 카드 효과 적용시 타이머
            self.effectTimer2.update()
            
    def timeEvent(self): # 특정 시간이 되었다면, 특정 함수를 실행함.
        ## 우노 경쟁
        if self.state == UNO:
            remainTime = -1
            if self.playerList[self.turnPlayer].isUser == True:
                remainTime = USER_TIME
            else:
                remainTime = BOT_TIME      
            n = remainTime-min(self.botCompeteList)
            if self.timer2.time <= n:
                self.processUno(self.botCompeteList.index(n))
        
        ## timeOver
        if self.timer2.time <= 0:
             if self.playerList[self.turnPlayer].isUser == True: # user의 턴
                 self.eventDrawBtn()
             else: # bot의 턴
                 self.unoBot()
    
    def unoBot(self): # 봇의 턴    
        chkList = self.playerList[self.turnPlayer].canUseIdx(self)
        
        if chkList != []: # 낼 수 있는 카드가 있다면
            randIdx = random.choice(chkList) # 무작위의 카드를 내고
            useCard = self.playerList[self.turnPlayer].delCard(randIdx)
            self.placeOpenCardZone(useCard)
            print( useCard.info() + "를 냅니다.")
        else:             # 낼 수 있는 카드가 없다면
            self.playerList[self.turnPlayer].draw(self, 1) # 카드를 뽑고
            print("낼 카드가 없어서 1장 뽑습니다.")
        
        print(self.playerList[self.turnPlayer].playerName + ": ", self.playerList[self.turnPlayer].allHand())
        print()
        print()
        self.endPhase()
        
    def processUno(self, idx): # 누군가 우노를 외쳤을 때, 게임에서 실질적으로 바뀌는 부분에 대한 처리
        if self.state == UNO:
            self.state = NORM
            
            if self.turnPlayer-1 == idx: # (턴 플레이어 -1) = 전 턴의 플레이어 = 우노 상태를 만든 당사자
                print(self.playerList[idx].playerName,'가 UNO 우노를 외쳤습니다.')
            else: # 그 외의 플레이어
                print(self.playerList[idx].playerName,'가', self.playerList[self.turnPlayer-1].playerName,' 의 UNO 우노를 저지했습니다.')
                self.playerList[self.turnPlayer-1].draw(self, 1)
        else:
            print('state == UNO에서만 이 메서드가 동작합니다.')
    
    def searchUserIdx(self): # 하나의 user만 있을 때 동작합니다.
        result = -1
        for i in range(0, len(self.playerList)):
            if self.playerList[i].isUser == True:
                result = i
                break
        
        return result
        
    def userHand(self): # 유저의 패 리스트를 반환합니다.
        result = self.playerList[self.searchUserIdx()].handCardList
        
        return result
    
    def playerTurnTable(self): # 플레이어의 턴 순서를 표시하기 위한 정보를 반환합니다.
        
        result = []
        for i in range(0, len(self.playerList)):
            idx = (i+self.turnPlayer)%len(self.playerList)
            result.append(self.playerList[idx])
        return result
 

## 테스트용 ##
'''
user1 = Player('USER', True)
pcard = Player('Pcard', False)
pc2 = Player('PC2', False)
pc3 = Player('PC3', False)

gamePlayerList = [user1, pcard, pc2, pc3]
g = Game(gamePlayerList)

g.ready()
'''