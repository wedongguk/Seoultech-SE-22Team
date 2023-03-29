import random
from uno_Const import * # const
from uno_Pile import * # Pile Class
from uno_Player import * # Player Class
from uno_Card import * # Card Class
import uno_ChkCon # Check Condition

class game: # game 클래스 생성
    deckList = [] # 남은 덱
    openCard = [] # 공개된 카드
    playerList = [] # 플레이어 목록
    turnPlayer = -1 # 현재 턴 플레이어
    attackCard = 0 # 공격 카드 매수
    step = 1 # 턴 종료시, 플레이어를 넘기는 정도
    state = NORM
    botCompeteList = []
    winner = [] # 게임이 진행중이라면 빈 테이블, winner player가 존재한다면 0번 인덱스에 넣는다. 


    def __init__(self, player_list): # game 클래스 생성자
        self.playerList = player_list
        self.deckList = pile()
        self.openCard = pile()
        state = NORM
        turnPlayer = -1
        attackCard = 0
        step = 1
        botCompeteList = []
        winner = []
        

    def __del__(self): # game class 소멸자
        pass

    def ready(self): #게임을 준비하는 메서드
        deckPreset = self.setDeck() # 사전에 정의한 덱 리스트
        
        self.deckList + deckPreset # 덱에 deckPreset을 넣는다.
        self.deckList.shuffle()
        
        for i in range(0, len(self.playerList)): # 각 플레이어들에게 카드를 나눠줍니다.
            self.playerList[i].draw(self, 5) # 나눠줄 카드의 개수 : 임의로 5로 설정했음
            print(self.playerList[i].playerName + ": ", self.playerList[i].allHand(),"\n")
            
        self.placeOpenCardZone(self.deckList.takeTopCard()) # 덱 맨 위에서 카드를 1장 오픈합니다.
        print("TopCard" +": " + self.openCard.cardList[-1].info()+"\n")
        
        

    def placeOpenCardZone(self, card): #OpenCardList에 카드를 놓습니다.
        lst = []
        lst.append(card)
    
        self.openCard + lst
        card.cardEffect(self)

    def setDeck(self): # 게임에 사용할 덱의 CardList를 반환합니다.
        tempList = []
        for i in range(0, 4): # 0~9까지의 4색 카드를 임시 리스트에 넣습니다.
            for j in range(0, 10):
                tempList.append(card(i, j))

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
                if self.playerList[self.turnPlayer].handCardList[input_num].canUse(self):
                    useCard = self.playerList[self.turnPlayer].delCard(input_num)
                    self.placeOpenCardZone(useCard)
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

user1 = player('USER', True)
pc1 = player('PC1', False)
pc2 = player('PC2', False)
pc3 = player('PC3', False)

gamePlayerList = [user1, pc1, pc2, pc3]
g = game(gamePlayerList)

g.ready()