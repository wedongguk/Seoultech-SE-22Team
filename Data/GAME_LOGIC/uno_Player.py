import random

class Player: # player 클래스 생성
    playerName = '' # 플레이어 이름
    isUser = True # user인가 bot인가 확인
    handCardList = [] # 들고 있는 카드
    uid = -1 # user id
    

    def __init__(self, player_name, is_user, uid = -1): # player 클래스 생성자
        self.playerName = player_name
        self.isUser = is_user
        self.handCardList = []
        self.uid = uid

    def __del__(self): # player class 소멸자
        if self.handCardList != []: # handCardList의 Card instance들을 모두 del 합니다.
            for i in self.handCardList:
                del i
            self.handCardList = []

    def draw(self, game, num): # game의 DeckList에서 카드를 뽑아 패로 가져옵니다.
        
        if (len(game.deckList.cardList) == 0) and (len(game.openCard.cardList) == 1):
            print("섞을 카드가 없어요")
        else:
            if len(game.deckList.cardList) < num: # 뽑을 카드 부족하면
                print('뽑을 카드가 없으므로 openCard를 가져오겠습니다.')
                top = game.openCard.takeTopCard() # 맨 위 카드 하나 빼놓고
                game.deckList + game.openCard.cardList # 나머지는 합쳐서
                game.deckList.shuffle() # 셔플
                game.openCard + [top] # 빼둔 카드 openCard에 둠
            
        
            for i in range(0, num): # num 만큼 반복
                result = self.drawOneCard(game)
                if result == 0:
                    print('뽑을 카드가 없어요')
                    break
            
    def drawOneCard(self, game):
        if len(game.deckList.cardList) != 0:
            self.handCardList.append(game.deckList.takeTopCard())
            return 1
        else:
            return 0
        
    def weighted_draw(self, game, num): # game의 DeckList에서 카드를 뽑아 패로 가져옵니다.
        
        if (len(game.deckList.cardList) == 0) and (len(game.openCard.cardList) == 1):
            print("섞을 카드가 없어요w")
        else:
            if len(game.deckList.cardList) < num: # 뽑을 카드 부족하면
                print('뽑을 카드가 없으므로 openCard를 가져오겠습니다.w')
                top = game.openCard.takeTopCard() # 맨 위 카드 하나 빼놓고
                game.deckList + game.openCard.cardList # 나머지는 합쳐서
                game.deckList.shuffle() # 셔플
                game.openCard + [top] # 빼둔 카드 openCard에 둠
            
        
            for i in range(0, num): # num 만큼 반복
                result = self.drawOneCardW(game)
                if result == 0:
                    print('뽑을 카드가 없어요w')
                    break
        
    def drawOneCardW(self, game):
        cardList = game.deckList.cardList
        if len(cardList) != 0:
            start = 0
            weightList = []
            for i in range(len(cardList)):
                if (cardList[i].effectCode & NO_EFFECT) == NO_EFFECT:
                    start += 2
                else:
                    start += 3
                weightList.append(start)
            
            randRange = random.randrange(0,start)
            start = 0
            idx = None
            for i in range(len(cardList)):
                if (start <= randRange) and (weightList[i] > randRange):
                    idx = i
                    break
                else:
                    start = weightList[i]
            self.handCardList.append(game.deckList.takeIdxCard(idx))
            return 1
        else:
            return 0
    
    def UnoAndWinnerChecker(self, game):
        if len(self.handCardList) == 0: # 카드를 내서 0장이 되면 게임이 끝난다.
            game.winner = self
                        
        if len(self.handCardList) == 1: # 카드를 내서 1장이 되면 우노 경쟁을 위한 처리를 시작한다.
            game.unoCompeteTable()
        
        print(self.playerName + ": ", self.allHand())
        print('topCard: '+game.openCard.cardList[-1].info())
        

    def allHand(self): # hand의 모든 카드에 대한 텍스트를 반환합니다.
        tempList = []
        handCardList = self.handCardList
        for i in range(0, len(handCardList)):
            tempList.append(handCardList[i].info())

        return tempList

    def delCard(self, index): # player의 카드를 삭제합니다. i : 삭제할 인덱스
        
        result = self.handCardList[index]
        del self.handCardList[index]
        
        return result
    
    def canUseIdx(self, game): # 낼 수 있는 카드의 인덱스 리스트를 반환합니다.
        chkList = []
        tpHand = self.handCardList
        
        for i in range(0, len(tpHand)):
            if tpHand[i].canUse(game) == True:
                chkList.append(i)
        
        return chkList

    def printCurSta(self): # 현재 Player 카드 리스트 ## 테스트할 필요 없다고 판단
        print(self.playerName + ": ", self.allHand(), "\n")
        
    def data(self): # Front에서 card instance의 정보를 dictionary로 확인하기 위한 메서드
        name = self.playerName
        isUser = self.isUser
        handList = self.handCardList
        
        result = {'playerName': name, 'isUser': isUser, 'handCardList': handList}
        
        return result
